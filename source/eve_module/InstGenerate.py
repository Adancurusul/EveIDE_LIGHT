
from RtlGenerator import *
#import rtl_generator
mode_list = ['gen_inst_only','gen_inst_wc']
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename",required=True)
    parser.add_argument("-target",default='wrapper.v')
    parser.add_argument("-modulename")
    parser.add_argument("-mode",choices=mode_list,default=mode_list[0])
    options = parser.parse_args()
    return options
def get_arg(options,option):
    if hasattr(options,option):
        arg = getattr(options,option)
        return arg
    else:
        return None 
def compile_regex(**key_args):
    regex_dict={}
    if 'module_head' in key_args.keys():
        regex_module_head = re.compile(r'''
        (module\s+)
        (%s)
        ''' %(key_args['module_head']),re.VERBOSE)
        regex_dict['module_head'] = regex_module_head
    if 'module_ports' in key_args.keys():
        regex_module_ports = re.compile(r'''
        (output|input|inout)         #1 direction
        (\s+)                         #2
        (wire|reg)?                   #3 
        (\[[\w\-\:]+\])?              #4  width
        (\s+)?                        #5
        (\w+)                         #6   port name
        ''',re.VERBOSE)
        regex_dict['module_ports'] = regex_module_ports
    if 'width' in key_args.keys():
        regex_width = re.compile(r'''
        (\[)
        ([\w\-\:]+)
        (\])
        ''',re.VERBOSE)
        regex_dict['width'] = regex_width
    return regex_dict
rg = Rtl_generator()
if __name__ == "__main__":
    options = create_arg_parser()
    #print(options)
    file_name_arg = get_arg(options,"filename")
    module_name_arg=get_arg(options,"modulename")
    work_mode_arg = get_arg(options,"mode")
    target_file_arg = get_arg(options,"target")
    (filepath,filename_we) = os.path.split(file_name_arg)
    (filename,ext) = os.path.splitext(filename_we)
    rg.module_name = filename if module_name_arg is None else module_name_arg
    print('file name:{}\t\tmodule name:{}'.format(filename_we,rg.module_name))
    regex_dict = compile_regex(module_head=rg.module_name,module_ports=True,width=True)
    rg.get_module_specified_lines(regex_dict['module_head'],file_name_arg)
    #rg.display_list_for_test(rg.extract_list)
    rg.extract_ports_info(regex_dict['module_ports'],regex_dict['width'])
    #rg.display_list_for_test(rg.info_list)
    rg.gen_module_instance(target_file_arg,work_mode_arg)
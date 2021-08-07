'''=================================================
@Project -> File   ：EveIDE_Plus -> CreateInstanceNew
@IDE    ：PyCharm
@Author ：Adancurusul
@Date   ：2021/8/7 10:10
=================================================='''
# !/usr/bin/env python
# coding=utf-8
import os
import re
import argparse
import glob


class sources:
    def __init__(self, file_name=None, module_name=None, ins_mode='inst_&_wire', ins_name=None, indentation=30,
                 tar_file_name=None):
        self.file_name = file_name
        self.module_name = module_name
        self.ins_mode = ins_mode
        self.indentation = indentation
        self.ins_name = ins_name

        self.tar_file_name = tar_file_name
        self.head_lines = []
        self.write_list = []
        print("Start parsing {}...".format(self.file_name))
        self.get_module(self.module_name)
        #self.write_list.append(['module {}();'.format('DUT')])
        for module_head_lines in self.head_lines:
            module_curr = module(module_head_lines[0], list(module_head_lines[2:]), self.ins_mode, self.ins_name,
                                 self.indentation)
            self.write_list.append(module_curr.out_line_list)
        #self.write_list.append(['endmodule\n'])
        self.gen_file(self.write_list)

    def get1stSymPos(self,s, fromPos = 0):
        g_DictSymbols = {'"': '"', '/*': '*/','//':'\n'}
        listPos = [] #位置,符号
        for b in g_DictSymbols:
            pos = s.find(b, fromPos)
            listPos.append((pos,b)) #插入位置以及结束符号
        minIndex = -1 #最小位置在listPos中的索引
        index = 0 #索引
        while index < len(listPos):
            pos = listPos[index][0] #位置
            if minIndex < 0 and pos >= 0: #第一个非负位置
                minIndex = index
            if 0 <= pos < listPos[minIndex][0]: #后面出现的更靠前的位置
                minIndex = index
            index = index+1
        if minIndex == -1: #没找到
            return (-1,None)
        else:
            return (listPos[minIndex])

    def rmComments(self,s):
        g_DictSymbols = {'"': '"', '/*': '*/','//':'\n'}

        if not isinstance(s, str):
            raise TypeError(s)
        fromPos = 0
        while(fromPos < len(s)):
            result = self.get1stSymPos(s,fromPos)
            #logging.info(result)
            if result[0] == -1: #没有符号了
                return s
            else:
                endPos = s.find(g_DictSymbols[result[1]],result[0]+len(result[1]))
                if result[1] == '//': # 单行注释
                    if endPos == -1: #没有换行符也可以
                        endPos = len(s)
                    s = s.replace(s[result[0]:endPos],' ',1)
                    fromPos = result[0]
                elif result[1] == '/*': #区块注释
                    if endPos == -1: #没有结束符就报错
                        raise ValueError("块状注释未闭合")
                    s = s.replace(s[result[0]:endPos+2],' ',1)
                    fromPos = result[0]
                else: #字符串
                    if endPos == -1: #没有结束符就报错
                        raise ValueError("符号未闭合")
                    fromPos = endPos + len(g_DictSymbols[result[1]])
        return s

    def get_module(self, module_name=None):
        regex_module_head = re.compile(r'''
            [^\w]*module\s*
            (%s)                                   #1 module name
            (\s*\#\s*\(\s*parameter\s*)?           #2
            ((?(2)(?:.*\n)*?[^/\n]*(?:/[^/\n]+)*)) #3 parameter
            (?(2)\s*\)(?://.*\n)?)
            \s*\(\s*
            ((?:.*\n)*?[^/\n]*(?:/[^/\n]+)*)       #4 ports
            \s*\)[ \t]*?;(?://.*\n)?
            (.*)                                   #5 comments
            [\s\S]*?endmodule
            ''' % (module_name if module_name is not None else '\w+'), re.VERBOSE)

        file_obj = open(self.file_name, 'r',encoding="utf-8")
        file_str = file_obj.read()
        file_str = self.rmComments(file_str)
        file_obj.close()
        self.head_lines = re.findall(regex_module_head, file_str)

    def gen_file(self, write_list=[]):
        try:
            if self.__class__.gen_file.called:
                wr_mode = 'a'
        except AttributeError:
            self.__class__.gen_file.called = True
            wr_mode = 'w'

        with open(self.tar_file_name, '{}'.format(wr_mode),encoding="utf-8") as file_obj:
            for module in write_list:
                for line in module:
                    file_obj.write(line)
                    file_obj.write('\n')
        print('{} in {} been instanced successfully into {}!'.format(
            'All the modules' if self.module_name is None else 'Module ' + self.module_name,
            self.file_name + ' have' if self.module_name is None else self.file_name + ' has',
            self.tar_file_name))


class module:
    regex_module_params = re.compile(r'''
        (\w+)                                 #1 param name
        \s*=\s*
        ([()\w\s+\-*:]+(?:/?[()\w\s+\-*:]+)+) #2 value
        \s*,?\s*
        (//.*)?                               #3 comment
        ''', re.VERBOSE)
    regex_module_ports = re.compile(r'''
        (output|input|inout)                  #1 direction
        \s*
        (wire|reg)?                           #2 type
        \s*
        (\[.*?:.*?\]\s*)*           #3 width
        \s*
        ((?:\w+                               #4 port name
        \s*
        (?:,|;)?)+)
        \s*
        (//.*)?                               #5 comment
        ''', re.VERBOSE)
    tb_initial = '''
        bit Clk  ;
        bit Clear;
        bit Rstn ;

        initail forever #2.5 Clk = ~Clk;//200MHz
        initial
        begin
            repeat (5) @posedge( Clk );
            Rstn <= 'b1
        end
        '''

    def __init__(self, module_name=None, extract_list=[], ins_mode='inst_&_wire', ins_name=None, indentation=30):
        self.ins_mode = ins_mode
        self.ins_name = ins_name
        self.indentation = indentation
        self.module_name = module_name
        self.params_list = list(extract_list[0].rstrip('\n').split('\n')) if len(extract_list[0]) else []
        self.ports_list = list(extract_list[1].rstrip('\n').split('\n'))
        self.comment = extract_list[2]
        self.params_info_list = []
        self.ports_info_list = []
        self.out_line_list = []
        print("Start parsing module {}...".format(self.module_name))
        if self.params_list:
            self.get_params()
        self.get_ports()
        self.instance()

    def get_params(self):
        for line in self.params_list:
            re_params_obj = re.search(module.regex_module_params, line)
            if re_params_obj is not None:
                params_info = {'flag': 1,
                               'name': re_params_obj.group(1),
                               'value': re_params_obj.group(2),
                               'comment': re_params_obj.group(3) if re_params_obj.group(3) is not None else ""}

            else:
                params_info = {'flag': 0, 'comment': line}
            self.params_info_list.append(params_info)
        pass

    def get_ports(self):
        for line in self.ports_list:
            re_ports_obj = re.search(module.regex_module_ports, line)
            if re_ports_obj is not None:
                port_info = {'flag': 1,
                             'direction': re_ports_obj.group(1),
                             'type': re_ports_obj.group(2) if re_ports_obj.group(2) is not None else "wire",
                             'width': re_ports_obj.group(3) if re_ports_obj.group(3) is not None else "",
                             'name': re_ports_obj.group(4).rstrip(',|;'),
                             'comment': re_ports_obj.group(5) if re_ports_obj.group(5) is not None else ""}
            else:
                port_info = {'flag': 0, 'comment': line}
            self.ports_info_list.append(port_info)

    def instance(self):
        params_num = len(self.params_info_list)
        params_max_width_of_name = max(
            [len(str(line['name'])) for line in self.params_info_list if line['flag']]) if params_num > 0 else 0
        params_max_width_of_value = max(
            [len(str(line['value'])) for line in self.params_info_list if line['flag']]) if params_num > 0 else 0

        ports_num = len(self.ports_info_list)
        ports_max_width_of_width = max([len(str(line['width'])) for line in self.ports_info_list if line['flag']])
        ports_max_width_of_name = max([len(str(line['name'])) for line in self.ports_info_list if line['flag']])
        ports_max_width_of_name_s = max(
            [len(str(port_name)) for line in self.ports_info_list if line['flag'] for port_name in
             line['name'].split(',')])

        ins_max_width_of_name = max(params_max_width_of_name, ports_max_width_of_name_s, self.indentation)
        ins_max_width_of_value = max(params_max_width_of_value, ports_max_width_of_name_s, self.indentation)

        # wire declariton
        if ins_mode != 'inst_only':
            for i in range(ports_num):
                if self.ports_info_list[i]['flag']:
                    self.out_line_list.append(
                        '{:<4} {:>{}} {:<{}};{}'.format('reg' if self.ports_info_list[i]['type'] == 'reg' else 'wire',
                                                        self.ports_info_list[i]['width'], ports_max_width_of_width,
                                                        self.ports_info_list[i]['name'], ports_max_width_of_name,
                                                        self.ports_info_list[i]['comment']))
                else:
                    self.out_line_list.append('{}'.format(self.ports_info_list[i]['comment'].lstrip()))
            self.out_line_list.append('\n')
            if ins_mode == 'inst_tb':
                for line in module.tb_initial.split('\n'):
                    self.out_line_list.append(line.lstrip())

        # intance
        if params_num > 0:
            self.out_line_list.append('{} #\n('.format(self.module_name))
            for i in range(params_num):
                if self.params_info_list[i]['flag']:
                    self.out_line_list.append(
                        '.{:<{}} ( {:<{}} ){}{}'.format(self.params_info_list[i]['name'], ins_max_width_of_name,
                                                        self.params_info_list[i]['value'], ins_max_width_of_value,
                                                        ',' if i < params_num - 1 else "",
                                                        self.params_info_list[i]['comment']))
                else:
                    self.out_line_list.append('{}'.format(self.params_info_list[i]['comment'].lstrip()))
            self.out_line_list.append(
                ')\n{}\n('.format(self.ins_name if self.ins_name is not None else self.module_name + '_inst'))
        else:
            self.out_line_list.append('{} {}\n('.format(self.module_name,
                                                        self.ins_name if self.ins_name is not None else self.module_name + '_U0'))

        for i in range(ports_num):
            if self.ports_info_list[i]['flag']:
                for port_name in self.ports_info_list[i]['name'].split(','):
                    self.out_line_list.append('.{:<{}} ( {:<{}} ){}{}'.format(port_name, ins_max_width_of_name,
                                                                              port_name, ins_max_width_of_value,
                                                                              ',' if i < ports_num - 1 else "",
                                                                              self.ports_info_list[i]['comment']))
            else:
                self.out_line_list.append('{}'.format(self.ports_info_list[i]['comment'].lstrip()))

        self.out_line_list.append(');{}\n'.format(self.comment))


def arg_parser():
    parser = argparse.ArgumentParser(allow_abbrev=True)
    parser.add_argument("-f", "-filename", metavar="inputfile", dest='filename')
    parser.add_argument("-module", metavar="modulename", help='specify one module in the file')
    parser.add_argument("-insmode", choices=['0', '1', '2'],
                        help='0:{};1:{};2:{}'.format(ins_mode_list[0], ins_mode_list[1], ins_mode_list[2]), default=0)
    parser.add_argument("-insname", metavar="insmodulename", help='specify the module name of instance', type=str)
    parser.add_argument("-indent", metavar="indentation", help='specify the indentation of instance', type=int,
                        default=30)
    parser.add_argument("-fout", metavar="outputfile", help='specify the output file', default='DUT.sv')

    # parser.print_help()
    options = vars(parser.parse_args())
    file_name = options["filename"]
    module_name = options["module"]
    ins_mode = ins_mode_list[int(options["insmode"])]
    ins_name = options["insname"]
    indentation = options["indent"]
    tar_file_name = options["fout"]
    print(
        'input file    : {}\nmodule name   : {}\ninstance mode : {}\noutput file   : {}'.format(file_name, module_name,
                                                                                                ins_mode,
                                                                                                tar_file_name))
    return file_name, module_name, ins_mode, ins_name, indentation, tar_file_name

ins_mode = 'inst_&_wire'
def CreateInstance(inputFile, outputFile):
    sources(file_name = inputFile,tar_file_name=outputFile,ins_mode = 'inst_&_wire')

# --Main-----------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ins_mode_list = ['inst_&_wire', 'inst_only', 'inst_tb']
    file_name, module_name, ins_mode, ins_name, indentation, tar_file_name = arg_parser()

    file_list = [f for f in glob.glob('*.v') + glob.glob('*.sv') if
                 not re.match(r'DUT.sv', f)] if file_name is None else file_name.split(' ')
    for file in file_list:
        sources(file, module_name, ins_mode, ins_name, indentation, tar_file_name)


import re
import argparse
import os
class Rtl_generator:
    def __init__(self):
        self.extract_list=[]
        self.info_list=[]
        self.module_name = None

    @staticmethod 
    def display_list_for_test(list_name):
        print('list :\n')
        for unit in list_name:
            print(unit)
    def get_module_specified_lines(self,regex,file_name):
        print('input function: get_module_specified\n')
        with open(file_name,'r') as file_obj:
            add_flag = 0
            for line in file_obj:
                line = line.strip()
                if not line.startswith('//'):
                    re_head_obj = re.match(regex,line)
                    re_tail_obj = re.match(r'endmodule',line)
                    if re_head_obj is not None:
                        add_flag = 1
                    elif add_flag == 1 and re_tail_obj is not None:
                        add_flag = 0
                        break
                else:
                    continue
                if add_flag == 1:
                    self.extract_list.append(line)
    def extract_ports_info(self,regex_ports, regex_width):
        print('input function: get_ports_info\n')
        for unit in self.extract_list:
            re_ports_obj = re.search(regex_ports,unit)
            if re_ports_obj is not None:
                port_name = re_ports_obj.group(6)#得到ports
                port_direction = re_ports_obj.group(1)#方向
                port_width_str = re_ports_obj.group(4)#位宽
                if port_width_str is None:
                    port_width = 1
                else:
                    #port_width = port_width_str
                    width_str = re.search(regex_width,port_width_str).group(2)
                    width_info_list = width_str.split(":")
                    high_str = width_info_list[0]#高位
                    low_str = width_info_list[1]#低位
                    if '-1' in high_str:
                        port_width = high_str.split("-")[0]
                    else:
                        high = int(high_str)
                        low = int(low_str)
                        port_width = high - low + 1 if high >= low else low - high + 1
                port_info = {'name':port_name,'direct':port_direction,'width':port_width}
                self.info_list.append(port_info)
    def gen_module_instance(self,filename,mode):
        print('input function: gen_module_instance')
        ports_num = len(self.info_list)
        line_list = []
        line_list.append('module wrapper();')
        if mode == 'gen_inst_wc':
            for i in range(ports_num):
                var_type = 'reg' if self.info_list[i]['direct'] == 'input' else 'wire'
                line_list.append('{:<5} [{}-1:0] {};'.format(var_type,
                                                         self.info_list[i]['width'],
                                                         self.info_list[i]['name']))
            line_list.append('\n')
        line_list.append('{} inst_name'.format(self.module_name))
        line_list.append('(')
        index = 0
        for unit in self.info_list:
            if index == ports_num - 1:
                post_fix = '//{:<15}width:{}'.format(unit['direct'], unit['width'])
            else:
                post_fix = ',//{:<15}width:{}'.format(unit['direct'], unit['width'])
            index+=1
            if mode == 'gen_inst_wc':
                line_list.append('.{:<30}{:<30}{}'.format(unit['name'], '('+unit['name']+')', post_fix))
            elif mode == 'gen_inst_only':
                line_list.append('.{:<30}{:<5}{}'.format(unit['name'], '(' + ')', post_fix))
        line_list.append(');')
        line_list.append('endmodule\n')
        with open(filename,'w') as file_obj:
            for line in line_list:
                file_obj.write(line)
                file_obj.write('\n')
        print('generate instance finish')


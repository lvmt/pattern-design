#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-07-08 11:23:37
@Last Modified by:   lvmengting
@Last Modified time: 2022-07-08 11:23:37
'''


'''
解释:处理对象创建,客户端可以申请一个对象而不用知道对象被哪个class创建.可以方便地解耦对象的使用和创建.有两种实现, 工厂方法和抽象工厂.
'''

import json
import xml.etree.ElementTree as etree



class JSONConnector:

    def __init__(self, filepath):
        self.data = {}
        with open(filepath, 'r', encoding='utf-8') as fr:
            self.data = json.load(fr)

    @property
    def parsed_data(self):
        return self.data 


class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    '''工厂方法'''
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endsiwth('xml'):
        connector = XMLConnector
    else:
        raise ValueError(f'cannot  connect to {filepath}')
    return connector(filepath)

print(connection_factory('a.json').parsed_data)  # 为啥是parsed_data, 而不是parsed_data()

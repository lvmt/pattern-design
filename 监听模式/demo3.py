#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author:lvmengting
@Date:2022/07/21 16:28:57
'''

import time  
from abc import ABCMeta, abstractclassmethod



class Oberser(metaclass=ABCMeta):
    
    '''观察者基类'''
    def update(self, observable, object):
        pass  
    
    
class Observerable:
    '被观察者基类'
    
    def __init__(self):
        self.__observers = []
        
    def add_observer(self, observer):
        self.__observers.append(observer)
        
    def remove_observer(self, observer):
        self.__observers.remove(observer)
        
    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)
            

class Account(Observerable):
    '''用户账户，被监听对象'''
    
    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__latest_region = {}    
        
    
    def login(self, name, ip, time):
        region = self.get_region(ip)
        if self.is_long_distance(name, region):
            self.notify_observers({'name': name, 'ip': ip, 'region': region, 'time': time})
            
        self.__latest_region[name] = region 
        self.__latest_ip[name] = ip
    
    
    def get_region(self, ip):
        ip_regions = {
            '101.47.18.9': '浙江省杭州市',
            '67.218.147.69': '美国洛杉矶'
        }
        region = ip_regions.get(ip, '')
        return  region 
    
    
    def is_long_distance(self, name, region):
        '''
        计算本次登录与最近几次登录的地区差异
        '''
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region  
    
    
class SmsSender(Oberser):
    
    def update(self, observerable, object):
        print(f'【短信发送】, {object["name"]} 您好，检测到你的账户可能登录异常，最近一次的登录信息是：{object["region"]}, {object["ip"]}')
    
    
    
if __name__ == '__main__':
    account = Account()
    account.add_observer(SmsSender())
    
    account.login('tony', '101.47.18.9', time.time())
    account.login('tony', '67.218.147.69', time.time())
    
        
    
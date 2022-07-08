#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-07-08 10:25:53
@Last Modified by:   lvmengting
@Last Modified time: 2022-07-08 10:25:53
'''


from abc import ABCMeta, abstractclassmethod


class Factory(metaclass=ABCMeta):

    @abstractclassmethod
    def get_price(self):
        pass 

    @abstractclassmethod
    def set_price(self, price):
        pass 

    @abstractclassmethod
    def get_name(self):
        pass 



# 抽象 汉堡
class Burger(Factory):
    name = ''
    price = 0
    
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name 


class cheeseBurger(Burger):
    def __init__(self):
        self.name = 'cheese burger'
        self.price = 10


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = 'spicy chiken  burger'
        self.price = 15


## 抽象 小吃
class Snack(Factory):
    name = ''
    price = 0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name 
    

class chips(Snack):
    def __init__(self):
        self.name = 'chips'
        self.price = 6 


class chickenWings(Snack):
    def __init__(self):
        self.name = 'chicken wings'
        self.price = 12


# 抽象 饮料
class Beverage(Factory):
    name = ''
    price = 0
    type = 'BEVERAGE'

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name  


class coke(Beverage):
    def __init__(self):
        self.name = 'coke'
        self.price = 4


class mike(Beverage):
    def __init__(self):
        self.name = 'mike'
        self.price = 5



# 抽象 工厂
class foodFactory:
    type = ''

    def createFood(self, foodclass):
        print(self.type, 'factory produce a instance')
        return foodclass()

    
class burgerFactory(foodFactory):
    def __init__(self):
        self.type = 'BURGER'


class snackFactory(foodFactory):
    def __init__(self):
        self.type = 'SNACK'

    
class beverageFactory(foodFactory):
    def __init__(self):
        self.type = 'BEVERAGE'



if __name__ == '__main__':
    burger_factory = burgerFactory()
    snack_factory = snackFactory()
    beverage_factory = beverageFactory()

    cheese_burger = burger_factory.createFood(cheeseBurger)
    chicken_wings = snack_factory.createFood(chickenWings)
    coke_drink = beverage_factory.createFood(coke)

    print(cheese_burger.name, cheese_burger.price)
    
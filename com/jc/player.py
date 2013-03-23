'''
Created on 22 Mar 2013
Tennis player

@author: Javi Carretero
'''
class Player(object):
    """Class representing a Tennis player"""
    def __init__(self, name, surname, nick_name, rank):
        self.__name = name
        self.__surname = surname
        self.__nick_name = nick_name
        self.__rank = rank
        
    def getName(self):
        return self.__name
    def getNickName(self):
        return self.__nick_name
    def getSurname(self):
        return self.__surname
    def rank(self):
        return self.__rank
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __str__(self):
        if(self.__nick_name is not None):
            return self.__nick_name
        return self.__name + " " + self.__surname
        
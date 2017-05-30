#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
class BasicAuthenticationUser(AGitHubUser.AGitHubUser):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def __GetUsername(self):
        return self.__username
    Username = property(__GetUsername)
    
    def __GetPassword(self):
        return self.__password
    Password = property(__GetPassword)
    
    def CreateHeaders(self):
        return {}

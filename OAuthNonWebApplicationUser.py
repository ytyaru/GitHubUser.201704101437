#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
class OAuthNonWebApplicationUser(AGitHubUser.AGitHubUser):
    def __init__(self, token):
        self.__token = token
    
    def __GetAccessToken(self):
        return self.__token
    AccessToken = property(__GetAccessToken)
    
    def CreateHeaders(self):
        return {"Authorization": "token " + self.AccessToken}

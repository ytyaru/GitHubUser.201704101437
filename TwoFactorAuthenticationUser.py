#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import AGitHubUser
import BasicAuthenticationUser
class TwoFactorAuthenticationUser(BasicAuthenticationUser.BasicAuthenticationUser):
    def __init__(self, username, password, secret):
        super().__init__(username, password)
        self.__secret = secret
    
    def __GetOtp(self):
        # self.__secretを使って算出する
        return None
    OneTimePassword = property(__GetOtp)
    
    def CreateHeaders(self):
        return {"X-GitHub-OTP": self.OneTimePassword}

import os
from configparser import ConfigParser

def read_configuration(category,key):
    config = ConfigParser()
    #config.read(r"C:\Users\PurviDholakia\PycharmProjects\CROWD_TestAutomationFramework\Configurations\config.ini")
    raise ValueError(f"Current path: {os.getcwd()}")

    try:
	    file = open("../Configurations/config.ini")
	    print(f"Got the config file successfully: {file}")
	    config.read(file);
	    return config.get(category,key)
	except:
		raise ValueError("Failed to read configuration file")





























# import configparser
# from configparser import ConfigParser
#
# config = configparser.RawConfigParser("")
# #config.read(".\\Configurations\\config.ini")
# config.read("Configurations/config.ini");
# class ReadConfig:
#
#     @staticmethod
#     def getBrowser():
#         browser = config.get('basic information', 'browser')
#         return browser
#
#     @staticmethod
#     def getApplicationURL():
#         url=config.get('basic information', 'url')
#         return url
#
#     @staticmethod
#     def getUsername():
#         username = config.get('basic information', 'username')
#         return username
#
#     @staticmethod
#     def getPassword():
#         password = config.get('basic information', 'password')
#         return password
#

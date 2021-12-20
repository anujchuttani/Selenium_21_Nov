import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
            url=config.get('common info', 'baseurl')
            return url

    @staticmethod
    def getUsrEmail():
            username = config.get('common info', 'useremail')

            return username

    @staticmethod
    def getPassword():
            password = config.get('common info', 'password')

            return password

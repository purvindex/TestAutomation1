import softest

from Base.base_Driver import BaseDriver


class FileUploadPageUnitTest(BaseDriver):

    def __init__(self,
                 driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver

from Backend import database
from datetime import datetime
from Backend.models import Message  # Import the Message model

class Message_Builder:
    def __init__(self):
        self.__Text = None
        self.__From = None
        self.__To = None
        self.__TimeStamp = datetime.now() 
    
    def set_Text(self,Text):
        self.__Text = Text
        return self
    def set_From(self,From):
        self.__From = From
        return self
    def set_To(self,To):
        self.__To = To
        return self
    def set_Time(self,TimeStramp):
        self.__From = TimeStramp
    def build(self):
        return Message(self.__Text,self.__From,self.__To,self.__TimeStamp)
    
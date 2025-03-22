from Message import Message

class Message_Builder:
    def __init__(self):
        self.__Text = None
        self.__From = None
        self.__To = None
        self.__Time = None
    
    def set_Text(self,Text):
        self.__Text = Text
        return self
    def set_From(self,From):
        self.__From = From
        return self
    def set_To(self,To):
        self.__To = To
        return self
    def set_Time(self,Time):
        self.__From = Time
    def build(self):
        return Message(self.__Text,self.__From,self.__To,self.__Time)
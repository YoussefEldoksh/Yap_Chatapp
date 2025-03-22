class Message:
    def __init__(self,Text,From,To,Time): 
        self.__Text = Text
        self.__From = From
        self.__To = To
        self.__Time = Time

    def get_Text(self):
        return self.__Text
    def get_From(self):
        return self.__From
    def get_To(self):
        return self.__To
    def get_Time(self):
        return self.__Time
    

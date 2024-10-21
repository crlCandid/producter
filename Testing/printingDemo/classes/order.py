class Order:

    type:int
    name:str
    number:str

    def __init__(self,type:int,name:str,number:str):
        self.type = type
        self.name = name
        self.number = number
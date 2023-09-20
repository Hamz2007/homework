class User: 
    def __init__(self,name,health,speed):
        self.name= name 
        self.health= health
        self.speed= speed
    
    def print_info(self,one_line):
        if one_line: print(f"name:{self.name}health:{self.health}speed:{self.speed}")
        else: print(f"name:{self.name}\nhealth: {self.health}\nspeed:{self.speed}")                   
                    
user1 = User(name="rtv",health=250,speed=300)
user1.print_info(False)                     

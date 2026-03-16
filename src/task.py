import random

class task:

    def __init__(self, name:str, kind:str):
        self.kind = kind 
        self.name = name
        self.kind = () 
        
        "easy", "medium","more difficult","hard"

        self.xp = random.randint(0,15) * kind

    def complete(self):
        return self.xp
    

if __name__ == "__main__":
    t = task()
      

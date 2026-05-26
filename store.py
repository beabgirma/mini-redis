# Brain of the mini database
import json
from pathlib import Path

class MiniRedisStore:
    def __init__(self, filename="data.json"):
        self.filename= Path(filename)
        self.store=self.load()
  
    def load(self):
        if self.filename.exists():
            with open(self.filename, "r") as file:
                return json.load(file)
        return  {} 

    def save(self):
        with open(self.filename, "w")as file:
            json.dump(self.store,file)

    def set(self, key, value):
        self.store[key]=value
        self.save()
        return "OK"
    
    def get(self, key):
        return self.store.get(key, "(nil)")
    
    def delete(self,key):
        if key in self.store:
            del self.store[key]
            self.save()
            return "OK"
        return "(nil)"
    
    def exists(self, key):
        return "1" if key in self.store else "0"
    
    

class MySet:
    def __init__(self,enumarable = []):
        self.dictionary = {}
        for value in enumarable:
            self.dictionary[value] = True
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self 

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self  


  
  
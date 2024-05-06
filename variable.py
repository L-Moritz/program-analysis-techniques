class Variable:
    name: str;
    def __init__(self, name: str):
        self.name = name;
        
    def __str__(self):
        return self.name;
    
    def __eq__(self, value: object) -> bool:
        return self.name == value.name;

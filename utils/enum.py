from enum import Enum

class SmartEnum(Enum):
    def __call__(self, *args, **kwargs):
        return self.value

    def __eq__(self, value):
        return self.value == value
    
    def __str__(self):
        return self.name
    
    def __add__(self, other):
        if isinstance(other, int):
            num_elements = len(self.__class__)
            next_value = (self.value + other) % num_elements
            return [*self.__class__][next_value]
        return NotImplemented
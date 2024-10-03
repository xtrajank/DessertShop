from abc import ABC

class Combinable(ABC):
    def can_combine(self, other: 'Combinable') -> bool:
        pass
    
    def combine(self, other: 'Combinable') -> 'Combinable':
        pass
    

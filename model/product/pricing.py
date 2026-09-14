from abc import ABC, abstractmethod
 
class PricingPolicy(ABC):
    @abstractmethod
    def factor(self) -> float: ...

class Normal(PricingPolicy):
    def factor(self):
        return 1.0

class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        self._factor = 1.0 * percentage
    
    def factor(self):
        return self._factor
from abc import ABC, abstractmethod

from IPython.lib.pretty import Printable


class PricingPolicy(ABC): #ABC FORÇA FILHAS A COPIAREM OS PARAMETROS DA MÃE
    @abstractmethod
    def factor(self) -> float: ... #mesma coisa que pass só que é um valor e n um statement

class Normal(PricingPolicy):
    def factor(self):
        return 1.0

class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        self._factor = 1.0 * percentage
    
    def factor(self):
        return self._factor
#Classe PricingPolicy é um CONTRATO/INTERFACE -> Significa que ela seta as condições das suas classes filhas

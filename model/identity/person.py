from dataclasses import dataclass
from abc import ABC

# Value Objects
@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zip_code: str
    
    def __str__(self):
        return f"{self.street}, {self.city} - {self.zip_code}"

@dataclass(frozen=True)
class Contact:
    email: str
    phone: str
    
    def __str__(self):
        return f"{self.email} / {self.phone}"

# ABCDEFG... python é estranho mesmo
class Person(ABC):
    def __init__(self, name: str, address: Address, contact: Contact):
        self._name = name
        self._address = address
        self._contact = contact

    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    @property
    def contact(self):
        return self._contact
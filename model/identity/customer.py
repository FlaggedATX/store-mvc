from .person import * 

class Customer(Person):
    def __init__(self, customer_id: str, name: str, address: Address, contact: Contact):
        super().__init__(name, address, contact) # Usa a inicializacao do pai (Person)
        self._customer_id = customer_id
        self._loyalty_points = 0

    @property
    def customer_id(self):
        return self._customer_id

    # Vou apresentar essa ideia pro Rodrigo amanhã
    def add_points(self, n: int) -> None:
        self._loyalty_points += n
    
    def __repr__(self):
        # o que será que esse !r faz aqui?
        return (f"Customer(id={self._customer_id!r}, "
                f"name={self._name!r}, "
                f"address={self._address!r}, "
                f"contact={self._contact!r})")

    def __str__(self):
        return (f"[{self._customer_id}] {self._name}\n"
                f"  {self._address}\n"
                f"  {self._contact}")
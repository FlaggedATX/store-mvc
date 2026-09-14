# Note a clareza nos imports! 

# Traga a view do consumidor do domínio de identidades
# Você também pode criar um init em view/identity para importar a classe de view.identity
from view.identity.customer_view import CustomerView 
# Traga o modelo do consumidor, endereço e contato do domínio de identidades
from model.identity import Customer, Address, Contact


class CustomerController:
    def __init__(self, view: CustomerView):
        self._customers: list[Customer] = []
        self._view = view

    def register(self) -> Customer:
        data = self._view.prompt_data()
        address = Address(data["street"], data["city"], data["zip_code"])
        contact = Contact(data["email"], data["phone"])
        customer = Customer(
            customer_id = data["email"],
            name = data["name"],
            address = address,
            contact = contact,
        )
        self._customers.append(customer)
        self._view.show(customer)
        return customer

    def find(self, customer_id: str) -> Customer | None:
        for c in self._customers:
            if c.customer_id == customer_id:
                self._view.show(c)
                return c
        return None

    def list_all(self) -> None:
        self._view.show_list(self._customers)
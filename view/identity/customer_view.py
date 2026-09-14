from model.identity.customer import Customer

class CustomerView:
    def show(self, customer: Customer) -> None:
        print(customer)

    def show_list(self, customers: list[Customer]) -> None:
        for customer in customers:
            print(customer)

    def prompt_data(self) -> dict:
        return {
            "name": input("Name: "),
            "email": input("Email: "),
            "phone": input("Phone: "),
            "street": input("Street: "),
            "city": input("City: "),
            "zip_code": input("ZIP: "),
        }

from model.payment import *
from view.payment.payment_view import PaymentView

class PaymentController:
    def __init__(self, view: PaymentView):
        self._payment: Payment | None = None
        self._view = view

    def set_method(self, payment: Payment) -> None:
        self._payment = payment

    def prompt_method(self, amount: float) -> None:
        self._view.show_total(amount)
        self._view.show_methods()
        choice = self._view.prompt_method()
        if choice == "1":
            tendered = float(input("  Cash tendered: R$ "))
            self.set_method(Cash(tendered))
        elif choice == "2":
            last4 = input("  Card last 4 digits: ")
            self.set_method(Card(last4))
        elif choice == "3":
            key = input("  Pix key: ")
            self.set_method(Pix(key))

    def process(self, order: "Order") -> Receipt:
        if not self._payment:
            raise ValueError("No payment method set")
        receipt = self._payment.process(order)
        self._view.show_receipt(receipt)
        return receipt
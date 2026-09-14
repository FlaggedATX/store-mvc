from model.payment import Receipt

class PaymentView:
    def show_methods(self) -> None:
        print("Payment methods: [1] Cash  [2] Card  [3] Pix")

    def show_receipt(self, receipt: Receipt) -> None:
        print(receipt)

    def show_total(self, amount: float) -> None:
        print(f"  Total due: R$ {amount:.2f}")

    def prompt_method(self) -> str:
        return input("Choose method (1/2/3): ").strip()
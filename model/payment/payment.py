from abc import ABC, abstractmethod
from model.checkout import Order
import datetime
from .receipt import Receipt

class Payment(ABC):
    @abstractmethod
    def process(self, order: "Order") -> Receipt: ...

    def _make_receipt(self, order: "Order", method: str) -> Receipt:
        return Receipt(
            order_id = order.order_id,
            amount = order.total(),
            method = method,
            timestamp = datetime.now().strftime("dd-mm-yyyy %H:%M:%S"),
        )

class Cash(Payment):
    def __init__(self, tendered: float):
        self._tendered = tendered

    def process(self, order: "Order") -> None:
        # TODO: faço depois do cafézinho
        pass

class Card(Payment):
    def __init__(self, last4: str):
        self._last4 = last4

    def process(self, order: "Order") -> None:
        # TODO: faço depois do cafézinho
        pass

class Pix(Payment):
    def __init__(self, key: str):
        self._key = key

    # Made with Claude
    def process(self, order: "Order") -> Receipt:
        receipt = self._make_receipt(order, f"Pix: {self._key}")
        order.advance_status()
        return receipt
from dataclasses import dataclass

@dataclass(frozen=True)
class Receipt:
    order_id: str
    amount: float
    method: str
    timestamp: str

    def __str__(self):
        return (f"-- Receipt ------------------\n"
                f"  Order: #{self.order_id}\n"
                f"  Amount: R$ {self.amount:.2f}\n"
                f"  Method: {self.method}\n"
                f"  Time: {self.timestamp}\n"
                f"-----------------------------")

    def __repr__(self):
        return (f"Receipt(order_id={self.order_id!r}, "
                f"amount={self.amount:.2f}, method={self.method!r})")

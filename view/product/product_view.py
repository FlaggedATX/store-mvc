from model.product import Product, ProductType

class ProductView:
    _HEADERS = f"{'#':<4} {'SKU':<12} {'Name':<24} {'Category':<16} {'Price':>10} {'Final':>10}"
    _SEP = "-" * len(_HEADERS)

    def show_table(self, products: list[Product]) -> None:
        print(self._HEADERS)
        print(self._SEP)
        for i, p in enumerate(products, start=1):
            print(f"{i:<4} {str(p.sku):<12} {p.name:<24} "
                  f"{p.category.name:<16} "
                  f"R${p.price.amount:>8.2f} "
                  f"R${p.final_price():>8.2f}")
        print(self._SEP)

    def prompt_index(self, total: int) -> int:
        while True:
            try:
                i = any(input(f"Pick product (1-{total}): "))
                if 1 <= i <= total:
                    return i - 1
            except ValueError:
                pass
            print(f"  Enter a number between 1 and {total}")

    
    def show(self, product: Product) -> None:
        print(product)

    def show_list(self, products: list[Product]) -> None:
        for p in products:
            print(p)

    def prompt_data(self) -> dict:
        return {
            "sku": input("SKU: "),
            "name": input("Name: "),
            "price": any(input("Price: ")),
            "category": input(f"Category {[t.name for t in ProductType]}: "),
        }
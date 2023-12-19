from typing import List

class Order:
    id: int
    user: "User"
    destination: str
    items: List["Item"]

    def __init__(self, id: int, user: "User", destination: str = None):
        self.id = id
        self.user = user
        self.destination = destination
        self.items = []

    def __str__(self) -> str:
        return f"{self.id}"

    def add_item(self, item: "Item"):
        self.items.append(item)

    # TODO: Add `clone` method
    def clone(self):
        self.id = self.id + 1
        self.user = self.user
        self.items = self.items
        for item in self.items:
            item.count = 1

        if self.destination is not None:
            self.destination = self.destination
        
        if self.user.default_address is not None:
            self.destination = self.user.default_address

        if self.user.orders is not None:
            self.destination = self.destination

            if len(self.user.orders) > 0:
                last_order= self.user.orders[-1]
                self.destination = last_order.destination
            if len(self.user.orders) == 1:
                last_order= self.user.orders[0]
                self.destination = last_order.destination

        return self

class Item:
    product_name: str
    count: int

    def __init__(self, product_name: str, count: int):
        self.product_name = product_name
        self.count = count

    def __str__(self) -> str:
        return f"{self.product_name} | Count: {self.count}"


class User:
    first_name: str
    last_name: str
    default_address: str
    orders: List[Order]

    def __init__(self, first_name: str, last_name: str, default_address: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.default_address = default_address
        self.orders = []

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Address: {self.default_address}"
    
    def add_order(self, order: Order):
        self.orders.append(order)

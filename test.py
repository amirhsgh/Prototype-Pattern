from models import Order, User, Item

user = User("amirhs", "Qavi")
item = Item("water", 2)
item2 = Item("cake", 3)


order = Order(1, user, "mashhad1")
order2 = Order(2, user, "mashhad2")

order.add_item(item)
order.add_item(item2)

order_clone = order2.clone()


print(order_clone.destination)
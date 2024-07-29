from playsound import playsound

class Order:
    def __init__(self, order_id, details):
        self.order_id = order_id
        self.details = details
        self.status = "Received"  # Possible statuses: Received, Preparing, Completed

class OrderSystem:
    def __init__(self):
        self.orders = []
        self.order_id_counter = 1

    def add_order(self, details):
        order = Order(self.order_id_counter, details)
        self.orders.append(order)
        self.order_id_counter += 1
        return order

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                if new_status == "Completed":
                    playsound('notification.mp3')  # Notification sound
                return order
        return None

    def get_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

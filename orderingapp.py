import tkinter as tk
from tkinter import messagebox
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

class OrderApp:
    def __init__(self, root, order_system):
        self.order_system = order_system
        self.root = root
        self.root.title("Order Tracking System")

        # Order details input
        self.order_details_label = tk.Label(root, text="Order Details:")
        self.order_details_label.pack()
        self.order_details_entry = tk.Entry(root)
        self.order_details_entry.pack()

        self.add_order_button = tk.Button(root, text="Add Order", command=self.add_order)
        self.add_order_button.pack()

        # Order status update
        self.order_id_label = tk.Label(root, text="Order ID:")
        self.order_id_label.pack()
        self.order_id_entry = tk.Entry(root)
        self.order_id_entry.pack()

        self.status_label = tk.Label(root, text="New Status:")
        self.status_label.pack()
        self.status_options = ["Received", "Preparing", "Completed"]
        self.status_var = tk.StringVar(root)
        self.status_var.set(self.status_options[0])
        self.status_menu = tk.OptionMenu(root, self.status_var, *self.status_options)
        self.status_menu.pack()

        self.update_status_button = tk.Button(root, text="Update Status", command=self.update_status)
        self.update_status_button.pack()

        # Display orders
        self.orders_list_label = tk.Label(root, text="Orders:")
        self.orders_list_label.pack()
        self.orders_listbox = tk.Listbox(root, width=50)
        self.orders_listbox.pack()

    def add_order(self):
        details = self.order_details_entry.get()
        if details:
            order = self.order_system.add_order(details)
            self.orders_listbox.insert(tk.END, f"Order ID: {order.order_id}, Details: {order.details}, Status: {order.status}")
            self.order_details_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Order {order.order_id} added successfully!")

    def update_status(self):
        try:
            order_id = int(self.order_id_entry.get())
            new_status = self.status_var.get()
            order = self.order_system.update_order_status(order_id, new_status)
            if order:
                self.refresh_orders_listbox()
                messagebox.showinfo("Success", f"Order {order.order_id} status updated to {new_status}!")
            else:
                messagebox.showerror("Error", f"Order ID {order_id} not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid Order ID.")

    def refresh_orders_listbox(self):
        self.orders_listbox.delete(0, tk.END)
        for order in self.order_system.orders:
            self.orders_listbox.insert(tk.END, f"Order ID: {order.order_id}, Details: {order.details}, Status: {order.status}")

if __name__ == "__main__":
    root = tk.Tk()
    order_system = OrderSystem()
    app = OrderApp(root, order_system)
    root.mainloop()

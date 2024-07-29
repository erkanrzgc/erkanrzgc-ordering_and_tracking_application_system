if __name__ == "__main__":
    root = tk.Tk()
    order_system = OrderSystem()
    app = OrderApp(root, order_system)
    root.mainloop()

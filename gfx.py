import tkinter as tk

class Graphics:
    def __init__(self, db):
        self.item_count = 0
        self.wnd = tk.Tk()
        self.wnd.title("Inventory management")
        self.main_menu = tk.Menu(self.wnd)
        
        self.query_frame = tk.Frame(self.wnd)
        self.query_frame.grid()
        self.search_field = tk.Entry(self.query_frame, text="Item")
        self.search_field.grid(row=1, column=1)
        self.item_count_field = tk.Entry(self.query_frame, textvariable=self.item_count)
        self.item_count_field.grid(row=1, column=2)
        self.search_field.grid(row=1, column=1)
        self.search_button = tk.Button(self.query_frame, text="Search")
        self.search_button.grid(row=2, column=1)
        self.add_button = tk.Button(self.query_frame, text="Add", command=self.add_item_win)
        self.add_button.grid(row=2, column=2)

        self.wnd.mainloop()

    def add_item_win(self):
        self.item_win = tk.Tk()
        self.item_name = tk.Entry(self.item_win)
        self.item_number = tk.Entry(self.item_win)
        self.item_category = tk.Entry(self.item_win)
        self.item_quantity = tk.Entry(self.item_win)
        self.add_buttton = tk.Button(self.item_win)

        self.item_name.grid()
        self.item_name.grid()
        self.item_name.grid()
        self.item_name.grid()

    def update_table(self):
        pass

    def clear_table(self):
        pass

    def send_query(self, gfx):
        pass
    
    def error_handle(self):
        print("Error occured")
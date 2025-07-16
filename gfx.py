import tkinter as tk

class Graphics:
    def __init__(self, db):
        self.item_count = db.get_item()
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
        self.add_button = tk.Button(self.query_frame, text="Add")
        self.add_button.grid(row=2, column=2)

        self.wnd.mainloop()
    
    def update_table(self):
        pass

    def clear_table(self):
        pass

    def send_query(self, gfx):
        pass

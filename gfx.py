import tkinter as tk
import database
class Graphics:
    def __init__(self, db):
        self.item_count = 0
        self.wnd = tk.Tk()
        self.wnd.title("Inventory management")
        self.main_menu = tk.Menu(self.wnd)
        
        self.query_frame = tk.Frame(self.wnd)
        self.query_frame.grid()
        self.search_field = tk.Entry(self.query_frame, text="Item")
        self.search_field.grid(row=1, column=2)
        self.item_count_field = tk.Entry(self.query_frame, textvariable=self.item_count)
        self.item_count_field.grid(row=1, column=2)
        self.search_field.grid(row=1, column=2)
        self.search_button = tk.Button(self.query_frame, text="Search...", command=self.search_btn_cmd)
        self.search_button.grid(row=2, column=2)
        self.add_button = tk.Button(self.query_frame, text="Add...", command=self.add_item_btn_cmd)
        self.add_button.grid(row=2, column=2)
        self.db = database.Database(r"C:\Users\krist\Desktop\Programming Ideas\Inventory management\db\inventory.cvs")

        self.wnd.mainloop()

    def add_item_btn_cmd(self):
        self.item_name_entry = tk.StringVar()
        self.item_number_entry = tk.StringVar()
        self.item_category_entry = tk.StringVar()
        self.item_quantity_entry = tk.StringVar()
        self.item_location_entry = tk.StringVar()

        self.item_win = tk.Toplevel()
        self.item_name = tk.Entry(self.item_win, textvariable=self.item_name_entry)
        self.item_number = tk.Entry(self.item_win, textvariable=self.item_number_entry)
        self.item_category = tk.Entry(self.item_win, textvariable=self.item_category_entry)
        self.item_quantity = tk.Entry(self.item_win, textvariable=self.item_quantity_entry)
        self.item_location = tk.Entry(self.item_win, textvariable=self.item_location_entry)
            
        self.item_name_descriptor = tk.Label(self.item_win,text="Name: ")
        self.item_number_descriptor = tk.Label(self.item_win, text="Item#")
        self.item_category_descriptor = tk.Label(self.item_win, text="Cat: ")
        self.item_quantity_descriptor = tk.Label(self.item_win, text="Qty: ")
        self.item_location_descriptor = tk.Label(self.item_win, text="Loc:")
        self.add_button = tk.Button(self.item_win, text="Add item", command=lambda: self.db.add_item(self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get()))

        self.item_name.grid(column=2, row=1)
        self.item_number.grid(column=2, row=2)
        self.item_category.grid(column=2, row=3)
        self.item_quantity.grid(column=2, row=4)
        self.item_location.grid(column=2, row=5)
        self.add_button.grid(column=2, row=6)

        self.item_name_descriptor.grid(column=1, row=1)
        self.item_number_descriptor.grid(column=1, row=2)
        self.item_category_descriptor.grid(column=1, row=3)
        self.item_quantity_descriptor.grid(column=1, row=4)
        self.item_location_descriptor.grid(column=1, row=5)

    
    def search_btn_cmd(self):
        self.item_list = []

        self.item_name_entry = tk.StringVar()
        self.item_number_entry = tk.StringVar()
        self.item_category_entry = tk.StringVar()
        self.item_quantity_entry = tk.StringVar()
        self.item_location_entry = tk.StringVar()

        self.item_win = tk.Toplevel()
        self.item_name = tk.Entry(self.item_win, textvariable=self.item_name_entry)
        self.item_number = tk.Entry(self.item_win, textvariable=self.item_number_entry)
        self.item_category = tk.Entry(self.item_win, textvariable=self.item_category_entry)
        self.item_quantity = tk.Entry(self.item_win, textvariable=self.item_quantity_entry)
        self.item_location = tk.Entry(self.item_win, textvariable=self.item_location_entry)


        self.item_name_descriptor = tk.Label(self.item_win,text="Name: ")
        self.item_number_descriptor = tk.Label(self.item_win, text="Item#")
        self.item_category_descriptor = tk.Label(self.item_win, text="Cat: ")
        self.item_quantity_descriptor = tk.Label(self.item_win, text="Qty: ")
        self.item_location_descriptor = tk.Label(self.item_win, text="Loc:")
        self.search_button = tk.Button(self.item_win, command=lambda: self.db.search_query(self.item_list, self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get()))
        self.next_button = tk.Button(self.item_win, command=None, text=">")
        self.prev_button = tk.Button(self.item_win, command=None, text="<")

        self.item_name.grid(column=2, row=1)
        self.item_number.grid(column=2, row=2)
        self.item_category.grid(column=2, row=3)
        self.item_quantity.grid(column=2, row=4)
        self.item_location.grid(column=2, row=5)
        self.search_button.grid(column=2, row=6)

        self.item_name_descriptor.grid(column=1, row=1)
        self.item_number_descriptor.grid(column=1, row=2)
        self.item_category_descriptor.grid(column=1, row=3)
        self.item_quantity_descriptor.grid(column=1, row=4)
        self.item_location_descriptor.grid(column=1, row=5)

        

    def update_table(self):
        pass
    
    def clear_table(self):
        pass

    def send_query(self, gfx):
        pass
    
    def error_handle(self):
        print("Error occured")
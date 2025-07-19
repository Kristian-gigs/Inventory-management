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
        self.search_field = tk.Label(self.query_frame, text="Welcome to the inventory manager.\n choose below whether to add a new item, or search the system for an existing item.")
        self.search_field.grid(row=1, column=1, columnspan=2)
        self.search_button = tk.Button(self.query_frame, text="Search...", command=self.search_btn_cmd)
        self.search_button.grid(row=2, column=1)
        self.add_button = tk.Button(self.query_frame, text="Add...", command=self.add_item_btn_cmd)
        self.add_button.grid(row=2, column=2)
        self.credits_button = tk.Button(self.query_frame, command=self.credits, text="Credits")
        self.credits_button.grid(row=3, column=1, columnspan=2, pady=30)
        self.db = database.Database(r"C:\Users\krist\Desktop\Programming Ideas\Inventory management\db\inventory.cvs")

        self.wnd.mainloop()

    def add_item_btn_cmd(self):
        self.item_name_entry = tk.StringVar()
        self.item_number_entry = tk.StringVar()
        self.item_category_entry = tk.StringVar()
        self.item_quantity_entry = tk.StringVar()
        self.item_location_entry = tk.StringVar()

        self.wnd.bind('<Return>', lambda: self.db.add_item(self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get()))

        def clear():
            self.item_name_entry.set("") 
            self.item_number_entry.set("")
            self.item_category_entry.set("")
            self.item_quantity_entry.set("")
            self.item_location_entry.set("")
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
        self.clear_button = tk.Button(self.item_win, text="Clear", command=clear)

        self.item_name.grid(column=2, row=1)
        self.item_number.grid(column=2, row=2)
        self.item_category.grid(column=2, row=3)
        self.item_quantity.grid(column=2, row=4)
        self.item_location.grid(column=2, row=5)
        self.add_button.grid(column=2, row=6)
        self.clear_button.grid(column=1, row=6)

        self.item_name_descriptor.grid(column=1, row=1)
        self.item_number_descriptor.grid(column=1, row=2)
        self.item_category_descriptor.grid(column=1, row=3)
        self.item_quantity_descriptor.grid(column=1, row=4)
        self.item_location_descriptor.grid(column=1, row=5)

    
    def search_btn_cmd(self):
        self.wnd.bind('<Return>', search)
        self.item_list = []

        self.item_name_entry = tk.StringVar()
        self.item_number_entry = tk.StringVar()
        self.item_category_entry = tk.StringVar()
        self.item_quantity_entry = tk.StringVar()
        self.item_location_entry = tk.StringVar()

        def clear():
            self.item_name_entry.set("") 
            self.item_number_entry.set("")
            self.item_category_entry.set("")
            self.item_quantity_entry.set("")
            self.item_location_entry.set("")

        self.item_win = tk.Toplevel()
        self.item_name = tk.Entry(self.item_win, textvariable=self.item_name_entry)
        self.item_number = tk.Entry(self.item_win, textvariable=self.item_number_entry)
        self.item_category = tk.Entry(self.item_win, textvariable=self.item_category_entry)
        self.item_quantity = tk.Entry(self.item_win, textvariable=self.item_quantity_entry)
        self.item_location = tk.Entry(self.item_win, textvariable=self.item_location_entry)

        def search():
            results = self.db.search_query( self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get())
            results_win = tk.Toplevel(self.item_win)
            results_win.geometry("400x200")
            results_win.title("Query results")
            results_display = tk.Label(results_win, text=str(results))
            results_display.grid()
            print(results)

        self.item_name_descriptor = tk.Label(self.item_win,text="Name: ")
        self.item_number_descriptor = tk.Label(self.item_win, text="Item#")
        self.item_category_descriptor = tk.Label(self.item_win, text="Cat: ")
        self.item_quantity_descriptor = tk.Label(self.item_win, text="Qty: ")
        self.item_location_descriptor = tk.Label(self.item_win, text="Loc:")
        self.button_bar = tk.Frame(self.item_win)
        self.search_button = tk.Button(self.button_bar, text="Search", command=search)
        self.next_button = tk.Button(self.button_bar, command=None, text=">")
        self.prev_button = tk.Button(self.button_bar, command=None, text="<")
        self.clear_button = tk.Button(self.button_bar, text="Clear", command=clear)

        self.item_name.grid(column=2, row=1)
        self.item_number.grid(column=2, row=2)
        self.item_category.grid(column=2, row=3)
        self.item_quantity.grid(column=2, row=4)
        self.item_location.grid(column=2, row=5)
        self.button_bar.grid(row=6, column=1, columnspan=3)
        self.search_button.pack(side="left")
        self.prev_button.pack(side="left")
        self.next_button.pack(side="left")
        self.clear_button.pack(side="left")

        self.item_name_descriptor.grid(column=1, row=1)
        self.item_number_descriptor.grid(column=1, row=2)
        self.item_category_descriptor.grid(column=1, row=3)
        self.item_quantity_descriptor.grid(column=1, row=4)
        self.item_location_descriptor.grid(column=1, row=5)
        
    def credits(self):
        credits_wnd = tk.Toplevel(self.wnd)
        credits_wnd.geometry("500x100")
        credits_wnd.title("Credits")
        credit_text = tk.Label(credits_wnd, text="This inventory management system was created by Kristian Gunnleiv i Gardastovu Sørensen\nIt aims to help one keep track of their inventory using a simple GUI,\n and was all in all just a fun little project\n\n Github: @Kristian-gigs\n Check out other things I have made!")
        credit_text.pack()

    def update_table(self):
        pass
    
    def clear_table(self):
        pass

    def send_query(self, gfx):
        pass
    
    def error_handle(self):
        print("Error occured")
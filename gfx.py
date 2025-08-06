import tkinter as tk
from tkinter import ttk
import database
class Graphics:
    def __init__(self, db):
        self.wnd = tk.Tk()
        self.wnd.title("Inventory management")
       
        
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


        def clear():
            self.item_name_entry.set("") 
            self.item_number_entry.set("")
            self.item_category_entry.set("")
            self.item_quantity_entry.set("")
            self.item_location_entry.set("")
        self.item_win = tk.Toplevel()
        self.item_win.bind('<Return>', lambda event: self.db.add_item(self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get()))
        self.item_win.bind("<Escape>", lambda event: self.item_win.destroy())
        
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

    def edit_selected(self, row: ttk.Treeview):

        if not row:
            print("No row selected!")
            return 0
        self.edit_win = tk.Toplevel(self.wnd)
        self.edit_win.title("Edit values")

        row_data = self.tree.item(row[0])["values"]
        self.item_name_entry = tk.StringVar()
        self.item_number_entry = tk.StringVar()
        self.item_category_entry = tk.StringVar()
        self.item_quantity_entry = tk.StringVar()
        self.item_location_entry = tk.StringVar()

        if str(row_data[0]).lower() != "nan":
            self.item_name_entry.set(row_data[0])
        if str(row_data[1]).lower() != "nan":
            self.item_number_entry.set(row_data[1])
        if str(row_data[2]).lower() != "nan":
            self.item_category_entry.set(row_data[2])
        if str(row_data[3]).lower() != "nan":
            self.item_quantity_entry.set(row_data[3])
        if str(row_data[4]).lower() != "nan":
            self.item_location_entry.set(row_data[4])

        self.edit_win.bind('<Return>', lambda event: self.db.edit_item(self.edit_win.destroy, database.pd.DataFrame([row_data], columns=["item_name","item_no","category","quantity","location"]), (self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get())))

        self.item_name = tk.Entry(self.edit_win, textvariable=self.item_name_entry)
        self.item_number = tk.Entry(self.edit_win, textvariable=self.item_number_entry)
        self.item_category = tk.Entry(self.edit_win, textvariable=self.item_category_entry)
        self.item_quantity = tk.Entry(self.edit_win, textvariable=self.item_quantity_entry)
        self.item_location = tk.Entry(self.edit_win, textvariable=self.item_location_entry)
            
        self.item_name_descriptor = tk.Label(self.edit_win,text="Name: ")
        self.item_number_descriptor = tk.Label(self.edit_win, text="Item#")
        self.item_category_descriptor = tk.Label(self.edit_win, text="Cat: ")
        self.item_quantity_descriptor = tk.Label(self.edit_win, text="Qty: ")
        self.item_location_descriptor = tk.Label(self.edit_win, text="Loc:")
        self.apply_button = tk.Button(self.edit_win, text="Apply", command=lambda: self.db.edit_item(self.edit_win.destroy, row_data, (self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), int(self.item_quantity_entry.get()), self.item_location_entry.get())))
        self.item_name.grid(column=2, row=1)
        self.item_number.grid(column=2, row=2)
        self.item_category.grid(column=2, row=3)
        self.item_quantity.grid(column=2, row=4)
        self.item_location.grid(column=2, row=5)
        self.apply_button.grid(column=2, row=6)

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

        def search(event=None):
            results = self.db.search_query( self.item_name_entry.get(), self.item_number_entry.get(), self.item_category_entry.get(), self.item_quantity_entry.get(), self.item_location_entry.get())
            results_win = tk.Toplevel(self.item_win)
            results_win.bind("<Escape>", lambda event: results_win.destroy())
            results_win.title("Query results")

             # Destroy old tree if exists
            if hasattr(self, "tree"):
                self.tree.destroy()

            self.tree = ttk.Treeview(results_win)
            self.tree["columns"] = list(results.columns)
            self.tree["show"] = "headings"

            # Set headings
            for col in results.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)

            # Insert rows
            for _, row in results.iterrows():
                self.tree.insert("", "end", values=list(row))

            self.tree.grid(row=4, column=0, columnspan=5, pady=10)
            # Add edit button
            self.edit_btn = tk.Button(results_win, text="Edit Selected", command=lambda: self.edit_selected(self.tree.selection()))
            self.edit_btn.grid(row=5, column=0, pady=5)

            print(results)
        self.item_win.bind('<Return>', search)

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
        credits_wnd.bind("<Escape>", lambda event: credits_wnd.destroy())
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
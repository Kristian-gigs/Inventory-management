import database
import gfx
import pandas as pd

def temp_error_handle():
    print("Error occured")

db = database.Database(r"C:\Users\krist\Desktop\Programming Ideas\Inventory management\db\inventory.cvs")
wnd = gfx.Graphics(db)
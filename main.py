import database
import gfx

def temp_error_handle():
    print("Error occured")

db = database.Database(r"C:\Users\krist\Desktop\Programming Ideas\Inventory management\db\inventory.cvs", temp_error_handle)
wnd = gfx.Graphics(db)
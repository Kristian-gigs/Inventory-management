import database
import gfx

def temp_error_handle():
    print("Error occured")

db = database.Database("db/inventory.csv", temp_error_handle)
wnd = gfx.Graphics(db)

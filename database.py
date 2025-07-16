import csv

#select db file
class Database:
    def __init__(self, db_source, gfx_error_handle):
        self.item = ("", 0)
        try:
            self.inv = open(db_source, newline=" ")
        except:
            gfx_error_handle()
    
    def add_item(self, item_name, count):
        open_db = csv.writer(self.inv)
        open_db.writerow(item_name, count)
    
    def get_item(self, item_name):
        return item_name

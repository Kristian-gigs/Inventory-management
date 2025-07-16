import csv

#select db file
class Database:
    def __init__(self, db_source, gfx_error_handle):
        self.item_dict = dict()
        self.db_source = db_source
        
    
    def add_item(self, item_name, count):
        open_db = csv.writer(self.inv)
        open_db.writerow(item_name, count)
    
    def search_query(self, item_name):
        raw_data = csv.DictReader(self.inv, dialect="excel")
    
    def edit_item(self):
        pass

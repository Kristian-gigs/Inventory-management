import pandas as pd

#select db file
class Database:
    def __init__(self, db_source):
        self.item_dict = dict()
        self.db_source = db_source
        
    
    def add_item(self, item_name, item_no, count, cat, location):
        new_row = pd.DataFrame([[item_name, item_no, cat, count, location]])
        new_row.to_csv(self.db_source, mode='a', index=False, header=False)
    
    def search_query(self, item_name, item_no, count, cat, location):
        with open(self.db_source) as csv_file:
            data = pd.read_csv(csv_file)
            data.query("")
    
    def edit_item(self):
        pass

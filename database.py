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
            query = f""
            first = True

            if item_name != "":
                query += f"item_name == '{item_name}'"
                first = False
            
            if item_no != "":
                if not first:
                    query += " and "

                query += f"item_no == '{item_no}'"
                first = False
            
            if count != "":
                if not first:
                    query += " and "
                    
                query += f"quantity == '{count}'"
                first = False
            
            if cat != "":
                if not first:
                    query += " and "
                    
                query += f"category == '{cat}'"
                first = False
            
            if location != "":
                if not first:
                    query += " and "
                    
                query += f"location == '{location}'"
                first = False
            

            item_list = data.query(query)
            return item_list
    
    def edit_item(self):
        pass

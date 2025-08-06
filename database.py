import pandas as pd

#select db file
class Database:
    def __init__(self, db_source):
        self.item_dict = dict()
        self.db_source = db_source
        
    
    def add_item(self, item_name, item_no, cat, count, location):
        new_row = pd.DataFrame([[item_name, item_no, cat, count, location]])
        new_row.to_csv(self.db_source, mode='a', index=False, header=False)
    
    def search_query(self, item_name, item_no, cat, count, location):
        with open(self.db_source) as csv_file:
            data = pd.read_csv(csv_file, quotechar="'")
            query = f""
            first = True
            
            if item_name:
                data = data[data["item_name"].astype(str).str.contains(item_name, case=False, na=False)]
            if item_no:
                data = data[data["item_no"].astype(str).str.contains(item_no, case=False, na=False)]
            if cat:
                data = data[data["category"].astype(str).str.contains(cat, case=False, na=False)]
            if count:
                data = data[data["quantity"].astype(str).str.contains(count, case=False, na=False)]
            if location:
                data = data[data["location"].astype(str).str.contains(location, case=False, na=False)]

            return data
    
    def edit_item(self, old_data, new_data: list):
        
        data = pd.read_csv(self.db_source).fillna("").astype(str).map(str.strip)
        

        old_data = [str(x).strip() if str(x).lower() != "nan" else "" for x in old_data]

        # For debugging errors in replacing rows. Compares each row of the dataframe to the
        # selected data, and checks for matches. This tells you if there are any unintended matches,
        # and also if the intended row is selected at all.
        
                # print("\n\n", "Columns:", list(data.columns))
                # print("Old data:", old_data)
                # print("Length match:", len(data.columns) == len(old_data), "\n\n")
                # for i, row in data.iterrows():
                #     match = row.tolist() == old_data
                #     print(f"Row {i}: {row.tolist()} == {old_data} → {match}")

        row_mask = (data == old_data).all(axis=1)
        data.loc[row_mask] = new_data
        print(data, "\n\n\n")
        data.to_csv(self.db_source, index=False)

        print(old_data)
        print(new_data, "\n\n\n")
        print(data)
        return data

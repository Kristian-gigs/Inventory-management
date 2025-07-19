This is an inventory management system using a local csv file as a database. The items are stored by item name, item#, category and quantity.
Through the GUI you can view parts of the inventory based on queries for item name, item# or category, and new items can also be added
through the GUI, as well as properties of an listed item, such as quantity can be updated



TODO:

Add edit func and win
* df = pd.read_csv('C:/TestBook1.csv')
df = df[['Coordinate','Speed']]

df['Coordinate']+=756
df.to_csv('C:/TestBook1.csv')

OR

Location = r'C:\\'
df = pd.read_csv(Location,header=None)
df["Coorinate"].values +756

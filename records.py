import sqlite3
import pickle
import datetime

class Records:
    def __init__(self, database_filename, first_table_name, hash_salt, key) -> None:
        self.database_filename = database_filename
        self.first_table_name = first_table_name
        self.hash_salt = hash_salt
        self.key = key

        self.connection = sqlite3.Connection(self.database_filename)
        self.cursor = self.connection.cursor()

        self.add_table(self.first_table_name)
    
    def add_table(self, table_name):

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                    (date datetime, list BLOB, contents BLOB)''')

    def pack(self, contents_types:list, contents:list):

        date_and_time = datetime.datetime.now()
        content_types_bin = pickle.dumps(contents_types)
        contents_bin = pickle.dumps(contents)

        return (date_and_time, content_types_bin, contents_bin)
    
    def unpack(self, package):
        if isinstance(package, (tuple, list)):
            package_unpacked = []
            for object in package:
                object_unpacked = pickle.loads(object)
                package_unpacked.append(object_unpacked)

        else:
            package_unpacked = pickle.loads(package)
        
        return package_unpacked
    
    def add_record(self,contents_types:list, contents:list,  table_name:str=None):

        if table_name is None:
            table_name = self.first_table_name

        data_to_add = self.pack(contents_types, contents)
        self.cursor.execute( f'''INSERT INTO {table_name} VALUES (?, ?, ?) ''', data_to_add)
        self.connection.commit()
    




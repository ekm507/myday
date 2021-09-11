import sqlite3
import pickle
import datetime

class Records:
    def __init__(self, database_filename, first_table_name, fernet_object = None) -> None:
        self.database_filename = database_filename
        self.first_table_name = first_table_name
        self.fernet_object = fernet_object

        self.connection = sqlite3.Connection(self.database_filename)
        self.cursor = self.connection.cursor()

        self.add_table(self.first_table_name)
    
    def add_table(self, table_name):

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                    (date datetime, list BLOB, contents BLOB)''')

    def pack(self, contents_types:list, contents:list, fernet_object=None):

        date_and_time = datetime.datetime.now()
        contents_types_bin = pickle.dumps(contents_types)
        contents_bin = pickle.dumps(contents)

        if fernet_object is None:
            packed_data = (date_and_time, contents_types_bin, contents_bin)
        
        else:
            contents_types_bin_crypt = fernet_object.encrypt(contents_types_bin)
            contents_bin_crypt = fernet_object.encrypt(contents_bin)
            packed_data = (date_and_time, contents_types_bin_crypt, contents_bin_crypt)

        return packed_data
    
    def unpack(self, package, fernet_object=None):
        if isinstance(package, (tuple, list)):
            package_unpacked = []
            for object in package:

                if fernet_object is None:
                    object_unpacked = pickle.loads(object)
                else:
                    object_decrypted = fernet_object.decrypt(object)
                    object_unpacked = pickle.loads(object_decrypted)

                package_unpacked.append(object_unpacked)

        else:
            package_unpacked = pickle.loads(package)
        
        return package_unpacked
    
    def add_record(self,contents_types:list, contents:list,  table_name:str=None):

        if table_name is None:
            table_name = self.first_table_name
        
        packed_data = self.pack(contents_types, contents, fernet_object=self.fernet_object)
        data_to_add = packed_data

        self.cursor.execute( f'''INSERT INTO {table_name} VALUES (?, ?, ?) ''', data_to_add)
        self.connection.commit()
    
    def return_all_records(self, table_name:str=None):

        if table_name is None:
            table_name = self.first_table_name
        
        table_values = self.cursor.execute(f'''SELECT * FROM {table_name};''')
        unpacked_records = []
        for package in table_values:
            date_and_time = package[0]
            contents_types, contents = self.unpack(package[1:], fernet_object=self.fernet_object)

            unpacked_records.append((date_and_time, contents_types, contents))

        return unpacked_records

        

    def check_key(self, table_name:str=None):

        if table_name is None:
            table_name = self.first_table_name

        first_records = self.cursor.execute(f'SELECT * FROM {table_name} ORDER BY ROWID ASC LIMIT 1')
        for record in first_records:

                try:
                    self.unpack(record[1:], fernet_object=self.fernet_object)
                except:
                    print('wrong password!')
                    exit(2)
            


        

    




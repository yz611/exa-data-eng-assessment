
"""
    python program to read json file
"""

import os, json, glob, psycopg2
import pandas as pd

#defining classes
        
        
        
class TableMap(object):
    """table relational map
    """    
    def __init__ (self, table_map: dict, parent_path):
        self._table_map = table_map
        self.__set_attributes(table_map)
        self.__converter()
        self.__create_folder(parent_path)
    
    def __set_attributes(self, record_table: dict):
        for name, value in record_table.items():
            setattr(self, name, value)
        self._keys = record_table.keys()
      
    def get_table_by_key(self, key: str):
        """get another table related by key
        
        Returns:
            dict: entry table
        """        

        return self._table_map[key]       
    
    def __converter(self):
        """convert list of dicts to table objects
        """        
        self.dir = False
        for key in self._keys:
            value = self._table_map[key]
            if isinstance(value, list):
                setattr(self, key, Table(value))
                self.dir = True
            if isinstance(value, dict):
                setattr(self, key, TableMap(value))
                self.dir = True
                
    def __create_folder(self, parent_path):
        
        if self.dir:
            for folder_name in self._keys:
                path = os.path.join(parent_path, folder_name)
                self.curr_path = path
                os.mkdir(path)         
            
            

                
               
class JsonRec(TableMap):
    """class definition of json record objects 
        that use data from json files
    """    
    def __init__(self, json_path: str):
        self._json_path = json_path
        self.__load_json_data()#load data from json file to python dict
        TableMap.__init__(self, self._raw_data)
        
        
    def __load_json_data(self):
        """convert json data to python dictionaries
        """        
        with open(self._json_path ,'r') as f:
            data = json.loads(f.read())
        self._raw_data = data


            
class Table(object):
    """tabular object

    """    
    def __init__(self, dict_list: list, parent_path):
        self.__set_attributes(dict_list)
        self.__converter()
        self.__create_folder(parent_path)
    
    def __set_attributes(self, dict_list: 'list[dict]'):
        self._dict_list = dict_list
        
    def __converter(self):
        def __line_converter(row):
            if isinstance(row, dict):
                for key in row:
                    value = row[key]
                    if isinstance(value, dict):
                        self.dir = True
                        row[key] = TableMap(value)
                    if isinstance(value, list):
                        self.dir = True
                        row[key] = Table(value)
        self.dir = False
        for row in self._dict_list:
            __line_converter(row)

    def __create_folder(self, parent_path):
            
        if self.dir:
            for num in range(len(self._dict_list)):
                path = os.path.join(parent_path, 'record_' + str(num))
                self.curr_path = path
                os.mkdir(path)
            
            
    
    
    
    
    
#testing
if __name__ == '__main__':
    #locate the data folder
    rel_path = os.path.join('..', 'data')

    #grab files in folder
    __json_file_paths = glob.glob(os.path.join(rel_path, '*.json'))
    
    #testing
    pilot = JsonRec(__json_file_paths[0])
    
    print()
            
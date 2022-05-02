
"""
    python program to read json file
"""

import os, json, glob, psycopg2
import pandas as pd

#defining classes
        
        
        
class TableMap(object):
    """table relational map
    """    
    def __init__ (self, table_map: dict):
        self.table_map = table_map
        self.__set_attributes(table_map)
    
    def __set_attributes(self, record_table: dict):
        for name in record_table:
            var = '_' + name
            setattr(self, var, record_table[name])
        self.keys = record_table.keys()
            
    def get_another_table(self, key: str):
        """get another table related by key
        
        Returns:
            dict: entry table
        """        

        return self.table_map[key]       
        
        
                
        
class JsonRec(TableMap):
    """class definition of json record objects 
        that use data from json files
    """    
    def __init__(self, json_path: str):
        self._json_path = json_path
        self.__load_json_data()#load data from json file to python dict
        TableMap.__init__(self, self._data)
        
        
    def __load_json_data(self):
        """convert json data to python dictionaries
        """        
        with open(self._json_path ,'r') as f:
            data = json.loads(f.read())
        self._data = data

                
    


class Table(object):
    """tabular object

    """    
    def __init__(self, dict_list: list):
        self.__set_attributes(dict_list)
    
    def __set_attributes(self, dict_list: 'list[dict]'):
        self.table_contents = dict_list
        self.cols = dict_list[0].keys()
    
    
    
    
    
#testing
if __name__ == '__main__':
    #locate the data folder
    rel_path = os.path.join('..', 'data')

    #grab files in folder
    __json_file_paths = glob.glob(os.path.join(rel_path, '*.json'))
    
    #testing
    pilot = JsonRec(__json_file_paths[0]).get_another_table('entry')
    pilot_table = Table(pilot)
    
    pilot_dict = Table(pilot)
    
    print()
            
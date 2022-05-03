
"""
    python server program to read json file and create file system 
"""

import os, json, glob

#defining classes

class options:
    """struct like class

    Returns:
        _type_: _description_
    """    
    #locate the data folder
    def get_rel_path():
        return os.path.join('..', 'data')

    #grab files in folder
    def get_json_file_paths(rel_path):
        return glob.glob(os.path.join(rel_path, '*.json'))
    
    #grab file names in folder
    def get_json_file_names(rel_path):
        return list(map(lambda x: x.replace('.json', ''), os.listdir(rel_path)))
        
class TableMap(object):
    """table relational map
    """    
    def __init__ (self, table_map: dict, parent_path):
        self.parent_path = parent_path
        self._table_map = table_map
        self.__set_attributes(table_map)
        self.__create_dirs()
    
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
    
    def __create_dirs(self):
        """convert list of dicts to table objects
        """        
        def __write_csv(path, csv_lines):
            """write the string info into a csv
            """        
            with open(path, 'w') as f:
                for line in csv_lines:
                    f.write(line)
        csv_lines = []#gather string info to a csv
        for key in self._keys:
            value = self._table_map[key]
            if isinstance(value, list):
                path = os.path.join(self.parent_path, str(key))
                os.makedirs(path, exist_ok = True)
                setattr(self, key, Table(value, path))
                
            elif isinstance(value, dict):
                path = os.path.join(self.parent_path, str(key))
                os.makedirs(path, exist_ok = True)
                setattr(self, key, TableMap(value, path))

            else:
                line = str(key) + ',' + str(value) + '\n'
                csv_lines.append(line)
        csv_path = os.path.join(self.parent_path, 'tabular_info.csv')
        __write_csv(csv_path, csv_lines)
        
                  
            
            

                
               
class JsonRec(TableMap):
    """class definition of json record objects 
        that use data from json files
    """    
    def __init__(self, json_path: str, parent_path: str, folder_name: str):
        self.__load_json_data(json_path)#load data from json file to python dict
        path = os.path.join(parent_path, folder_name)
        os.makedirs(path, exist_ok = True)      
        TableMap.__init__(self, self._raw_data, path)
        
        
    def __load_json_data(self, json_path):
        """convert json data to python dictionaries
        """        
        with open(json_path ,'r') as f:
            data = json.loads(f.read())
        self._raw_data = data


            
class Table(object):
    """tabular object

    """    
    def __init__(self, dict_list: list, parent_path):
        self.parent_path = parent_path
        self.__set_attributes(dict_list)
        self.__create_dirs()
    
    def __set_attributes(self, dict_list: 'list[dict]'):
        self._dict_list = dict_list
        
    def __create_dirs(self):
    
                    
        def __line_converter(num):
            row = self._dict_list[num]
            path = os.path.join(self.parent_path, 'record_' + str(num))
            os.makedirs(path, exist_ok = True)
            if isinstance(row, dict):                
                setattr(self, 'record_' + str(num), TableMap(row, path))               
            else:
                csv_path = os.path.join(path, 'string_info.csv')
                with open(csv_path, 'w') as f:
                    f.write(str(row))
              
        for num in range(len(self._dict_list)):
            __line_converter(num)

        
            
            
    
    
    
    
    
#testing
if __name__ == '__main__':
    #locate the data folder
    rel_path = os.path.join('..', 'data')

    #grab files in folder
    __json_file_paths = glob.glob(os.path.join(rel_path, '*.json'))
    __json_file_names = list(map(lambda x: x.replace('.json', ''), os.listdir(rel_path)))
    #testing
    #pilot = JsonRec(__json_file_paths[0], '..', __json_file_names[0].replace('.json', ''))
    
    for index in range(len(__json_file_paths)):
        JsonRec(__json_file_paths[index], '..', __json_file_names[index])
    
    print()
            
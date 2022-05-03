"""controls the json file for the server.
"""
import tkinter, server

#prepare
rel_path = server.options.get_rel_path()
names = server.options.get_json_file_names(rel_path)
paths = server.options.get_json_file_paths(rel_path)

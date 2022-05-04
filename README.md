# Solution to assessment:

The solution creates a file system from each json file in the data folder. A testing.py is made for the assessers to test the program. To process all data, please run server.py
Note: if you are running it on a terminal, please set the working directory as /exa-data-eng-assessment/scripts.

## Development ideas:

* Instantiate nested dictionaries and lists when creating an instance of each json file; for each object (Table or TableMap) create a subfolder(s) for each dictionary contained in it. Gather the leftpver string or float type data and put them in the folder parallely with the subfolders.

## Scripts:

* server.py: contains all classes for processing json files.
* testing.py: testing module which runs three tests to validate the classes in server.py

## Classes:

* TableMap: Template for a dictionary containing other objects (str, float, dict, list(instantiated to Table object)).
* Table: Template for a list of dictionaries(instantiated to TableMap object) or values(gathered in .csv files)),
* JsonRec(TableMap): Template for a json file, inherited attribs of TableMap.

## Implementation:

* Create Table and TableMap classes to instantiate the dictionaries and list of dictionaries nested in a json structure.
* Pass the path of the parent(the path) to the objects contained in a dictionary(TableMap/Table object), create new folders with the keys as their names (joining the parent path and the names and use os.makedirs(path)).
* Write the leftover data to a .csv file, place it alongside the newly created folders.

## Other files and folders:

* data: folder containing the raw(json) data
* test: folder contating the test results of testing.py
* dir_tree: file containing the tree structure of the directory
* Dockerfile: file for creating an image of the app for containerization
* README_old.md: file from the source, containing intro to project.

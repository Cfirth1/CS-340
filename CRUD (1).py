from pymongo import MongoClient
from bson.objectid import ObjectId
import csv
import pandas as pd
import json
from io import StringIO

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def detect_format_simple(self, data):
        
        # For all data, don't use any format, accept "all" as an argument
        if data == "all_data":
            return "all_data"
    
        # Try JSON first
        try:
            pd.read_json(data)
            return "json"
        except ValueError:
            pass

        # Try CSV next
        try:
            pd.read_csv(StringIO(data))            
            return "csv"
        except Exception:
            pass

        return "unknown"

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32427
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
                with open(data, mode="r", newline="") as file:
                    reader = csv.DictReader(file) # Reads each row as a dictionary
                    data = [row for row in reader]  # Convert to a list of dictionaries

                self.database.animals.insert_many(data)  # data should be dictionary
        else:
                raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, filter_criteria):
         animal_data = list(self.collection.find(filter_criteria))
         return animal_data
        
        #criteria_format = self.detect_format_simple(filter_criteria)
        
        #support both json and csv; determine input's format
        #if criteria_format == "json":
            #handle as json
        #    filter_criteria = json.loads(filter_criteria)
        #    animal_data = list(self.collection.find(filter_criteria))
            

        #elif criteria_format == "csv":
            #handle as csv
            # Split into lines and parse with csv.DictReader
        #    lines = filter_criteria.splitlines()
        #    reader = csv.DictReader(lines)

            # Get the first row as a dictionary
        #    filter_criteria = next(reader)
        #    animal_data = list(self.collection.find(filter_criteria))
            
        #elif criteria_format == "all_data":
        #    animal_data = list(self.collection.find())


        #else:
        #    return "Unsupported format"
                      
        #return animal_data
    
#Update method that queries for and changes document(s) 
    def update(self, query, new_values, multiple=False):
       if multiple:
        result = self.collection.update_many(query, new_values)
       else:
        result = self.collection.update_one(query, new_values)
       return result.modified_count



# Delete method
    def delete(self, query, multiple=False):
       if multiple:
        result = self.database.animals.delete_many(query)
       else:
        result = self.database.animals.delete_one(query)
       return result.deleted_count


import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """
    A class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self) -> None:
        """
        Initializes the MongoDB client connection.
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            print(f"Connected to MongoDB - Database: {self.mongo_client.database.name}")
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.
        database_name : Optional[str]
            Name of the database (optional). Defaults to DATABASE_NAME.

        Returns:
        -------
        pd.DataFrame
            DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """
        try:
            # Step 1: Connect to the correct database and collection
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            # Step 2: Debug collection details
            print(f"Using collection: {collection_name}")
            print(f"Total documents in collection: {collection.count_documents({})}")
            
            if collection.count_documents({}) == 0:
                raise MyException(f"Collection '{collection_name}' is empty." , sys)

            # Step 3: Fetch data from collection
            print("Fetching data from MongoDB...")
            data = list(collection.find())
            print(f"Fetched {len(data)} records from MongoDB.")

            if len(data) == 0:
                raise MyException(f"No data fetched from collection '{collection_name}'." , sys)

            # Step 4: Convert to DataFrame
            df = pd.DataFrame(data)
            print(f"Converted to DataFrame with shape: {df.shape}")

            # Step 5: Clean up the DataFrame
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
                print("Dropped '_id' column from DataFrame")

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            print(f"Error during data fetching: {e}")
            raise MyException(e, sys) from e

"""
Data Preprocessing Script
This script reads in cvs data, cleans it removing null values and bull-uploads it to the MySQL database using pands and SQLAlchemy
"""

import os
import logging
import pandas as pd
from sqlalchemy import create_engine

# Set up the logging format to print out status updates to the terminal
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def read_data(filename):
    """Load the CSV file into a pandas DataFrame."""
    logging.info(f"Reading data from {filename}")
    try:
        #Loads the csv file into a pandas DataFrame structure
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        #catches and logs any loading errors before exiting
        logging.error(f"Error reading file: {e}")
        raise e

def clean_data(data):
    """Clean the data by dropping rows with missing values."""
    logging.info("Cleaning data...")
    #Removes any of the rows from a dataset that cotain missing or empty cells
    cleaned_data = data.dropna()
    return cleaned_data

def load_data(data, table):
    """Upload the DataFrame to MySQL using SQLAlchemy bulk upload."""
    logging.info(f"Starting database upload to table: {table}")
    
    #Retreieves our database credentials from system environment variables 
    db_host = os.getenv("DBHOST")
    db_name = os.getenv("DBNAME")
    db_user = os.getenv("DBUSER")
    db_password = os.getenv("DBPASS")
    
    #Creates the connection needed by SQLAlchemy
    connection_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:3306/{db_name}"
    
    try:
        #Creates engine manager using the connection configuration URL
        engine = create_engine(connection_url)
        #Opens a database connection block to upload the data safely
        with engine.begin() as connection:
            data.to_sql(name=table, con=connection, if_exists='append', index=False)
            
        logging.info("Database upload successful!")
        
    except Exception as e:
        #Documents the specific fails of the database interactions
        logging.error(f"Database error occurred: {e}")
        raise e

def main():
    #Define our targeted storage location properties and file names assets
    csv_file = "MOCK_DATA.csv"
    table_name = "mock"
    
    try:
        #pulls raw dataset info
        raw_df = read_data(csv_file)
        #filter out broken or incomplete data points
        cleaned_df = clean_data(raw_df)
        #Upload the cleaned data into the MySQL table
        load_data(cleaned_df, table_name)
        
    except Exception as e:
        #Logs the errors in case anything in the pipeline fails
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    #Runs the main function when the script is executed
    main()


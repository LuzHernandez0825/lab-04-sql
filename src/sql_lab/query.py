"""
Database Query Script
This script connects to the MySQL table to filter data by group and calculate row counts.
"""

import os
import logging
import mysql.connector

# Setup logging output to match process.py
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def get_data_by_group(value):
    """
    Selects rows from the database where the group column matches the value.
    
    Args:
        value (str): The specific group value used to filter the group column.
        
    Returns:
        list: A list of all matching rows gotten from the database table.
    """
    logging.info(f"Filtering database rows where the group column equals: '{value}'")
    
    #Gets the credentials from the environment variables
    db_host = os.getenv("DBHOST")
    db_name = os.getenv("DBNAME")
    db_user = os.getenv("DBUSER")
    db_password = os.getenv("DBPASS")
    
    results = []
    
    try:
        # Open the connection to the MySQL database
        conn = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()
        
        # Use a %s placeholder for safety.
        # `group` uses backticks to prevent an error from using a key word in MySQL
        query = "SELECT * FROM mock WHERE `group` = %s"
        
        # Execute the query safely by passing the variable inside a tuple
        cursor.execute(query, (value,))
        results = cursor.fetchall()
        
        # Close the cursor and connection to clean up resources
        cursor.close()
        conn.close()
        
        logging.info("Successfully fetched matching group records!")
        
    except Exception as e:
        # Logs the error if for some reason the query fails
        logging.error(f"Error executing group query: {e}")
        raise e
        
    return results

def plot_counts(groupby):
    """
    Groups the rows by a specific column and counts the amount of times distinct values appear
    
    Args:
        groupby (str): The name of the database table column to group by.
        
    Returns:
        dict: A dictionary structure pairing distinct column values with row counts.
    """
    logging.info(f"Calculating row distributions grouped by column: '{groupby}'")
    
    # Gets the credentials from the environment variables
    db_host = os.getenv("DBHOST")
    db_name = os.getenv("DBNAME")
    db_user = os.getenv("DBUSER")
    db_password = os.getenv("DBPASS")
    
    counts_dict = {}
    
    try:
        # Opens connection with the MySQL database
        conn = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()

        #Puts the column name in a string so column can change dynamically
        query = f"SELECT {groupby}, COUNT(*) FROM mock GROUP BY {groupby}"
        
        cursor.execute(query)
        results = cursor.fetchall()

        # Loops through rows and stros key value pairs in a dictionary        
        for row in results:
            counts_dict[str(row[0])] = row[1]
            
        cursor.close()
        conn.close()
        
        logging.info("Successfully calculated database aggregation metrics!")
        
    except Exception as e:
        #Logs error if query breaks
        logging.error(f"Error calculating column counts: {e}")
        raise e
        
    return counts_dict

def main():
    """Main function to execute the query functions"""
    # Test values for the script
    target_group = "alpha"
    target_column = "gender" 
    
    try:
        # Filter rows by group
        matching_rows = get_data_by_group(target_group)
        print(f"\n[Test 1 Results] Total rows found in group '{target_group}': {len(matching_rows)}")
        
        # Prints first 3 lines to show it works
        print("Sample Rows:")
        for row in matching_rows[:3]:
            print(f"  {row}")
            
        # Gets row counts grouped by a column
        distribution = plot_counts(target_column)
        print(f"\n[Test 2 Results] Value distribution breakdown for '{target_column}':")
        for key, value in distribution.items():
            print(f"  * {key}: {value} rows")
            
    except Exception as e:
        # Catches and prints error details if the main sequence crashes
        print(f"\n[Run Failure] The demonstration routine crashed: {e}")

if __name__ == "__main__":
    # Runs main function when called in the terminal
    main()


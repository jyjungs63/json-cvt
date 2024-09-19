import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="happyzip"
)

cursor = conn.cursor()

# Function to insert binary data
def insert_file(file_path, file_name):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    
    sql = "INSERT INTO files (file_name, file_data) VALUES (%s, %s)"
    cursor.execute(sql, (file_name, binary_data))
    conn.commit()
    print(f"File {file_name} inserted successfully.")

# Example usage
file_path = 'D:\\12_DB\\json-cvt\\jsonCh\\B_Spline_1.exe'  # Replace with the path to your file
file_name = 'B_Spline_1.exe'          # Replace with your file name
insert_file(file_path, file_name)

# Close the connection
cursor.close()
conn.close()

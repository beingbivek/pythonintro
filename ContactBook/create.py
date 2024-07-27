# Create new contact
from main import create_connection


con = create_connection()
cursor = con.cursor()
name = input("Enter Name: ")
phone = input("Enter Phone: ")
cursor.execute("INSERT INTO contacts (name,phone) VALUES (%s,%s)",(name,phone))
con.commit()
con.close()
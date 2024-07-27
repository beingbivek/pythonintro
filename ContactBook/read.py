from main import create_connection

con = create_connection()
cursor = con.cursor()
cursor.execute("SELECT * FROM contacts")
contacts = cursor.fetchall()
for i in contacts:
    print(i)
con.close()
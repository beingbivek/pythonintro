from main import create_connection

con = create_connection()
cursor = con.cursor()
id = int(input("Enter id to delte: "))
cursor.execute(f"DELETE FROM contacts where id = {id}")
contacts = cursor.fetchall()
for i in contacts:
    print(i)
con.close()
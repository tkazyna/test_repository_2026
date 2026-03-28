import psycopg2
import csv
from config import config 

#  CREATE TABLE
def create_table():
    """Create the contacts table if it doesn't exist"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE
        )
        """,
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
        print("Table ready.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# INSERT FROM CONSOLE
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")

    sql = "INSERT INTO contacts(first_name, last_name, phone) VALUES(%s, %s, %s) RETURNING id;"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, last_name, phone))
        contact_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print(f"Contact added with ID: {contact_id}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# UPLOAD FROM CSV 
def upload_from_csv(file_path):
    sql = "INSERT INTO contacts(first_name, last_name, phone) VALUES(%s, %s, %s)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) 
            for row in reader:
                if len(row) == 3:
                    cur.execute(sql, row)

        conn.commit()
        cur.close()
        print("CSV imported successfully.")
    except FileNotFoundError:
        print("CSV file not found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#  SHOW ALL CONTACTS
def show_all_contacts():
    sql = "SELECT * FROM contacts ORDER BY id"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if rows:
            print("\n--- CONTACTS ---")
            for row in rows:
                print(row)
        else:
            print("No contacts found.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# SEARCH
def query_contacts(filter_type, value):
    allowed_filters = ['first_name', 'last_name', 'phone']

    if filter_type not in allowed_filters:
        print("Invalid filter type.")
        return

    sql = f"SELECT * FROM contacts WHERE {filter_type} ILIKE %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (f"%{value}%",))
        rows = cur.fetchall()
        if rows:
            print("\n--- SEARCH RESULTS ---")
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# UPDATE CONTACT
def update_contact(phone, new_first_name=None, new_phone=None):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if new_first_name:
            cur.execute("UPDATE contacts SET first_name=%s WHERE phone=%s", (new_first_name, phone))
        if new_phone:
            cur.execute("UPDATE contacts SET phone=%s WHERE phone=%s", (new_phone, phone))
        conn.commit()
        print(f"Updated {cur.rowcount} row(s).")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#  DELETE CONTACT 
def delete_contact(identifier):
    sql = "DELETE FROM contacts WHERE first_name=%s OR phone=%s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (identifier, identifier))
        conn.commit()
        print(f"Deleted {cur.rowcount} row(s).")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#  MENU 
def menu():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Create table")
        print("2. Insert from console")
        print("3. Upload from CSV")
        print("4. Show all contacts")
        print("5. Search contacts")
        print("6. Update contact")
        print("7. Delete contact")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            file_path = input("Enter CSV file path: ")
            upload_from_csv(file_path)
        elif choice == "4":
            show_all_contacts()
        elif choice == "5":
            print("Search by: first_name / last_name / phone")
            filter_type = input("Enter filter type: ")
            value = input("Enter search value: ")
            query_contacts(filter_type, value)
        elif choice == "6":
            phone = input("Enter current phone number: ")
            new_first_name = input("Enter new first name (or Enter to skip): ") or None
            new_phone = input("Enter new phone number (or Enter to skip): ") or None
            update_contact(phone, new_first_name, new_phone)
        elif choice == "7":
            identifier = input("Enter first name OR phone to delete: ")
            delete_contact(identifier)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
import psycopg2
from connect import get_connection


def show_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_all_contacts()")
    rows = cur.fetchall()
    if not rows:
        print("No contacts found.")
    for row in rows:
        print(f"{row[0]}  Name: {row[1]} {row[2]} , Phone: {row[3]}")
    cur.close()
    conn.close()


def add_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Saved.")


def add_many_contacts():
    print("Enter contacts (empty first name to stop):")
    data = []
    while True:
        first = input("First name (or Enter to stop): ")
        if not first:
            break
        last = input("Last name: ")
        phone = input("Phone: ")
        data.append(f"{first}|{last}|{phone}")

    if not data:
        print("Nothing to insert.")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_many_contacts(%s)", (data,))
    conn.commit()
    cur.close()
    conn.close()
    print("Done. Check terminal for invalid entries.")


def search():
    value = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (value,))
    rows = cur.fetchall()
    if not rows:
        print("Not found.")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Phone: {row[3]}")
    cur.close()
    conn.close()


def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    if not rows:
        print("No contacts found.")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Phone: {row[3]}")
    cur.close()
    conn.close()


def delete():
    value = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact_proc(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")


def menu():
    while True:
        print("\n1. Show all contacts")
        print("2. Add / Update contact")
        print("3. Add many contacts")
        print("4. Search")
        print("5. Show with pagination")
        print("6. Delete")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            add_many_contacts()
        elif choice == "4":
            search()
        elif choice == "5":
            show_paginated()
        elif choice == "6":
            delete()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
import csv
import os
import psycopg2
from psycopg2 import errors
# Import your existing configuration
from config import load_config


class PhoneBookApp:

    def __init__(self, config):
        """Initialize database connection."""
        self.config = config
        self.conn = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(**self.config)
            self.conn.autocommit = True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            exit(1)

    def create_table(self):
        """Creates the schema table if it does not already exist."""
        query = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        with self.conn.cursor() as cursor:
            cursor.execute(query)

    # ---------------------------------------------------------
    # FEATURE 1: Insert Single Contact (Console/Manual)
    # ---------------------------------------------------------
    def insert_contact(self, username, first_name, last_name, phone):
        """Inserts a new contact with conflict handling."""
        query = """
        INSERT INTO phonebook (username, first_name, last_name, phone)
        VALUES (%s, %s, %s, %s);
        """
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, (username, first_name, last_name, phone))
            print(f"✅ Contact '{username}' successfully added.")
            return True
        except errors.UniqueViolation:
            print(
                f"❌ Error: The username '{username}' or phone '{phone}' already exists."
            )
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
        return False

    # ---------------------------------------------------------
    # FEATURE 2: Bulk Insert from CSV File
    # ---------------------------------------------------------
    def import_from_csv(self, file_path):
        """Parses a CSV and bulk-inserts rows cleanly using a single transaction."""
        if not os.path.exists(file_path):
            print(f"❌ File not found at path: {file_path}")
            return

        print(f"⏳ Processing CSV file: {file_path}...")
        query = """
        INSERT INTO phonebook (username, first_name, last_name, phone)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (username) DO UPDATE 
        SET first_name = EXCLUDED.first_name, 
            last_name = EXCLUDED.last_name, 
            phone = EXCLUDED.phone;
        """
        # Using ON CONFLICT updates existing records if username hits a duplicate

        try:
            with open(file_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(
                    f
                )  # Expects headers: username, first_name, last_name, phone
                rows_to_insert = [
                    (
                        row["username"].strip(),
                        row["first_name"].strip(),
                        row["last_name"].strip(),
                        row["phone"].strip(),
                    )
                    for row in reader
                ]

            with self.conn.cursor() as cursor:
                cursor.executemany(query, rows_to_insert)

            print(f"✅ Successfully imported/updated {len(rows_to_insert)} contacts from CSV.")
        except KeyError as ke:
            print(
                f"❌ CSV Format Error: Missing required column header {ke}. Ensure columns match code headers."
            )
        except Exception as e:
            print(f"❌ CSV Processing Error: {e}")

    # ---------------------------------------------------------
    # FEATURE 3: Update Contact Details
    # ---------------------------------------------------------
    def update_contact(self, username, first_name=None, phone=None):
        """Dynamically updates first name, phone, or both for a given username."""
        if not first_name and not phone:
            print("⚠️ Nothing to update.")
            return

        # Dynamically build SQL to only alter fields provided
        fields = []
        values = []
        if first_name:
            fields.append("first_name = %s")
            values.append(first_name)
        if phone:
            fields.append("phone = %s")
            values.append(phone)

        values.append(username)  # For WHERE clause
        query = f"UPDATE phonebook SET {', '.join(fields)} WHERE username = %s;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, tuple(values))
            if cursor.rowcount > 0:
                print(f"✅ Contact '{username}' successfully updated.")
            else:
                print(f"⚠️ Contact with username '{username}' not found.")

    # ---------------------------------------------------------
    # FEATURE 4: Flexible Queries / Filtering
    # ---------------------------------------------------------
    def query_contacts(self, name_filter=None, phone_prefix=None):
        """Filters phonebook records using case-insensitive partial searches."""
        query = "SELECT username, first_name, last_name, phone FROM phonebook WHERE 1=1"
        params = []

        if name_filter:
            # Matches substring within first_name or last_name
            query += " AND (first_name ILIKE %s OR last_name ILIKE %s)"
            params.extend([f"%{name_filter}%", f"%{name_filter}%"])

        if phone_prefix:
            # Matches start of the phone number string
            query += " AND phone LIKE %s"
            params.append(f"{phone_prefix}%")

        query += " ORDER BY first_name ASC;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, tuple(params))
            results = cursor.fetchall()

        if not results:
            print("📭 No matching records found.")
            return

        print(
            f"\n🔎 Found {len(results)} matches:\n"
            f"{'Username':<15} | {'First Name':<15} | {'Last Name':<15} | {'Phone':<15}"
        )
        print("-" * 68)
        for row in results:
            print(f"{row[0]:<15} | {row[1]:<15} | {row[2]:<15} | {row[3]:<15}")
        print()

    # ---------------------------------------------------------
    # FEATURE 5: Delete Records
    # ---------------------------------------------------------
    def delete_contact(self, identifier, delete_by="username"):
        """Deletes matching rows by either 'username' or exact 'phone' matching."""
        if delete_by not in ["username", "phone"]:
            return

        query = f"DELETE FROM phonebook WHERE {delete_by} = %s;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, (identifier,))
            if cursor.rowcount > 0:
                print(
                    f"🗑️ Removed contact where {delete_by} was '{identifier}'."
                )
            else:
                print(f"⚠️ No contact matched {delete_by} '{identifier}'.")

    def close(self):
        if self.conn:
            self.conn.close()


# ---------------------------------------------------------
# INTERACTIVE CONSOLE INTERFACE
# ---------------------------------------------------------
def main():
    try:
        # Call the function to read your 'database.ini' file and get the dictionary
        db_config = load_config() 
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        return

    # Pass the resulting dictionary to your App
    app = PhoneBookApp(db_config)

    while True:
        print("\n=== PhoneBook PostgreSQL Manager ===")
        print("1. Add Contact via Console")
        print("2. Import Contacts from CSV File")
        print("3. Update Contact Details")
        print("4. Search / Filter Contacts")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            username = input("Enter unique username: ").strip()
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name (optional): ").strip()
            phone = input("Enter unique phone number: ").strip()
            if username and first_name and phone:
                app.insert_contact(username, first_name, last_name, phone)
            else:
                print("❌ Username, First Name, and Phone are mandatory fields.")

        elif choice == "2":
            path = input("Enter full path to CSV file: ").strip()
            app.import_from_csv(path)

        elif choice == "3":
            username = input(
                "Enter target username to modify: "
            ).strip()
            print("Leave blank if you do not wish to modify a specific field.")
            new_name = input("Enter new first name: ").strip() or None
            new_phone = input("Enter new phone number: ").strip() or None
            app.update_contact(username, first_name=new_name, phone=new_phone)

        elif choice == "4":
            print(
                "Provide filtering data (Press Enter/Leave blank to bypass a filter):"
            )
            name_filter = input("Filter by name substring: ").strip() or None
            phone_prefix = input("Filter by phone prefix: ").strip() or None
            app.query_contacts(
                name_filter=name_filter, phone_prefix=phone_prefix
            )

        elif choice == "5":
            print("Delete configurations:")
            print("1. Delete using Username")
            print("2. Delete using Phone Number")
            sub_choice = input("Selection: ").strip()

            if sub_choice == "1":
                val = input("Enter exact username: ").strip()
                app.delete_contact(val, delete_by="username")
            elif sub_choice == "2":
                val = input("Enter exact phone number: ").strip()
                app.delete_contact(val, delete_by="phone")
            else:
                print("❌ Invalid sub-choice selection.")

        elif choice == "6":
            print("🔌 Closing database connection. Goodbye!")
            app.close()
            break
        else:
            print("❌ Invalid Selection. Try again.")


if __name__ == "__main__":
    main()
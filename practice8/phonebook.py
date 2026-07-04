import psycopg2
from config import load_config

class AdvancedPhoneBook:
    def __init__(self):
        config = load_config()
        self.conn = psycopg2.connect(**config)
        self.conn.autocommit = True

    # 1. Pattern Matching (Calls database function via SELECT)
    def search(self, pattern):
        query = "SELECT * FROM search_contacts(%s);"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (pattern,))
            return cursor.fetchall()

    # 2. Upsert Contact (Calls stored procedure via CALL)
    def upsert(self, username, first_name, last_name, phone):
        query = "CALL upsert_contact(%s, %s, %s, %s);"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (username, first_name, last_name, phone))
            print(f"✅ Executed upsert routine for user: {username}")

    # 3. Bulk Insert with Internal Database Validation Loops
    def bulk_insert(self, contacts_list):
        # Unpack list of dicts/tuples into separate parallel lists for PostgreSQL arrays
        usernames = [c['username'] for c in contacts_list]
        first_names = [c['first_name'] for c in contacts_list]
        last_names = [c['last_name'] for c in contacts_list]
        phones = [c['phone'] for c in contacts_list]

        # In psycopg2, you pass Python lists, and it converts them to native SQL arrays
        # We must provide placeholder arguments for OUT variables so psycopg2 can catch them
        query = "CALL bulk_insert_with_validation(%s, %s, %s, %s, NULL, NULL, NULL);"
        
        with self.conn.cursor() as cursor:
            cursor.execute(query, (usernames, first_names, last_names, phones))
            # fetchall() or fetchone() picks up OUT parameters returned from a PROCEDURE CALL
            bad_usernames, bad_phones, reasons = cursor.fetchone()
            
        return bad_usernames, bad_phones, reasons

    # 4. Pagination (Calls database function)
    def get_page(self, limit, offset):
        query = "SELECT * FROM get_contacts_paginated(%s, %s);"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (limit, offset))
            return cursor.fetchall()

    # 5. Delete Strategy (Calls stored procedure)
    def remove(self, identifier, strategy):
        query = "CALL delete_contact_by_identifier(%s, %s);"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (identifier, strategy))
            print(f"🗑️ Delete command executed using strategy '{strategy}' for '{identifier}'.")

    def close(self):
        self.conn.close()

# --- Execution Test Run ---
if __name__ == "__main__":
    pb = AdvancedPhoneBook()

    print("--- 1. Testing Upsert Routine ---")
    pb.upsert("tonystark", "Tony", "Stark", "+123456789")
    pb.upsert("tonystark", "Tony", "Stark", "+199999999") # Updates phone number flawlessly

    print("\n--- 2. Testing Pattern Match Search ---")
    pb.upsert("peterparker", "Peter", "Parker", "+155555555")
    matches = pb.search("parker")
    print("Search matches:", matches)

    print("\n--- 3. Testing Stored Procedure Bulk Validation Loop ---")
    test_batch = [
        {"username": "clarkkent", "first_name": "Clark", "last_name": "Kent", "phone": "+188888888"}, # Valid
        {"username": "brucewayne", "first_name": "Bruce", "last_name": "Wayne", "phone": "123-BAD"},  # Invalid format
        {"username": "flash", "first_name": "Barry", "last_name": "Allen", "phone": "+199999999"}    # Duplicate Phone Check
    ]
    bad_users, bad_phones, reasons = pb.bulk_insert(test_batch)
    if bad_users:
        print("❌ Found Rejected Records inside the DB routine:")
        for u, p, r in zip(bad_users, bad_phones, reasons):
            print(f" User: {u} | Phone: {p} | Reason: {r}")

    print("\n--- 4. Testing Pagination Server-Side ---")
    # Fetch Page 1 (Limit 2, Offset 0)
    page_one = pb.get_page(limit=2, offset=0)
    print("Page One Data:", page_one)

    print("\n--- 5. Testing Delete Strategy Procedure ---")
    pb.remove("tonystark", "username")
    pb.remove("+155555555", "phone")

    pb.close()
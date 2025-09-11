def header():
    print("=" * 50)
    print(f"{'DB PERFORMANCE TESTER':^50}")
    print("=" * 50)

def connectionStatus(db_connection):
    if db_connection.test_connection():
        print(f"✓ Connected to {'<host>'} on port \n")
    else:
        print(f"✗ Not connected to {'<host>'}\n")
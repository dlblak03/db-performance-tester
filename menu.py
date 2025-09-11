def header():
    print(f"{'':=^50}")
    print(f"{'DB PERFORMANCE TESTER':^48}")
    print(f"{'':=^50}")

def connectionStatus(connected, db_host='<host>'):
    if connected:
        print(f"✓ Connected to {db_host}")
    else:
        print(f"✗ Not connected to {db_host}")
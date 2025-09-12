import getpass

def header():
    print("-" * 50)
    print(f"|{'DB PERFORMANCE TESTER':^48}|")
    print("-" * 50)

def connection_parameters(db_connection):
    print(f"{'| Type:'[:10]:<10}{(db_connection.configuration.get('type', '<type>') + ' |')[:40]:>40}")
    print(f"{'| Host:'[:10]:<10}{(db_connection.configuration.get('host', '<host>') + ' |')[:40]:>40}")
    print(f"{'| Port:'[:10]:<10}{(db_connection.configuration.get('port', '<port>') + ' |')[:40]:>40}")
    print(f"{'| Database:'[:10]:<10}{(db_connection.configuration.get('database', '<database>') + ' |')[:40]:>40}")
    print(f"{'| Username:'[:10]:<10}{(db_connection.configuration.get('username', '<username>') + ' |')[:40]:>40}")
    print(f"{'| Password:'[:10]:<10}{(db_connection.configuration.get('password', '<password>') + ' |')[:40]:>40}")
    print("-" * 50)

def connection_status(db_connection):
    if db_connection.test_connection():
        print(f"|{'✓ Connected to <host> on port':^48}|")
        print("-" * 50)
    else:
        print(f"|{'✗ Not connected to <host>':^48}|")
        print("-" * 50)

def set_type(db_connection):
    while True:
        print("\nSelect a database type:\n")
        print("1. PostgreSQL\n")
        type = input("(1): ").strip()

        if type == '1':
            db_connection.configuration['type'] = 'PostgreSQL'
            break
        else:
            print('\nInvalid option. Please try again.\n')

def set_host(db_connection):
    while True:
        host = input("\nEnter the database host: ").strip()
        db_connection.configuration['host'] = host

        break

def set_port(db_connection):
    while True:
        port = input("\nEnter the port number: ").strip()
        if port.isdigit():
            db_connection.configuration['port'] = port
            break
        else:
            print('\nInvalid option. Please try again.\n')

def set_database(db_connection):
    while True:
        database = input("\nEnter the database name: ").strip()
        db_connection.configuration['database'] = database
        
        break

def set_username(db_connection):
    while True:
        username = input("\nEnter the username: ").strip()
        db_connection.configuration['username'] = username

        break

def set_password(db_connection):
    while True:
        password = getpass.getpass("\nEnter the password: ").strip()
        db_connection.configuration['password'] = '*' * len(password)

        break
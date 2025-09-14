import getpass
import os

def header():
    print("-" * 50)
    print(f"|{'DB PERFORMANCE TESTER':^48}|")
    print("-" * 50)

def connection_parameters(db_connection):
    print(f"{'| Type:'[:10]:<10}{(db_connection.configuration.get('type', '<type>') + ' |')[:40]:>40}")
    print(f"{'| Min Connections:'[:10]:<10}{(db_connection.configuration.get('min_connections', '<2>') + ' |')[:40]:>40}")
    print(f"{'| Max Connections:'[:10]:<10}{(db_connection.configuration.get('max_connections', '<10>') + ' |')[:40]:>40}")
    print(f"{'| Host:'[:10]:<10}{(db_connection.configuration.get('host', '<host>') + ' |')[:40]:>40}")
    print(f"{'| Port:'[:10]:<10}{(db_connection.configuration.get('port', '<port>') + ' |')[:40]:>40}")
    print(f"{'| Database:'[:10]:<10}{(db_connection.configuration.get('database', '<database>') + ' |')[:40]:>40}")
    print(f"{'| Username:'[:10]:<10}{(db_connection.configuration.get('username', '<username>') + ' |')[:40]:>40}")
    print(f"{'| Password:'[:10]:<10}{('*' * len(db_connection.configuration.get('password', '<password>')) + ' |')[:40]:>40}")
    print("-" * 50)

def connection_status(db_connection):
    if db_connection.test_connection():
        print(f"|{'✓ Connected to ' + db_connection.configuration['host'][:15] + ' on port ' + db_connection.configuration['port']:^48}|")
        print("-" * 50)
    else:
        print(f"|{'✗ Not connected to ' + db_connection.configuration.get('host', '<host>')[:15]:^48}|")
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

def set_min_connections(db_connection):
    while True:
        min = input("\nEnter the min connections for connection pool: ").strip()
        if min.isdigit():
            db_connection.configuration['min_connections'] = min
            break
        else:
            print('\nInvalid option. Please try again.\n')

def set_max_connections(db_connection):
    while True:
        max = input("\nEnter the max connections for connection pool: ").strip()
        if max.isdigit():
            db_connection.configuration['max_connections'] = max
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
        db_connection.configuration['password'] = password

        break

def confirm_configuration(db_connection):
    while True:
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')

        header()
        connection_parameters(db_connection)
        connection_status(db_connection)

        print("\nConfirm the configuration:\n")
        
        print("1. Edit Type")
        print("2. Edit Min Connections")
        print("3. Edit Max Connections")
        print("4. Edit Host")
        print("5. Edit Port")
        print("6. Edit Database")
        print("7. Edit Username")
        print("8. Edit password")
        print("9. Confirm configuration")

        option = input("\n(1-9): ").strip()

        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')

        header()
        connection_parameters(db_connection)
        connection_status(db_connection)

        match option:
            case '1':
                set_type(db_connection)
            case '2':
                set_min_connections(db_connection)
            case '3':
                set_max_connections(db_connection)
            case '4':
                set_host(db_connection)
            case '5':
                set_port(db_connection)
            case '6':
                set_database(db_connection)
            case '7':
                set_username(db_connection)
            case '8':
                set_password(db_connection)
            case '9':
                break


class db_connection:
    def __init__(self):
        self.connection = None
        self.configuration = {}
        self.configured = False

    def set_configuration(self):
        for step in ['type','host','port','database','username','password', 'confirm']: 
            menu.header()
            menu.connection_parameters(self)
            menu.connection_status(self)

            match step:
                case 'type':
                    menu.set_type(self)
                case 'host':
                    menu.set_host(self)
                case 'port':
                    menu.set_port(self)
                case 'database':
                    menu.set_database(self)
                case 'username':
                    menu.set_username(self)
                case 'password':
                    menu.set_password(self)
                case 'confirm':
                    menu.confirm_configuration(self)
            
            if os.name == 'nt':  # Windows
                os.system('cls')
            else:  # Unix/Linux/MacOS
                os.system('clear')

        self.configured = True

    def set_connection(self):
        while not self.configured:
            self.set_configuration()

        if self.configuration['type'] == 'PostgreSQL':
            try:
                connection = psycopg2.connect(
                    host=self.configuration['host'],
                    port=self.configuration['port'],
                    database=self.configuration['database'],
                    user=self.configuration['username'],
                    password=self.configuration['password']
                )

                self.connection = connection
            except:
                self.configured = False
                print('A connection could not be established. Please try again.\n')

        
    def test_connection(self):
        if self.configuration.get('type', '') == 'PostgreSQL':
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT version();")
                version = cursor.fetchone()
                cursor.close()
                return True
            except:
                return False

class db_performance_tester:
    def __init__(self):
        self.database = None

    def start(self, database):
        self.database = database

        while True:
            menu.header()
            menu.connection_parameters(self.database)
            menu.connection_status(self.database)

    def query_concurrency_test(self, query, concurrent_users=10):
        pass

    def procedure_concurrency_test(self, procedure, concurrent_users=10):
        pass

def main():
    database = db_connection()
    tester = db_performance_tester()

    while not database.configured:
        database.set_connection()
        
    tester.start(database)

if __name__ == '__main__':
    try:
        import psycopg2
        from psycopg2 import sql
    except ImportError:
        print('\npsycopg2 not found. Install with: pip install psycopg2-binary\n')
        exit(1)
    
    import os
    import menu

    print('\nAll libraries found. Let\'s begin!\n')

    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
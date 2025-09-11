
class db_connection:
    def __init__(self):
        self.connection = None
        self.configuration = {}
        self.configured = False

    def set_configuration(self):
        print(f"{'Configure database connection:':50}\n")

        print("Pick a database type:\n")
        print("1. PostgreSQL\n")
        type = input("(1): ").strip()

        self.configured = True

    def get_connection(self):
        if not self.configured:
            self.set_configuration()
        
        return None
    
    def test_connection(self):
        return False

class db_performance_tester:
    def __init__(self):
        pass

    def query_concurrency_test(self, query, concurrent_users=10):
        pass

    def procedure_concurrency_test(self, procedure, concurrent_users=10):
        pass

def main():
    database = db_connection()
    tester = db_performance_tester()

    while True:
        menu.header()
        menu.connectionStatus(database)

        connection = database.get_connection()

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
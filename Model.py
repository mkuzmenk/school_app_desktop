from DB import start_db

class Model:
    def __init__(self):
        self.Session = start_db()

        assert self.Session is not None, 'DB connection not found'      # if no connection, program won't run


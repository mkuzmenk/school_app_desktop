

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_teacher(self, data):
        for i, j in data.items():
            print(i, j)
from window import Window
from Model import Model
from Controller import Controller

if __name__ == '__main__':
    model = Model()

    view = Window()

    controller = Controller(model, view)
    view.set_controller(controller)

    view.run()

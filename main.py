from view.Window import Window
from model.Model import Model
from controller.Controller import Controller

if __name__ == '__main__':
    model = Model()

    view = Window()

    controller = Controller(model, view)
    view.set_controller(controller)

    view.run()

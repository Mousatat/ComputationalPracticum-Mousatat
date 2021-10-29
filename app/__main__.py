import eel

from controller.web_controller import WebController
from model.model import Model
from view.web_view import WebView


model = Model()
view = WebView(model)
controller = WebController(model, view)


@eel.expose
def onUpdatePage1(params):
    controller.onUpdatePage1(params)


@eel.expose
def onUpdatePage2(params):
    controller.onUpdatePage2(params)


@eel.expose
def onUpdatePage3(params):
    controller.onUpdatePage3(params)


class Application:
    def __init__(self, _model, _view, _controller):
        self.model = _model
        self.view = _view
        self.controller = _controller

    def run(self):
        self.controller.run()


if __name__ == '__main__':
    app = Application(model, view, controller)
    app.run()

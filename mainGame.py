from firstWindow import *
from secondWindow import *


class Controller:
    def __init__(self):
        self.first_window = FirstWindow()
        self.window = SecondWindow()
        self.window.close()

    def show_window1(self):
        self.first_window.switch_window.connect(self.show_window2)
        self.first_window.show()

    def show_window2(self):
        self.first_window.close()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_window1()
    sys.exit(app.exec_())

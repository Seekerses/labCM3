import sys
from PyQt5 import QtWidgets
import design
import graph


class Enter(QtWidgets.QMainWindow, design.UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ready.clicked.connect(self.complete)

    def complete(self):
        self.hide()
        self.graph = Graph(self.getFunc())
        self.graph.show()


class Graph(QtWidgets.QMainWindow, graph.UiMainWindow):
    def __init__(self, function):
        super().__init__()
        self.setupUi(self, function)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Enter()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

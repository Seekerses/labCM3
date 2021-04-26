from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import tablemodel
import imath


def validate_params(a, b, min_intervals, max_intervals):
    if b > a and max_intervals >= min_intervals:
        return True
    else:
        return False


class UiMainWindow(object):

    def setupUi(self, MainWindow, function):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.data = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(20, 20, 371, 251))
        self.graph.setObjectName("graph")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(420, 20, 331, 281))
        self.stackedWidget.setObjectName("stackedWidget")
        self.rectangles = QtWidgets.QWidget()
        self.rectangles.setObjectName("rectangles")
        self.formLayoutWidget = QtWidgets.QWidget(self.rectangles)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 271, 276))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.rect_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_label.setObjectName("rect_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rect_label)
        self.rect_left = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rect_left.setObjectName("rect_left")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rect_left)
        self.rect_right = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rect_right.setObjectName("rect_right")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rect_right)
        self.rect_min = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rect_min.setObjectName("rect_min")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rect_min)
        self.rect_max = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rect_max.setObjectName("rect_max")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rect_max)
        self.rect_accuracy = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rect_accuracy.setObjectName("rect_accuracy")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rect_accuracy)
        self.rect_type = QtWidgets.QComboBox(self.formLayoutWidget)
        self.rect_type.setObjectName("rect_type")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.rect_type)
        self.rect_type.addItem("Левые")
        self.rect_type.addItem("Правые")
        self.rect_type.addItem("Середина")
        self.rect_left_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_left_label.setObjectName("rect_left_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rect_left_label)
        self.rect_right_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_right_label.setObjectName("rect_right_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rect_right_label)
        self.rect_min_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_min_label.setObjectName("rect_min_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rect_min_label)
        self.rect_max_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_max_label.setObjectName("rect_max_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.rect_max_label)
        self.rect_accuracy_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_accuracy_label.setObjectName("rect_accuracy_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.rect_accuracy_label)
        self.rect_type_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.rect_type_label.setObjectName("rect_type_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.rect_type_label)
        self.start_rect_label = QtWidgets.QPushButton(self.formLayoutWidget)
        self.start_rect_label.setObjectName("start_rect_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.start_rect_label)
        self.stackedWidget.addWidget(self.rectangles)
        self.trapeze = QtWidgets.QWidget()
        self.trapeze.setObjectName("trapeze")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.trapeze)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 271, 237))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.start_trapeze_label = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.start_trapeze_label.setObjectName("start_trapeze_label")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.start_trapeze_label)
        self.trapeze_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_label.setObjectName("trapeze_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.trapeze_label)
        self.trapeze_right = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.trapeze_right.setObjectName("trapeze_right")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.trapeze_right)
        self.trapeze_left = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.trapeze_left.setObjectName("trapeze_left")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.trapeze_left)
        self.trapeze_left_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_left_label.setObjectName("trapeze_left_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.trapeze_left_label)
        self.trapeze_right_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_right_label.setObjectName("trapeze_right_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.trapeze_right_label)
        self.trapeze_accuracy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.trapeze_accuracy.setObjectName("trapeze_accuracy")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.trapeze_accuracy)
        self.trapeze_min = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.trapeze_min.setObjectName("trapeze_min")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.trapeze_min)
        self.trapeze_min_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_min_label.setObjectName("trapeze_min_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.trapeze_min_label)
        self.trapeze_max = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.trapeze_max.setObjectName("trapeze_max")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.trapeze_max)
        self.trapeze_max_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_max_label.setObjectName("trapeze_max_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.trapeze_max_label)
        self.trapeze_accuracy_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.trapeze_accuracy_label.setObjectName("trapeze_accuracy_label")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.trapeze_accuracy_label)
        self.stackedWidget.addWidget(self.trapeze)
        self.simpson = QtWidgets.QWidget()
        self.simpson.setObjectName("simpson")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.simpson)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 271, 231))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.start_simpson_label = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.start_simpson_label.setObjectName("start_simpson_label")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.start_simpson_label)
        self.simpson_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_label.setObjectName("simpson_label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.simpson_label)
        self.simpson_left = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.simpson_left.setObjectName("simpson_left")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.simpson_left)
        self.simpson_right = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.simpson_right.setObjectName("simpson_right")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.simpson_right)
        self.simpson_min = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.simpson_min.setObjectName("simpson_min")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.simpson_min)
        self.simpson_max = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.simpson_max.setObjectName("simpson_max")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.simpson_max)
        self.simpson_accuracy = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.simpson_accuracy.setObjectName("simpson_accuracy")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.simpson_accuracy)
        self.simpson_left_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_left_label.setObjectName("simpson_left_label")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.simpson_left_label)
        self.simpson_right_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_right_label.setObjectName("simpson_right_label")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.simpson_right_label)
        self.simpson_min_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_min_label.setObjectName("simpson_min_label")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.simpson_min_label)
        self.simpson_max_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_max_label.setObjectName("simpson_max_label")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.simpson_max_label)
        self.simpson_accuracy_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.simpson_accuracy_label.setObjectName("simpson_accuracy_label")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.simpson_accuracy_label)
        self.stackedWidget.addWidget(self.simpson)
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(55, 341, 691, 211))
        self.table.setObjectName("table")
        self.graph.showGrid(x=True, y=True)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(300, 300, 270, 16))
        self.error.setText("")
        self.error.setObjectName("error")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(150, 300, 121, 24))
        self.save.setObjectName("save")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 300, 121, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.function = function
        self.pushButton.clicked.connect(self.change_method)
        self.start_simpson_label.clicked.connect(self.simpson_init)
        self.start_rect_label.clicked.connect(self.rect_init)
        self.start_trapeze_label.clicked.connect(self.trapeze_init)
        self.save.clicked.connect(self.save_to_file)
        self.update_graph(-10, 10)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rect_label.setText(_translate("MainWindow", "Метод прямоугольников"))
        self.rect_left_label.setText(_translate("MainWindow", "Левая граница"))
        self.rect_right_label.setText(_translate("MainWindow", "Правая граница"))
        self.rect_min_label.setText(_translate("MainWindow", "Минимум интервалов"))
        self.rect_max_label.setText(_translate("MainWindow", "Максимум интервалов"))
        self.rect_accuracy_label.setText(_translate("MainWindow", "Точность"))
        self.rect_type_label.setText(_translate("MainWindow", "Тип метода"))
        self.start_rect_label.setText(_translate("MainWindow", "Рассчитать"))
        self.start_trapeze_label.setText(_translate("MainWindow", "Рассчитать"))
        self.trapeze_label.setText(_translate("MainWindow", "Метод трапеций"))
        self.trapeze_left_label.setText(_translate("MainWindow", "Левая граница"))
        self.trapeze_right_label.setText(_translate("MainWindow", "Правая граница"))
        self.trapeze_min_label.setText(_translate("MainWindow", "Минимум интервалов"))
        self.trapeze_max_label.setText(_translate("MainWindow", "Максимум интервалов"))
        self.trapeze_accuracy_label.setText(_translate("MainWindow", "Точность"))
        self.start_simpson_label.setText(_translate("MainWindow", "Рассчитать"))
        self.simpson_label.setText(_translate("MainWindow", "Метод Симпсона"))
        self.simpson_left_label.setText(_translate("MainWindow", "Левая граница"))
        self.simpson_right_label.setText(_translate("MainWindow", "Правая граница"))
        self.simpson_min_label.setText(_translate("MainWindow", "Минимум интервалов"))
        self.simpson_max_label.setText(_translate("MainWindow", "Максимум интервалов"))
        self.simpson_accuracy_label.setText(_translate("MainWindow", "Точность"))
        self.save.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton.setText(_translate("MainWindow", "Сменить метод"))

    def update_graph(self, a, b):
        delta = abs(b - a) / 100
        values = []
        plots = []
        for i in range(100):
            plots.append(a + i * delta)
            values.append(self.function(a + i * delta))
        self.graph.clear()
        self.graph.plot(plots, values)

    def change_method(self):
        index = self.stackedWidget.currentIndex()
        if index > 1:
            index = 0
        else:
            index = index + 1
        self.stackedWidget.setCurrentIndex(index)

    def simpson_init(self):
        try:
            a = float(self.simpson_left.text())
            b = float(self.simpson_right.text())
            acc = float(self.simpson_accuracy.text())
            min_intervals = float(self.simpson_min.text())
            max_intervals = float(self.simpson_max.text())
            if not validate_params(a, b,min_intervals, max_intervals):
                raise ValueError
            self.error.setText('')
            delta = abs(b - a)
            self.update_graph(a - delta * 0.1, b + delta * 0.1)
            data = imath.simpson(self.function, a, b, acc, min_intervals, max_intervals)
            self.data = data
            model = tablemodel.TableModel(data, ["Sum", "N"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText('Invalid params')
        except imath.RequirementException:
            self.error.setText("Convergence requirements faild")
        except imath.BadParamsExceptions:
            self.error.setText('Invalid params')

    def rect_init(self):
        try:
            a = float(self.rect_left.text())
            b = float(self.rect_right.text())
            acc = float(self.rect_accuracy.text())
            min_intervals = float(self.rect_min.text())
            max_intervals = float(self.rect_max.text())

            if not validate_params(a, b, min_intervals, max_intervals):
                raise ValueError
            self.error.setText('')
            delta = abs(b - a)
            self.update_graph(a - delta * 0.1, b + delta * 0.1)
            if self.rect_type.currentIndex() == 0:
                data = imath.rectangles_left(self.function, a, b, acc, min_intervals, max_intervals)
            elif self.rect_type.currentIndex() == 1:
                data = imath.rectangles_right(self.function, a, b, acc, min_intervals, max_intervals)
            elif self.rect_type.currentIndex() == 2:
                data = imath.rectangles_middle(self.function, a, b, acc, min_intervals, max_intervals)
            self.data = data
            model = tablemodel.TableModel(data, ["Sum", "N"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText('Invalid params')
        except imath.RequirementException:
            self.error.setText("Convergence requirements faild")
        except imath.BadParamsExceptions:
            self.error.setText('Invalid params')


    def trapeze_init(self):
        try:
            a = float(self.trapeze_left.text())
            b = float(self.trapeze_right.text())
            acc = float(self.trapeze_accuracy.text())
            min_intervals = float(self.trapeze_min.text())
            max_intervals = float(self.trapeze_max.text())
            if not validate_params(a, b, min_intervals, max_intervals):
                raise ValueError
            self.error.setText('')
            delta = abs(b - a)
            self.update_graph(a - delta * 0.1, b + delta * 0.1)
            data = imath.trapeze(self.function, a, b, acc, min_intervals, max_intervals)
            self.data = data
            model = tablemodel.TableModel(data, ["Sum", "N"])
            self.table.setModel(model)
            self.table.update()
        except ValueError:
            self.error.setText("Invalid Params")
        except imath.RequirementException:
            self.error.setText("Convergence requirements faild")
        except imath.BadParamsExceptions:
            self.error.setText('Invalid params')


    def save_to_file(self):
        openfile = QtGui.QFileDialog.getOpenFileName(self, 'Open file')[0]
        f = open(openfile, 'w')
        data = self.data
        for d in data:
            f.write(','.join(list(map(str, d))))
        f.close()

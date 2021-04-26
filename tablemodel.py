import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers):
        super(TableModel, self).__init__()
        self._data = data
        self.headers = headers


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QtCore.QVariant(self.headers[col])
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QtCore.QVariant(col+1)
        return QtCore.QVariant()

    def columnCount(self, index):
        return len(self._data[0])

    def getData(self):
        return self._data
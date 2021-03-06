# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionScanFolderRaw = QtWidgets.QAction(MainWindow)
        self.actionScanFolderRaw.setObjectName("actionScanFolderRaw")
        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionIntegrate_over_all = QtWidgets.QAction(MainWindow)
        self.actionIntegrate_over_all.setObjectName("actionIntegrate_over_all")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionPlaceholder = QtWidgets.QAction(MainWindow)
        self.actionPlaceholder.setObjectName("actionPlaceholder")
        self.menuFile.addAction(self.actionPlaceholder)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi-axis motor control"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionPlaceholder.setText(_translate("MainWindow", "Placeholder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

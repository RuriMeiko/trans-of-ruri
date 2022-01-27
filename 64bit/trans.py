#rurimeiko, 7:55 pm


from PyQt5 import QtCore, QtGui, QtWidgets
import logo
from googletrans import Translator
from pygame.mixer import init, music



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(537, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(285, 0, 241, 192))
        self.textEdit1.setObjectName("textEdit1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 200, 47, 13))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 231, 191))
        self.textEdit.setObjectName("textEdit")
        self.buttontrans = QtWidgets.QPushButton(self.centralwidget)
        self.buttontrans.setGeometry(QtCore.QRect(320, 250, 75, 23))
        self.buttontrans.setObjectName("buttontrans")
        self.buttoncopy = QtWidgets.QPushButton(self.centralwidget)
        self.buttoncopy.setGeometry(QtCore.QRect(410, 250, 75, 23))
        self.buttoncopy.setObjectName("buttoncopy")
        self.buttonclear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonclear.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.buttonclear.setObjectName("buttonclear")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 47, 13))
        self.label_2.setObjectName("label_2")
        self.chonngonngu1 = QtWidgets.QComboBox(self.centralwidget)
        self.chonngonngu1.setGeometry(QtCore.QRect(80, 220, 81, 22))
        self.chonngonngu1.setObjectName("chonngonngu1")
        self.chonngonngu1.addItem("a")
        self.chonngonngu1.addItem("V")
        self.chonngonngu1.addItem("n")
        self.chonngonngu1.addItem("auto")
        self.chonngonngu2 = QtWidgets.QComboBox(self.centralwidget)
        self.chonngonngu2.setGeometry(QtCore.QRect(360, 220, 81, 22))
        self.chonngonngu2.setObjectName("chonngonngu2")
        self.chonngonngu2.addItem("v")
        self.chonngonngu2.addItem("a")
        self.chonngonngu2.addItem("n")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        self.menu_more = QtWidgets.QMenu(self.menubar)
        self.menu_more.setObjectName("menu_more")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_Abt = QtWidgets.QAction(MainWindow)
        self.menu_Abt.setObjectName("menu_Abt")
        self.menu_exit = QtWidgets.QAction(MainWindow)
        self.menu_exit.setObjectName("menu_exit")
        self.menu_more.addAction(self.menu_Abt)
        self.menu_more.addSeparator()
        self.menu_more.addAction(self.menu_exit)
        self.menubar.addAction(self.menu_more.menuAction())
        self.textEdit1.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dịch [API Google]"))
        self.label.setText(_translate("MainWindow", "Output"))
        self.buttontrans.setText(_translate("MainWindow", "Dịch"))
        self.buttonclear.setText(_translate("MainWindow", "Xoá tất cả"))
        self.buttoncopy.setText(_translate("MainWindow", "Copy"))
        self.label_2.setText(_translate("MainWindow", "Intput"))
        self.chonngonngu1.setItemText(0, _translate("MainWindow", "Tiếng Anh"))
        self.chonngonngu1.setItemText(1, _translate("MainWindow", "Tiếng Việt"))
        self.chonngonngu1.setItemText(2, _translate("MainWindow", "Tiếng Nhật"))
        self.chonngonngu1.setItemText(3, _translate("MainWindow", "Tự nhận dạng"))
        self.chonngonngu2.setItemText(0, _translate("MainWindow", "Tiếng Việt"))
        self.chonngonngu2.setItemText(1, _translate("MainWindow", "Tiếng Anh"))
        self.chonngonngu2.setItemText(2, _translate("MainWindow", "Tiếng Nhật"))
        self.menu_more.setTitle(_translate("MainWindow", "Thêm"))
        self.menu_Abt.setText(_translate("MainWindow", "About"))
        self.menu_exit.setText(_translate("MainWindow", "Thoát"))
        

    def ifpress(self, MainWindow):
        self.buttonclear.clicked.connect(lambda: self.doaa("c"))
        self.buttontrans.clicked.connect(lambda: self.doaa("t"))
        self.buttoncopy.clicked.connect(lambda: self.doaa("x"))
        self.menu_Abt.triggered.connect(self.showabt)
        self.menu_exit.triggered.connect(self.exitl)
    def ngonngu(self,j,i):
        nn2 = {
            0:"vi",
            1:"en",
            2:"ja",
        }
        nn1 = {
            0:"en",
            1:"vi",
            2:"ja",
            3:"auto",
        }
        if j == 1:
            return nn1.get(i,"null")
        else:
            return nn2.get(i,"null")

    def doaa(self,a):
        print(a)
        if a == "c":
            self.textEdit.clear()
            self.textEdit1.clear()
        if a == "t":
            vanban = self.textEdit.toPlainText()
            self.textEdit1.setPlainText(Translator().translate(vanban,dest=self.ngonngu(0,self.chonngonngu2.currentIndex()),src=self.ngonngu(1,self.chonngonngu1.currentIndex())).text)
        if a == "x":
            self.textEdit1.selectAll()
            self.textEdit1.copy()

    def showabt(self):
        init()
        music.load("song.mp3")
        music.set_volume(30)
        music.play()
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon(':/icons/logo.png'))
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setInformativeText("(੭👁️‸👁️)੭̸*✩⁺˚")
        msg.setText("This app make by rurimeiko")
        msg.setWindowTitle("About")
        msg.exec_()
        music.stop()
    def exitl(self):
        sys.exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ifpress(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

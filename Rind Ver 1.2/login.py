from PyQt5 import QtCore, QtGui, QtWidgets

class Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 555)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 290, 651, 271))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_login = QtWidgets.QPushButton(self.tab)
        self.pushButton_login.setGeometry(QtCore.QRect(190, 150, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit_login_account = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_login_account.setGeometry(QtCore.QRect(190, 40, 261, 41))
        self.lineEdit_login_account.setObjectName("lineEdit_login_account")
        self.lineEdit_login_password = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_login_password.setGeometry(QtCore.QRect(190, 80, 261, 41))
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(120, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_traveller = QtWidgets.QPushButton(self.tab)
        self.pushButton_traveller.setGeometry(QtCore.QRect(480, 40, 93, 28))
        self.pushButton_traveller.setObjectName("pushButton_traveller")
        self.Tip_Login = QtWidgets.QLabel(self.tab)
        self.Tip_Login.setGeometry(QtCore.QRect(470, 170, 131, 21))
        self.Tip_Login.setStyleSheet("color: rgb(255, 0, 0);")
        self.Tip_Login.setText("")
        self.Tip_Login.setObjectName("Tip_Login")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_sign_account = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sign_account.setGeometry(QtCore.QRect(190, 40, 261, 41))
        self.lineEdit_sign_account.setObjectName("lineEdit_sign_account")
        self.lineEdit_sign_password = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sign_password.setGeometry(QtCore.QRect(190, 80, 261, 41))
        self.lineEdit_sign_password.setObjectName("lineEdit_sign_password")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_sign = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_sign.setGeometry(QtCore.QRect(190, 150, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_sign.setFont(font)
        self.pushButton_sign.setObjectName("pushButton_sign")
        self.Tip_Signup = QtWidgets.QLabel(self.tab_2)
        self.Tip_Signup.setGeometry(QtCore.QRect(470, 170, 141, 21))
        self.Tip_Signup.setStyleSheet("color: rgb(255, 0, 0);")
        self.Tip_Signup.setText("")
        self.Tip_Signup.setObjectName("Tip_Signup")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_logo = QtWidgets.QLabel(Dialog)
        self.label_logo.setGeometry(QtCore.QRect(-10, -60, 641, 381))
        self.label_logo.setStyleSheet("image: url(:/new/Logo5.jpg);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.label_logo.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)

        #self.pushButton_login.clicked.connect(Dialog.close)
        self.pushButton_traveller.clicked.connect(Dialog.close)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "瓜皮电影"))
        self.pushButton_login.setText(_translate("Dialog", "登录"))
        self.label_4.setText(_translate("Dialog", "账号"))
        self.label_5.setText(_translate("Dialog", "密码"))
        self.pushButton_traveller.setText(_translate("Dialog", "游客登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "                登录                "))
        self.label_2.setText(_translate("Dialog", "账号"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.pushButton_sign.setText(_translate("Dialog", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "                注册                "))
        self.lineEdit_login_account.setPlaceholderText("请输入账号")
        self.lineEdit_login_password.setPlaceholderText("请输入密码")
        self.lineEdit_sign_account.setPlaceholderText("请输入账号")
        self.lineEdit_sign_password.setPlaceholderText("请输入密码")
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)


import pictures
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QRadioButton
from PyQt5.uic import loadUi
import sys
import re
import DataBaseFunction

DataBaseFunction.createTables1()
DataBaseFunction.createTables2()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('./ui/mainpage.ui', self)
        self.buttons()

    def buttons(self):
        self.signinbutton.clicked.connect(self.ShowSignInPage)
        self.signupbutton.clicked.connect(self.ShowSignUpPage)

    def ShowSignInPage(self):
        window2.show()
        self.close()

    def ShowSignUpPage(self):
        window3.show()
        self.close()

class SignInPage(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('./ui/signinpage.ui', self)
        self.buttons()

    def buttons(self):
        self.backbutton.clicked.connect(self.ShowMainPage)
        self.signinbutton.clicked.connect(self.CheckUser)

    def ShowMainPage(self):
        window1.show()
        self.close()

    def ShowInformationPage(self):
        window4.show()
        self.close()

    def CheckUser(self):
        username = self.usernamelineedit.text()
        password = self.passwordlineedit.text()
        alluser = DataBaseFunction.checkUser()
        if username != '' and password != '':
            for user in alluser:
                if user['name'] == username and user['password'] == password:
                    self.errorlabel.setText('خوش آمدید')
                    self.ShowInformationPage()
                    break
            else:
                self.errorlabel.setText('نام کاربری و رمزعبور اشتباه است')
        else:
            self.errorlabel.setText('نام کاربری و رمزعبور را وارد کنید')

class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('./ui/signupage.ui', self)
        self.buttons()

    def buttons(self):
        self.backbutton.clicked.connect(self.ShowMainPage)
        self.signupbutton.clicked.connect(self.AddUser)

    def ShowMainPage(self):
        window1.show()
        self.close()

    def AddUser(self):
        username = self.usernamelineedit.text()
        password = self.passwordlineedit.text()
        repeat = self.repeatlineedit.text()
        personally = self.personallylineedit.text()
        phone = self.phonelineedit.text()
        alluser = DataBaseFunction.checkUser()
        if username != '' and password != '' and repeat != '' and personally != '' and phone != '':
            if re.fullmatch(r'^(09[0-9]{9})$', phone):
                if len(password) >= 6:
                    if password == repeat:
                        for user in alluser:
                            if user['personally'] == personally:
                                self.errorlabel.setText('این نام کاربری قبلا ثبت شده است')
                                break
                        else:
                            DataBaseFunction.insertUser(username, password, personally, phone)
                            self.errorlabel.setText('حساب کاربری شما با موفقیت ایجاد شد')
                    else:
                        self.errorlabel.setText('رمزعبور با تکرار آن مطابقت ندارد')
                else:
                    self.errorlabel.setText('رمزعبور نباید کمتر از 6 رقم باشد')
            else:
                self.errorlabel.setText('شماره موبایل نادرست است')
        else:
            self.errorlabel.setText('لطفا همه اطلاعات را تکمیل کنید')

class InformationPage(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('./ui/informationpage.ui', self)
        self.buttons()
        self.yearcombobox = QComboBox(self)
        self.yearcombobox.setGeometry(270, 40, 69, 22)
        self.yearcombobox.addItem('')
        self.yearcombobox.addItem('1403')
        self.yearcombobox.addItem('1402')
        self.yearcombobox.addItem('1401')
        self.yearcombobox.addItem('1400')
        self.yearcombobox.addItem('1399')
        self.yearcombobox.addItem('1398')
        self.yearcombobox.addItem('1397')
        self.yearcombobox.addItem('1396')
        self.yearcombobox.activated[str].connect(self.comboboxtest)

        self.classcombobox = QComboBox(self)
        self.classcombobox.setGeometry(270, 190, 69, 22)
        self.classcombobox.addItem('')
        self.classcombobox.addItem('151')
        self.classcombobox.addItem('161')
        self.classcombobox.addItem('171')
        self.classcombobox.addItem('251')
        self.classcombobox.addItem('261')
        self.classcombobox.addItem('271')
        self.classcombobox.addItem('351')
        self.classcombobox.addItem('361')
        self.classcombobox.addItem('371')
        self.classcombobox.activated[str].connect(self.comboboxtest2)

        self.manradiobutton = QRadioButton('مرد', self)
        self.manradiobutton.move(330, 240)
        self.manradiobutton.toggled.connect(self.man)
        self.womanradiobutton = QRadioButton('زن', self)
        self.womanradiobutton.move(250, 240)
        self.womanradiobutton.toggled.connect(self.woman)

    def buttons(self):
        self.backbutton.clicked.connect(self.ShowSignInPage)
        self.addbutton.clicked.connect(self.AddStudent)
        self.removebutton.clicked.connect(self.RemoveStudent)

    def ShowSignInPage(self):
        window2.show()
        self.close()

    def RemoveStudent(self):
        nationalcode = self.codelineedit.text()
        alluser = DataBaseFunction.CheckStudent()
        if nationalcode != '':
            for user in alluser:
                if user['nationalcode'] == nationalcode:
                    DataBaseFunction.RemoveUser(nationalcode)
                    self.errorlabel.setText('کاربر با موفقیت حذف شد')
                    break
            else:
                self.errorlabel.setText('کاربر وجود ندارد')
        else:
            self.errorlabel.setText('لطفا حداقل کد ملی را پر کنید')

    def AddStudent(self):
        academicyear = self.label2.text()
        firstname = self.firstnamelineedit.text()
        lastname = self.lastnamelineedit.text()
        classname = self.label3.text()
        gender = self.label4.text()
        fatherlineedit = self.fatherlineedit.text()
        codelineedit = self.codelineedit.text()
        phonelineedit = self.phonelineedit.text()
        addresslineedit = self.addresslineedit.text()
        alluser = DataBaseFunction.CheckStudent()
        if academicyear != '' and firstname != '' and lastname != '' and classname != '' and gender != '' and fatherlineedit != '' and codelineedit != '' and phonelineedit != '' and addresslineedit != '':
            for user in alluser:
                if user['nationalcode'] == codelineedit:
                    self.errorlabel.setText('این کاربر قبلا ثبت شده است')
                    break
            else:
                DataBaseFunction.AddUser(academicyear, firstname, lastname, classname, gender, fatherlineedit, codelineedit, phonelineedit, addresslineedit)
                self.errorlabel.setText('کاربر شما با موفقیت ثبت شد')
        else:
            self.errorlabel.setText('لطفا همه کادر ها را پر کنید')

    def comboboxtest(self, text):
        self.label2.setText(text)

    def comboboxtest2(self, text):
        self.label3.setText(text)

    def man(self):
        self.label4.setText('مرد')

    def woman(self):
        self.label4.setText('زن')


if __name__ == '__main__':
    global window1, window2, window3, window4
    app = QApplication(sys.argv)
    window1 = Main()
    window2 = SignInPage()
    window3 = SignUpPage()
    window4 = InformationPage()
    window1.show()
    app.exec()
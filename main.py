import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from APP_Design import Ui_MainWindow

# IMPORT FUNCTIONS
from APP_Functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## HOME_MENU MENU
        ########################################################################
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_14))
        # create pop up msg
        self.messageBox = QMessageBox()
        ## PAGES
        ########################################################################
        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        # Functions for page 1
        # MINI PAGE 1
        self.ui.pushButton_6.clicked.connect(
            lambda: UIFunctions.checkIsempty(self, 6))
        UIFunctions.showMiniPage1(self)
        # MINI PAGE 2
        self.ui.pushButton_8.clicked.connect(
            lambda: UIFunctions.checkIsempty(self, 8))
        UIFunctions.showMiniPage2(self)
        # MINI PAGE 3
        self.ui.pushButton_7.clicked.connect(
            lambda: UIFunctions.checkIsempty(self, 7))
        UIFunctions.showMiniPage3(self)
        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # Functions for page 2
        UIFunctions.clicksOnPage2(self)
        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        # Functions for page 3
        UIFunctions.goToMinipage2Page3(self)
        # PAGE 4
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        # functions for page 4 :
        UIFunctions.clickOnCalculateRadiusOfCurvature(self)
        # PAGE 5
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
        # Functions for Page 5
        UIFunctions.page5Connector(self)
        # PAGE 6
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_10))
        # Functions for Page 6
        UIFunctions.page6Connector(self)
        # PAGE 7
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_11))
        # Functions for Page 7
        UIFunctions.page7Connector(self)
        # PAGE 8
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_12))
        # Functions for Page 8
        UIFunctions.page8Connector(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

import ast
import math
import re

import mpmath
from PyQt5.QtWidgets import QMessageBox

from main import *

# Functions for all pages

class UIFunctions(MainWindow):

    # Functions for page 1
    def showMiniPage1(self):
        self.ui.radioButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6))

    def showMiniPage2(self):
        self.ui.radioButton_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5))

    def showMiniPage3(self):
        self.ui.radioButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7))

    def checkIsempty(self, page):
        if page == 6:
            UIFunctions.calculateParamWithaAndb(self)
        elif page == 7:
            UIFunctions.calculateParamWithaAnde(self)
        else:
            UIFunctions.calculateParamWithaAndf(self)

    def calculateParamWithaAndb(self):
        try :
            a = ast.literal_eval(self.ui.lineEdit.text())
            b = ast.literal_eval(self.ui.lineEdit_2.text())
            inv_f = a / (a - b)
            excentricite1 = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(a, 2))
            excentricite2 = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(b, 2))
            excentriciteAngulaire = math.degrees(math.acos(b / a))
            courburePole = (math.pow(a, 2)) / b
            self.ui.lineEdit_7.setText(str("%.4f" % excentricite1))
            self.ui.lineEdit_6.setText(str("%.4f" % inv_f))
            self.ui.lineEdit_3.setText(str("%.4f" % excentricite2))
            self.ui.lineEdit_5.setText(str("%.4f" % excentriciteAngulaire))
            self.ui.lineEdit_4.setText(str("%.4f" % courburePole))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def calculateParamWithaAndf(self):
        try:
            a = ast.literal_eval(self.ui.lineEdit_59.text())
            inv_f = ast.literal_eval(self.ui.lineEdit_61.text())
            f = 1 / inv_f
            b = a * (1 - f)
            excentricite1 = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(a, 2))
            excentricite2 = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(b, 2))
            excentriciteAngulaire = math.acos(b / a)
            courburePole = a * a / b
            self.ui.lineEdit_58.setText(str("%.4f" % excentricite1))
            self.ui.lineEdit_62.setText(str("%.4f" % b))
            self.ui.lineEdit_57.setText(str("%.4f" % excentricite2))
            self.ui.lineEdit_60.setText(str("%.4f" % excentriciteAngulaire))
            self.ui.lineEdit_63.setText(str("%.4f" % courburePole))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def calculateParamWithaAnde(self):
        try:
            a = ast.literal_eval(self.ui.lineEdit_66.text())
            e_carre = ast.literal_eval(self.ui.lineEdit_68.text())
            b = math.sqrt(math.pow(a, 2) * (1 - e_carre))
            inv_f = a / (a - b)
            excentricite2 = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(b, 2))
            excentriciteAngulaire = math.acos(b / a)
            courburePole = (math.pow(a, 2)) / b
            self.ui.lineEdit_65.setText(str("%.4f" % inv_f))
            self.ui.lineEdit_69.setText(str("%.4f" % b))
            self.ui.lineEdit_64.setText(str("%.4f" % excentricite2))
            self.ui.lineEdit_67.setText(str("%.4f" % excentriciteAngulaire))
            self.ui.lineEdit_70.setText(str("%.4f" % courburePole))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    # Functions for page 2
    def clicksOnPage2(self):
        self.ui.pushButton_11.clicked.connect(lambda: UIFunctions.checkOnPage2andGoto(self))

    def checkOnPage2andGoto(self):
        try :
            self.a = ast.literal_eval(self.ui.lineEdit_72.text())
            self.invf = ast.literal_eval(self.ui.lineEdit_71.text())
            self.ui.pushButton_10.setHidden(False)
            self.ui.pushButton_9.setHidden(False)
            UIFunctions.clickedOnPage(self)
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def clickedOnPage(self):
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_12.clicked.connect(lambda: UIFunctions.transformeGeographicToCartesian(self))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_13))
        self.ui.pushButton_13.clicked.connect(lambda: UIFunctions.transformeCartesianToGeographic(self))
        self.ui.pushButton_74.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page))
        self.ui.pushButton_73.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page))

    def transformeGeographicToCartesian(self):
        try :
            self.ui.pushButton_11.setHidden(True)
            if(float(self.ui.lineEdit_82.text()) < 0) :
                phi = - ( math.fabs(ast.literal_eval(self.ui.lineEdit_82.text()) )+ ast.literal_eval(
                    self.ui.lineEdit_83.text()) / 60 + ast.literal_eval(self.ui.lineEdit_81.text()) / 3600)
            else :
                phi = ast.literal_eval(self.ui.lineEdit_82.text()) + ast.literal_eval(
                self.ui.lineEdit_83.text()) / 60 + ast.literal_eval(self.ui.lineEdit_81.text()) / 3600
            if (float(self.ui.lineEdit_74.text()) < 0) :
                landa = - (math.fabs(ast.literal_eval(self.ui.lineEdit_74.text())) + ast.literal_eval(
                    self.ui.lineEdit_79.text()) / 60 + ast.literal_eval(self.ui.lineEdit_80.text()) / 3600)
            else :
                landa = ast.literal_eval(self.ui.lineEdit_74.text()) + ast.literal_eval(
                    self.ui.lineEdit_79.text()) / 60 + ast.literal_eval(self.ui.lineEdit_80.text()) / 3600
            h = ast.literal_eval(self.ui.lineEdit_75.text())
            f = 1 / self.invf
            b = self.a * (1 - f)
            e = ((math.pow(self.a, 2)) - (math.pow(b, 2))) / (math.pow(self.a, 2))
            N = self.a / (math.sqrt(1 - e * math.pow(math.sin(math.radians(phi)), 2)))
            X = (N + h) * math.cos(math.radians(landa)) * math.cos(math.radians(phi))
            Y = (N + h) * math.sin(math.radians(landa)) * math.cos(math.radians(phi))
            Z = (N * (1 - e) + h) * math.sin(math.radians(phi))
            self.ui.lineEdit_77.setText(str("%.4f" % X))
            self.ui.lineEdit_76.setText(str("%.4f" % Y))
            self.ui.lineEdit_78.setText(str("%.4f" % Z))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def transformeCartesianToGeographic(self):
        try:
            f = 1 / self.invf
            b = self.a * (1 - f)
            e = ((math.pow(self.a, 2)) - (math.pow(b, 2))) / (math.pow(self.a, 2))
            X = ast.literal_eval(self.ui.lineEdit_92.text())
            Y = ast.literal_eval(self.ui.lineEdit_93.text())
            Z = ast.literal_eval(self.ui.lineEdit_91.text())
            landa = math.degrees(math.atan(Y / X))
            phi0 = math.degrees(math.atan(Z / math.sqrt(math.pow(X, 2) + math.pow(Y, 2))))
            N0 = self.a / math.sqrt(1 - e * math.degrees(math.pow(math.sin(math.radians(phi0)), 2)))
            H0 = (math.sqrt(math.pow(X, 2) + math.pow(Y, 2)) / (math.cos(math.radians(phi0)))) - N0
            while True:
                phi = math.degrees(
                    math.atan((Z / math.sqrt((math.pow(X, 2) + math.pow(Y, 2)))) * 1 / (1 - e * (N0 / (N0 + H0)))))
                N = self.a / math.sqrt(1 - e * math.pow(math.sin(math.radians(phi)), 2))
                H = math.sqrt(math.pow(X, 2) + math.pow(Y, 2)) / (math.cos(math.radians(phi))) - N
                if abs((phi - phi0) / phi) < 0.0001 * math.pow(10, -4):
                    break
                else:
                    phi0 = phi
                    H0 = H
                    N0 = N
            landa = UIFunctions.degdecimal2dms(landa)
            phi = UIFunctions.degdecimal2dms(phi)
            self.ui.lineEdit_90.setText(str("%.f" % landa[0]))
            self.ui.lineEdit_88.setText(str("%.f" % landa[1]))
            self.ui.lineEdit_89.setText(str("%.4f" % landa[2]))
            self.ui.lineEdit_86.setText(str("%.f" % phi[0]))
            self.ui.lineEdit_84.setText(str("%.f" % phi[1]))
            self.ui.lineEdit_85.setText(str("%.4f" % phi[2]))
            self.ui.lineEdit_87.setText(str("%.4f" % H))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def degdecimal2dms(dd):
        is_positive = dd >= 0
        dd = abs(dd)
        minutes, seconds = divmod(dd * 3600, 60)
        degrees, minutes = divmod(minutes, 60)
        degrees = degrees if is_positive else -degrees
        return (degrees, minutes, seconds)

    def goToMinipage2Page3(self):
        self.ui.pushButton_14.clicked.connect(lambda: UIFunctions.checkEditLineAndClickBtn(self))

    def checkEditLineAndClickBtn(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_16)
        UIFunctions.radioButtonClicked(self)

    def radioButtonClicked(self):
        self.ui.radioButton_4.clicked.connect(lambda: UIFunctions.clearEditLines(self, self.ui.radioButton_4))
        self.ui.radioButton_5.clicked.connect(lambda: UIFunctions.clearEditLines(self, self.ui.radioButton_5))
        self.ui.radioButton_6.clicked.connect(lambda: UIFunctions.clearEditLines(self, self.ui.radioButton_6))
        self.ui.pushButton_16.clicked.connect(lambda: UIFunctions.calculateLatitudes(self))
        self.ui.pushButton_75.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_15))

    def clearEditLines(self, radioBtn):
        if radioBtn.objectName() == "radioButton_4":
            self.ui.lineEdit_99.setEnabled(True)
            self.ui.lineEdit_96.setEnabled(False)
            self.ui.lineEdit_97.setEnabled(False)
            self.ui.lineEdit_99.setText("")
            self.ui.lineEdit_96.setText("")
            self.ui.lineEdit_97.setText("")
        elif radioBtn.objectName() == "radioButton_5":
            self.ui.lineEdit_96.setEnabled(True)
            self.ui.lineEdit_99.setEnabled(False)
            self.ui.lineEdit_97.setEnabled(False)
            self.ui.lineEdit_99.setText("")
            self.ui.lineEdit_96.setText("")
            self.ui.lineEdit_97.setText("")
        else:
            self.ui.lineEdit_97.setEnabled(True)
            self.ui.lineEdit_99.setEnabled(False)
            self.ui.lineEdit_96.setEnabled(False)
            self.ui.lineEdit_99.setText("")
            self.ui.lineEdit_96.setText("")
            self.ui.lineEdit_97.setText("")

    def calculateLatitudes(self):
        try :
            a = ast.literal_eval(self.ui.lineEdit_73.text())
            b = ast.literal_eval(self.ui.lineEdit_94.text())
            if self.ui.lineEdit_99.text() != "":
                phi = ast.literal_eval(self.ui.lineEdit_99.text())
                beta = math.degrees( math.atan( math.tan( math.radians(phi) ) * (b / a) ))
                psi = math.degrees(math.atan(  ( math.pow(b, 2) / math.pow(a, 2)   ) * math.tan( math.radians(phi) )   ) )
                self.ui.lineEdit_97.setText(str("%.4f" % beta))
                self.ui.lineEdit_96.setText(str("%.4f" % psi))
            elif self.ui.lineEdit_96.text() != "":
                psi = ast.literal_eval(self.ui.lineEdit_96.text())
                beta = math.degrees(math.atan((a / b) * math.tan(math.radians(psi))))
                phi = math.degrees(math.atan((math.pow(a, 2) / math.pow(b, 2)) * math.tan(math.radians(psi))))
                self.ui.lineEdit_97.setText(str("%.4f" % beta))
                self.ui.lineEdit_99.setText(str("%.4f" % phi))
            else:
                beta = ast.literal_eval(self.ui.lineEdit_97.text())
                phi = math.degrees(math.atan((a / b) * math.tan(math.radians(beta))))
                psi = math.degrees(math.atan((b / a) * math.tan(math.radians(beta))))
                self.ui.lineEdit_96.setText(str("%.4f" % psi))
                self.ui.lineEdit_99.setText(str("%.4f" % phi))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def clickOnCalculateRadiusOfCurvature(self):
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_18))
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_19))
        self.ui.pushButton_15.clicked.connect(lambda: UIFunctions.calculateRadiusOfCurvature(self))
        self.ui.pushButton_19.clicked.connect(lambda: UIFunctions.calculateRadiusOfCurvatureAlpha(self))
        self.ui.pushButton_21.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_17))
        self.ui.pushButton_20.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_17))

    def calculateRadiusOfCurvature(self):
        try :
            self.ui.pushButton_20.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_17))
            # get input and then calculate curvature
            phi = ast.literal_eval(self.ui.lineEdit_100.text()) + ast.literal_eval(
                self.ui.lineEdit_98.text()) / 60 + ast.literal_eval(self.ui.lineEdit_95.text()) / 3600
            a = ast.literal_eval(self.ui.lineEdit_102.text())
            b = ast.literal_eval(self.ui.lineEdit_101.text())
            e = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(a, 2))
            curvatureMeridian = (a * (1 - e)) / math.pow( (1 - e * math.pow(math.sin(math.radians(phi)), 2)), 3 / 2 )
            curvature1erVertical = a / math.sqrt( 1 - ( e * math.pow( math.sin( math.radians(phi) ), 2 )) )
            self.ui.lineEdit_103.setText(str("%.4f" % curvatureMeridian))
            self.ui.lineEdit_104.setText(str("%.4f" % curvature1erVertical))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def calculateRadiusOfCurvatureAlpha(self):
        try :
            phi = ast.literal_eval(self.ui.lineEdit_109.text()) + ast.literal_eval(
                self.ui.lineEdit_107.text()) / 60 + ast.literal_eval(self.ui.lineEdit_108.text()) / 3600
            alpha = ast.literal_eval(self.ui.lineEdit_106.text())
            a = ast.literal_eval(self.ui.lineEdit_110.text())
            b = ast.literal_eval(self.ui.lineEdit_111.text())
            e = ((math.pow(a, 2)) - (math.pow(b, 2))) / (math.pow(a, 2))
            curvatureMeridian = (a * (1 - e)) / math.pow((1 - e * math.pow(math.sin(math.radians(phi)), 2)), 3 / 2)
            curvature1erVertical = a / math.sqrt(1 - e * math.pow(math.sin(math.radians(phi)), 2))
            rAlpha = (curvatureMeridian * curvature1erVertical) / (
                    curvatureMeridian * math.pow(math.sin(math.radians(alpha)),
                                                 2) + curvature1erVertical *
                math.pow(math.cos(math.radians(alpha)), 2))
            self.ui.lineEdit_105.setText(str("%.4f" % rAlpha))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def page5Connector(self):
        self.ui.pushButton_24.clicked.connect(lambda: UIFunctions.calculateLongeurArc(self))
        self.ui.pushButton_22.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_21))
        self.ui.pushButton_23.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_23))
        self.ui.pushButton_28.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_22))
        self.ui.pushButton_25.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_20))
        self.ui.pushButton_26.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_20))
        self.ui.pushButton_29.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_20))
        self.ui.pushButton_30.clicked.connect(lambda: UIFunctions.calculateLongeurArcPhi1EtPhi2(self))
        self.ui.pushButton_27.clicked.connect(lambda: UIFunctions.calculateLongeurArcParallele(self))

    def calculateLongeurArc(self):
        try :
            phi = math.radians(ast.literal_eval(self.ui.lineEdit_115.text()) + ast.literal_eval(
                self.ui.lineEdit_117.text()) / 60 + ast.literal_eval(self.ui.lineEdit_118.text()) / 3600)
            a = ast.literal_eval(self.ui.lineEdit_114.text())
            e = math.sqrt(ast.literal_eval(self.ui.lineEdit_116.text()))
            A = 1 + (3 / 4) * e ** 2 + (45 / 64) * e ** 4 + (175 / 256) * e ** 6 + (11025 / 16348) * e ** 8 + (
                    43659 / 65536) * e ** 10
            B = (3 / 4) * e ** 2 + (15 / 16) * e ** 4 + (525 / 512) * e ** 6 + (2205 / 2048) * e ** 8 + (
                    72765 / 65536) * e ** 10
            C = (15 / 16) * e ** 4 + (105 / 256) * e ** 6 + (2205 / 4096) * e ** 8 + (10395 / 16348) * e ** 10
            D = (35 / 512) * e ** 6 + (315 / 2048) * e ** 8 + (31185 / 131072) * e ** 10
            E = (315 / 16384) * e ** 8 + (3465 / 65536) * e ** 10;
            F = (639 / 131072) * e ** 10
            alpha = A * a * (1 - e ** 2)
            beta = (B / 2) * a * (1 - e ** 2)
            gamma = (C / 4) * a * (1 - e ** 2)
            delta = (D / 6) * a * (1 - e ** 2)
            epsilon = (E / 8) * a * (1 - e ** 2)
            mu = (F / 10) * a * (1 - e ** 2)
            S = alpha * phi - beta * math.sin(2 * phi) + gamma * math.sin(4 * phi) - delta * math.sin(
                6 * phi) + epsilon * math.sin(8 * phi) - mu * math.sin(10 * phi)
            SenKm = (S) / 1000
            self.ui.lineEdit_112.setText(str("%.4f" % SenKm))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def calculateLongeurArcPhi1EtPhi2(self):
        try :
            phi1 = math.radians(ast.literal_eval(self.ui.lineEdit_135.text()) + ast.literal_eval(
                self.ui.lineEdit_138.text()) / 60 + ast.literal_eval(self.ui.lineEdit_137.text()) / 3600)
            phi2 = math.radians(ast.literal_eval(self.ui.lineEdit_132.text()) + ast.literal_eval(
                self.ui.lineEdit_131.text()) / 60 + ast.literal_eval(self.ui.lineEdit_139.text()) / 3600)
            a = ast.literal_eval(self.ui.lineEdit_136.text())
            e = math.sqrt(ast.literal_eval(self.ui.lineEdit_134.text()))
            A = 1 + (3 / 4) * e ** 2 + (45 / 64) * e ** 4 + (175 / 256) * e ** 6 + (11025 / 16348) * e ** 8 + (
                    43659 / 65536) * e ** 10
            B = (3 / 4) * e ** 2 + (15 / 16) * e ** 4 + (525 / 512) * e ** 6 + (2205 / 2048) * e ** 8 + (
                    72765 / 65536) * e ** 10
            C = (15 / 16) * e ** 4 + (105 / 256) * e ** 6 + (2205 / 4096) * e ** 8 + (10395 / 16348) * e ** 10
            D = (35 / 512) * e ** 6 + (315 / 2048) * e ** 8 + (31185 / 131072) * e ** 10
            E = (315 / 16384) * e ** 8 + (3465 / 65536) * e ** 10;
            F = (639 / 131072) * e ** 10
            alpha = A * a * (1 - e ** 2)
            beta = (B / 2) * a * (1 - e ** 2)
            gamma = (C / 4) * a * (1 - e ** 2)
            delta = (D / 6) * a * (1 - e ** 2)
            epsilon = (E / 8) * a * (1 - e ** 2)
            mu = (F / 10) * a * (1 - e ** 2)
            S1 = alpha * phi1 - beta * math.sin(2 * phi1) + gamma * math.sin(4 * phi1) - delta * math.sin(
                6 * phi1) + epsilon * math.sin(8 * phi1) - mu * math.sin(10 * phi1)
            S2 = alpha * phi2 - beta * math.sin(2 * phi2) + gamma * math.sin(4 * phi2) - delta * math.sin(
                6 * phi2) + epsilon * math.sin(8 * phi2) - mu * math.sin(10 * phi2)
            SenKm = (S2 - S1) / 1000
            self.ui.lineEdit_133.setText(str("%.4f" % SenKm))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def calculateLongeurArcParallele(self):
       try :
            phi = math.radians(ast.literal_eval(self.ui.lineEdit_122.text()) + ast.literal_eval(
                self.ui.lineEdit_120.text()) / 60 + ast.literal_eval(self.ui.lineEdit_121.text()) / 3600)
            lambda1 = math.radians(ast.literal_eval(self.ui.lineEdit_127.text()) + ast.literal_eval(
                self.ui.lineEdit_126.text()) / 60 + ast.literal_eval(self.ui.lineEdit_125.text()) / 3600)
            lambda2 = math.radians(ast.literal_eval(self.ui.lineEdit_130.text()) + ast.literal_eval(
                self.ui.lineEdit_129.text()) / 60 + ast.literal_eval(self.ui.lineEdit_128.text()) / 3600)
            a = ast.literal_eval(self.ui.lineEdit_123.text())
            e = (ast.literal_eval(self.ui.lineEdit_124.text()))
            L = (lambda2 - lambda1) * math.cos(phi) * (a / (1 - e * (math.sin(phi) ** 2)))
            lEnKm = L / 1000
            self.ui.lineEdit_119.setText(str("%.4f" % lEnKm))
       except Exception:
           UIFunctions.errorMsg(self, "Erreur\nressayer une autre fois ")

    def page6Connector(self):
        self.ui.pushButton_40.clicked.connect(lambda: UIFunctions.calculateSurface(self))

    def calculateSurface(self):
        try :
            def f(x):
                return (math.sin(x) + ((2 / 3) * (e ** 2) * (math.sin(x) ** 3)) + (
                        (3 / 5) * (e ** 4) * (math.sin(x) ** 5)) + ((4 / 7) * (e ** 6) * (math.sin(x) ** 7)))

            phi1 = math.radians(ast.literal_eval(self.ui.lineEdit_169.text()) + ast.literal_eval(
                self.ui.lineEdit_173.text()) / 60 + ast.literal_eval(self.ui.lineEdit_172.text()) / 3600)
            phi2 = math.radians(ast.literal_eval(self.ui.lineEdit_168.text()) + ast.literal_eval(
                self.ui.lineEdit_171.text()) / 60 + ast.literal_eval(self.ui.lineEdit_166.text()) / 3600)
            lambda1 = math.radians(ast.literal_eval(self.ui.lineEdit_176.text()) + ast.literal_eval(
                self.ui.lineEdit_177.text()) / 60 + ast.literal_eval(self.ui.lineEdit_175.text()) / 3600)
            lambda2 = math.radians(ast.literal_eval(self.ui.lineEdit_179.text()) + ast.literal_eval(
                self.ui.lineEdit_180.text()) / 60 + ast.literal_eval(self.ui.lineEdit_178.text()) / 3600)
            a = ast.literal_eval(self.ui.lineEdit_167.text())
            e = math.sqrt(ast.literal_eval(self.ui.lineEdit_170.text()))
            b = math.sqrt(math.pow(a, 2) * (1 - e**2))
            Z = ((b ** 2) * (lambda2 - lambda1) * (f(phi2) - f(phi1)))
            ZenKm = Z/(10**6)
            self.ui.lineEdit_174.setText(str("%.4f" % ZenKm))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def page7Connector(self):
        self.ui.pushButton_41.clicked.connect(lambda: UIFunctions.calculateDirecteProblem(self))

    def calculateDirecteProblem(self):
        try:
            a = 6378249.2
            b = 6356515
            R = (2 * a + b) / 3

            phi1 = math.radians(ast.literal_eval(self.ui.lineEdit_184.text()) + ast.literal_eval(
                self.ui.lineEdit_185.text()) / 60 + ast.literal_eval(self.ui.lineEdit_182.text()) / 3600)
            lambda1 = math.radians(ast.literal_eval(self.ui.lineEdit_186.text()) + ast.literal_eval(
                self.ui.lineEdit_181.text()) / 60 + ast.literal_eval(self.ui.lineEdit_183.text()) / 3600)
            azimut = math.radians(ast.literal_eval(self.ui.lineEdit_190.text()) + ast.literal_eval(
                self.ui.lineEdit_187.text()) / 60 + ast.literal_eval(self.ui.lineEdit_189.text()) / 3600)
            distanceD12 = (ast.literal_eval(self.ui.lineEdit_188.text()))/R

            phi2 = math.degrees(math.asin(
                (math.sin(phi1)) * (math.cos(distanceD12)) + (math.cos(phi1)) * (math.sin(distanceD12)) * (
                    math.cos(azimut))))
            lambda2 =(math.degrees(lambda1)) + (math.degrees(mpmath.acot(((mpmath.cot(distanceD12)) * math.sin(
                ((math.pi / 2) - phi1)) - (math.cos((math.pi / 2) - phi1)) * math.cos(azimut)) * (1 / (math.sin(azimut))))))
            azimutRetour = math.degrees(mpmath.acot(
                ( (math.cos(distanceD12)) * (math.cos(azimut)) - (math.tan(phi1)) * (math.sin(distanceD12)) ) * (1 / (math.sin(azimut))) ))
            phi2 = UIFunctions.degdecimal2dms(phi2)
            lambda2 = UIFunctions.degdecimal2dms(lambda2)
            azimutRetour = UIFunctions.degdecimal2dms(azimutRetour)
            self.ui.lineEdit_192.setText(str("%.f" % phi2[0]))
            self.ui.lineEdit_198.setText(str("%.f" % phi2[1]))
            self.ui.lineEdit_191.setText(str("%.4f" % phi2[2]))

            self.ui.lineEdit_197.setText(str("%.f" % lambda2[0]))
            self.ui.lineEdit_199.setText(str("%.f" % lambda2[1]))
            self.ui.lineEdit_194.setText(str("%.4f" % lambda2[2]))

            self.ui.lineEdit_195.setText(str("%.f" % azimutRetour[0]))
            self.ui.lineEdit_196.setText(str("%.f" % azimutRetour[1]))
            self.ui.lineEdit_193.setText(str("%.4f" % azimutRetour[2]))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def page8Connector(self):
        self.ui.pushButton_97.clicked.connect(lambda: UIFunctions.calculateInverseProblem(self))

    def calculateInverseProblem(self):
        try :
            phi1 = math.radians(ast.literal_eval(self.ui.lineEdit_389.text()) + ast.literal_eval(
            self.ui.lineEdit_390.text()) / 60 + ast.literal_eval(self.ui.lineEdit_387.text()) / 3600)
            lambda1 = math.radians(ast.literal_eval(self.ui.lineEdit_391.text()) + ast.literal_eval(
            self.ui.lineEdit_386.text()) / 60 + ast.literal_eval(self.ui.lineEdit_388.text()) / 3600)
            phi2 = math.radians(ast.literal_eval(self.ui.lineEdit_402.text()) + ast.literal_eval(
            self.ui.lineEdit_400.text()) / 60 + ast.literal_eval(self.ui.lineEdit_403.text()) / 3600)
            lambda2 = math.radians(ast.literal_eval(self.ui.lineEdit_399.text()) + ast.literal_eval(
            self.ui.lineEdit_404.text()) / 60 + ast.literal_eval(self.ui.lineEdit_401.text()) / 3600)

            a = 6378249.2
            b= 6356515
            R = (2*a+b)/3

            deltaLambda = lambda2 - lambda1
            distanceD12 = math.acos( (math.sin(phi1)) * (math.sin(phi2)) + (math.cos(phi1)) * (math.cos(phi2)) * (math.cos(deltaLambda) ) )
            distanceD12 = R * distanceD12
            azimutDepart = math.degrees( mpmath.acot(
                ( ( (math.tan(phi2)) * math.cos(phi1) ) / math.sin(deltaLambda)) -
            ((math.sin(phi1)) * (mpmath.cot(deltaLambda))) ) )
            azimutArrive = math.degrees(  mpmath.acot( - ( ( (math.tan(phi1)) * math.cos(phi2) ) / (math.sin(deltaLambda)) -
            ( (math.sin(phi2)) * (mpmath.cot(deltaLambda) ) ) ) ) )
            azimutDepart = UIFunctions.degdecimal2dms(azimutDepart)
            azimutArrive = UIFunctions.degdecimal2dms(azimutArrive)
            self.ui.lineEdit_393.setText(str("%.4f" % distanceD12))
            self.ui.lineEdit_395.setText(str("%.f" % azimutDepart[0]))
            self.ui.lineEdit_392.setText(str("%.f" % azimutDepart[1]))
            self.ui.lineEdit_394.setText(str("%.4f" % azimutDepart[2]))
            self.ui.lineEdit_398.setText(str("%.f" % azimutArrive[0]))
            self.ui.lineEdit_396.setText(str("%.f" % azimutArrive[1]))
            self.ui.lineEdit_397.setText(str("%.4f" % azimutArrive[2]))
        except Exception :
            UIFunctions.errorMsg(self,"Erreur\nressayer une autre fois ")

    def errorMsg(self, string):
        self.messageBox.setWindowTitle("Erreur input!")
        self.messageBox.setIcon(QMessageBox.Critical)
        self.messageBox.setText(string)
        self.messageBox.show()

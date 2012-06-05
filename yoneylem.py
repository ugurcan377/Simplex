# -*- coding: utf-8 -*-
import sys
import time
from copy import deepcopy
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_yoneylem import Ui_MainWindow
from ui_yoneylem2 import Ui_MainWindow as TableWindow
from ui_kisit import Ui_Dialog

class OtherWindow(QtGui.QMainWindow,TableWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

class ConDialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.table = OtherWindow()
        self.constraint = ConDialog()
        self.smatrix = []
        self.results = []
        self.conname = []
        self.conchange = []
        self.coneq = []
        self.conres = []
        self.eqprofit = []
        self.varname = []
        self.varcount = 0
        self.concount = 0
        self.scount =  0
        self.current = 0
        self.buttonCon.setVisible(False)
        self.profit.setToolTip(u"Kisit ekleyebilmek için denklemi yazdıktan sonra Enter'a basin")
        self.profit.returnPressed.connect(self.setVariables)
        self.buttonCon.clicked.connect(self.openDialog)
        self.button_enter.clicked.connect(self.generate)
        self.table.buttonPrev.clicked.connect(self.Prev)
        self.table.buttonNext.clicked.connect(self.Next)
        self.table.buttonFinish.clicked.connect(self.Result)
        self.constraint.buttonAdd.clicked.connect(self.addConstraint)
    
    def setUi(self):
        self.table.buttonPrev.setVisible(True)
        self.table.buttonNext.setVisible(True)
        self.table.buttonFinish.setVisible(False)
        if self.current == 0:
            self.table.buttonPrev.setVisible(False)
        if self.current == self.scount: 
            self.table.buttonNext.setVisible(False)
            self.table.buttonFinish.setVisible(True)
    def Prev(self):
        self.current-=1
        self.setUi()
        self.Paint()
    def Next(self):
        self.current+=1
        self.setUi()
        self.Paint()
    def Result(self):
        tres = "Maksimum Kar = " + str(self.smatrix[self.varcount][-1])
        self.table.labelResult.setText(tres)
    def Paint(self): 
        de = [str(x) for x in self.conchange[self.current]]
        temp1 = "\n\n".join(de)
        temp1 += "\n\nzj\n\ncj-zj"
        self.table.labelLeft.setText(temp1)
        temp = self.results[self.current]
        stemp = ""
        for l in temp:
            ada = [round(x,2) for x in l]
            stemp+="\t".join([str(x) for x in ada])
            stemp+="\n\n"
        self.table.label.setText(stemp)

    def openDialog(self):
        self.constraint.show()
        self.constraint.conNumber.setText("Kisit %d" %(self.concount+1))

    def addConstraint(self):
        #Once denklemleri ve sonuclari ayri ayri kaydet 
        self.concount+=1
        temp = ""
        temp = self.constraint.conEq.text()
        temp = temp.split("+")
        te=[]
        for l in temp:
         #   if (l[1:] in self.varname):
            if (str(l[1]).isdigit()):
                te.append(int(l[0:2]))
            else:
                te.append(int(l[0]))
        self.coneq.append(te)
        self.conres.append(int(self.constraint.conRes.text()))
        self.constraint.close()
        self.constraint.conNumber.setText("")
        self.constraint.conEq.setText("")
        self.constraint.conRes.setText("")

    def setVariables(self): 
        self.entry = self.profit.text()
        self.entry = self.entry.split("+")
        self.varcount = self.entry.__len__()
        for l in self.entry:
            if (str(l[1]).isdigit()):
                self.eqprofit.append(int(l[0:2]))
                self.varname.append(l[2:])
            else:
                self.eqprofit.append(int(l[0]))
                self.varname.append(l[1:])
        self.finished = False
        self.buttonCon.setVisible(True)

    def check(self):
        c = False
        v = 0
        for i in self.smatrix[-1]:
            if i>0:
                v=1
        if v==0:
            c=True
        return c

    def generate(self):
        t1 = ["S%s"%(x) for x in range(1,self.concount+1)]
#Araya SLeri ve sonucu ekleyen bir dongu yaz
        self.varname.extend(t1)
        self.varname.append("Miktar")
        t = [0 for x in range(self.concount)]
        self.eqprofit.extend(t)
        self.conname = deepcopy(t1)
        print self.varname
        print self.coneq
        print self.conres
        print self.concount
        for i in range(self.concount):
            temp = deepcopy(t)
            temp[i]=1
            self.coneq[i].extend(temp)
            self.coneq[i].append(self.conres[i])
            self.smatrix.append([x for x in self.coneq[i]])

        self.smatrix.append([0 for x in range(self.eqprofit.__len__()+1)])
        self.smatrix.append([x for x in self.eqprofit])
        self.finished = self.check()
        self.cj = []
        self.results.append(deepcopy(self.smatrix))
        self.conchange.append(deepcopy(self.conname))
        for i in self.smatrix:
            print i
        while(not self.finished):
            if (self.scount > 100):
               reply = QtGui.QMessageBox.question(self, 'Hata',
                           u"Tablo Hesaplanamıyor",QtGui.QMessageBox.Ok)
               if reply == QtGui.QMessageBox.Ok:
                   sys.exit(app.exec_())

            self.scount+=1
            #print "Debug Adim %d" %(self.scount)
            ch = 100
            ch_index = -1
            opcolon = -1
            chcol = -100
            total = 0
            for i in range(self.eqprofit.__len__()):
                d = self.smatrix[-1][i]
                if d > chcol:
                    chcol = d
                    opcolon = i
            for i in range(self.concount):
                try:
                    d = self.smatrix[i][-1] / self.smatrix[i][opcolon]
                except ZeroDivisionError:
                    d = 150
                if d < ch:
                    ch = d
                    ch_index = i
            #print "OPCOLON = %d CH_INDEX = %d CH = %d"%(opcolon,ch_index,ch)
            self.cj.append(opcolon)
            self.smatrix[ch_index]=[x/float(self.smatrix[ch_index][opcolon]) for x in self.smatrix[ch_index]]
            for i in range(self.concount):
                if (i != ch_index): 
                    factor = self.smatrix[i][opcolon]
                    for j in range(self.smatrix[0].__len__()):
                        self.smatrix[i][j] = self.smatrix[i][j] - (factor * self.smatrix[ch_index][j])
            for i in range(self.eqprofit.__len__()):
                rsum = 0
                for j in self.cj:
                    rsum += self.eqprofit[j] * self.smatrix[j][i]
                self.smatrix[self.concount][i] = rsum
            #print self.eqprofit
            for j in self.cj:
                total+= self.eqprofit[j] * self.smatrix[j][-1]
            #print total
            self.smatrix[self.concount][-1] = total
            for i in range(self.eqprofit.__len__()):
                self.smatrix[-1][i] = self.eqprofit[i] - self.smatrix[self.varcount][i] 
            self.finished = self.check()
            self.results.append(deepcopy(self.smatrix))
            self.conname[ch_index] = self.varname[opcolon]
            self.conchange.append(deepcopy(self.conname))
            #for s in self.smatrix:
            #   print s
        self.table.show()
        test = [str(x) for x in self.varname]
        temp = "\t".join(test)
        self.table.labelUp.setText(temp)
        self.current = 0
        self.setUi()
        self.Paint()


app = QtGui.QApplication(sys.argv)
run = MainWindow()
run.show()
sys.exit(app.exec_())


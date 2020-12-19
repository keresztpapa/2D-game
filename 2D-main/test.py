#hogy ne kelljen kipróbáláshoz létrehozni mindeig külön filet, ennek a tartalma nem számit
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
import sys
import constans
import popups

app = QApplication(sys.argv)
ex = popups.App(constans.WIN_X,constans.WIN_Y,300,200)

print(ex)

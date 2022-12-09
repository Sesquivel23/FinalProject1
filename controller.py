import csv

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

voters_dict = {
    'Voter ID:': ['Candidate:']
}


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_Vote.clicked.connect(lambda: self.vote())
        self.pushButton_Exit.clicked.connect(lambda: self.exit())

    def vote(self):
        for item in voters_dict:
            voterID = self.input_voterID.text()
            candidate = [0]

        self.label_output.setText('Type in Voter ID and select candidate')
        self.input_voterID.setText('')

        if self.radioButton_John.isChecked():
            self.label_output.setText(f"{voterID}'s vote for John is recorded")
            candidate = 'John'

        if self.radioButton_Jane.isChecked():
            self.label_output.setText(f"{voterID}'s vote for Jane is recorded")
            candidate = 'Jane'

        with open('voters.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            line = str(voterID), str(candidate)
            writer.writerow(line)
            # if voterID in open('voters.csv').read():
            #     self.label_output.setText('Voter ID already registered. Please enter new Voter ID')
            #     self.input_voterID.setText('')
            # else:
            #     pass

    def exit(self):
        message = QMessageBox()
        message.setWindowTitle('Window Close')
        message.setText('Are you sure you want to close the window?')
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Yes)
        message.setDefaultButton(QMessageBox.No)

        x = message.exec_()

        self.close()

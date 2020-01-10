import sys

import psycopg2
from Main_Form import Ui_Form
from PyQt5 import QtWidgets


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton_TestSQL.clicked.connect(self.btnClicked)

    def btnClicked(self):
        self.ui.label_Hello.setText("Вы нажали на кнопку!")
        # Если не использовать, то часть текста исчезнет.
        self.ui.label_Hello.adjustSize()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
conn = psycopg2.connect(host="localhost", port="5432", database="TFOMS_BASE", user="postgres", password="root60009")
try:
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Patients"')
    print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

sys.exit(app.exec())

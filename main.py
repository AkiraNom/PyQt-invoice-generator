from datetime import datetime
import os
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox, QPushButton, QMenu
import shutil
import sys
from PyQt6 import QtWidgets, uic

from invoice import Ui_MainWindow
from add_item import Ui_add_item
from create_report import InvoiceData
from connect_db import DataBaseConnect

class SearchClientWindow(QDialog):

    client_data_signal = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        uic.loadUi("./ui/search_db.ui", self)
        self.connect_db = DataBaseConnect()
        data = self.connect_db.get_all_clients()
        self.client_table = self.tableWidget
        css = '''
            color:black;
        '''
        self.client_table.setStyleSheet(css)
        self.import_csv_btn.clicked.connect(self.import_csv)
        self.client_widget_close_btn.clicked.connect(self.close_dialog)


        if data:
            for info in data:
                row_count = self.client_table.rowCount()
                self.client_table.insertRow(row_count)
                print(f"current row count: {row_count}")

                action_add_btn = QtWidgets.QPushButton("Add")
                action_add_btn.clicked.connect(lambda: self.action_add_triggered())
                self.client_table.setCellWidget(row_count,0,action_add_btn)

                for column in range(6):
                    item = QTableWidgetItem(str(info[column]))
                    self.client_table.setItem(row_count, column+1, item)

    def action_add_triggered(self):
        button = self.sender()
        if button:
            index = self.client_table.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                print(f"Add button clicked in row: {row}")


            self.client_data = []
            for col in range(self.client_table.columnCount()):
                item = self.client_table.item(row,col)
                if item == None:
                    continue
                self.client_data.append(item.text())

        print([x for x in self.client_data])
        self.client_data_signal.emit(self.client_data)

    def import_csv(self):
        self.connect_db.insert_csv()

    def close_dialog(self):
        self.close()

class AddItemWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_item()
        self.ui.setupUi(self)

    def new_item_data(self):

        id = self.ui.item_id.text().strip()
        name = self.ui.item_name.currentText().strip()
        desc = self.ui.description.toPlainText()
        price = self.ui.price.text().strip()
        quantity = self.ui.quantity.text().strip()

        data_dict = {
            "id" : id,
            "name":name,
            "description":desc,
            "price":price,
            "quantity":quantity
        }

        return data_dict

    def add_new_item(self):

        item_data = self.new_item_data()

        if item_data:
            return item_data

        else:
            pass

    def clear_data_field(self):

        self.ui.item_id.clear()
        self.ui.item_name.clear()
        self.ui.price.setText("0.00")
        self.ui.quantity.setText("0.00")
        self.ui.description.clear()

    def close_item_window(self):
        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.search_client_window = SearchClientWindow()
        self.search_client_window.client_data_signal.connect(self.handle_client_data)

        self.setWindowTitle("Invoice Generator")
        self.SignIn_btn.clicked.connect(self.invoice_page)

        #### invoice_page ####
        # header button action
        self.new_btn.clicked.connect(self.new_invoice)
        self.select_client_btn.clicked.connect(self.open_client_dialog)
        self.add_btn.clicked.connect(self.open_add_item_dialog)
        self.save_btn.clicked.connect(self.saveInvoice)
        self.clear_btn.clicked.connect(self.clear_table_data)
        self.close_btn.clicked.connect(self.close_window)
        self.update_summary_btn.clicked.connect(self.update_summaryFrame)

    def handle_client_data(self, client_data):

        print(f'Received data from the dialog: {client_data}')
        self.clientName.setText(client_data[0])
        self.clientContact.setText(client_data[4])
        self.clientEmail.setText(client_data[1])
        self.clientPhone.setText(client_data[2])
        self.clientAddress.setText(client_data[3])
        self.clientNote.setText(client_data[5])

    def invoice_page(self):

        if (self.companyName.text() == "Supplier Company INC") & (self.companyEmail.text() =="suppliercompany@supplier.com"):
            self.stackedWidget.setCurrentIndex(1)

        else:

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Input Error")
            dlg.setText("""Invalid email address / password combination""")
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Close:
                print("Close")

            return

    def cancelInvoice(self):

        self.n_invoice.clear()
        self.date.setText(datetime.today().strftime('%Y-%m-%d'))
        self.clientName.clear()
        self.clientContact.clear()
        self.clientEmail.clear()
        self.clientPhone.clear()
        self.clientAddress.clear()
        self.clientNote.clear()
        self.total.setText("0.00")
        self.total_quantity.setText("0")
        self.subtotal.setText("0.00")
        self.discount.setText("0.00")
        self.vat.setText("0.00")
        self.vat_rate.setText("7.50")

    def clear_table_data(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)

        self.update_summaryFrame()

    def new_invoice(self):
        self.clear_table_data()
        self.cancelInvoice()

    def open_client_dialog(self):

        self.search_client_window.exec()

    def open_add_item_dialog(self):
        self.dlg = AddItemWindow()

        self.dlg.ui.add_item_btn.clicked.connect(self.new_item_save)
        self.dlg.ui.clear_field_btn.clicked.connect(self.dlg.clear_data_field)
        self.dlg.ui.close_window_btn.clicked.connect(self.dlg.close_item_window)

        self.dlg.exec()

    def get_col_data(self, column):
        data = []
        for row in range(self.tableWidget.rowCount()):
            it = self.tableWidget.item(row, column)
            text = it.text() if it is not None else ""
            data.append(text)

        return data

    def cal_sum_data(self, dtype: int| float , data:list):

        result = sum(map(dtype, data))
        return result

    def update_summaryFrame(self):

        _subtotal = self.get_col_data(5)
        _subtotal = self.cal_sum_data(float,_subtotal)
        _total_quantity = self.get_col_data(4)
        _total_quantity = self.cal_sum_data(int,_total_quantity)
        _discount = float(self.discount.text().strip())
        _vat_rate = float(self.vat_rate.text().strip())

        _vat = (_subtotal - _discount) * (_vat_rate*0.01)
        _total = _subtotal + _vat - _discount


        self.total.setText(str(f"{_total:.2f}"))
        self.total_quantity.setText(str(_total_quantity))
        self.subtotal.setText(str(f"{_subtotal:.2f}"))
        self.discount.setText(str(f"{_discount:.2f}"))
        self.vat.setText(str(f"{_vat:.2f}"))

    def edit_item_data(self,data):
        self.dlg = AddItemWindow()

        # reuse 'add_tem.py' ui
        _translate = QtCore.QCoreApplication.translate
        self.dlg.ui.window_title.setText(_translate("add_item", "Edit Item"))
        self.dlg.ui.item_id.setText(data["id"])
        self.dlg.ui.item_name.setCurrentText(data["name"])
        self.dlg.ui.description.setPlainText(data["description"])
        self.dlg.ui.price.setText(data["price"])
        self.dlg.ui.quantity.setText(data["quantity"])

        self.dlg.ui.add_item_btn.clicked.connect(self.new_item_save)
        self.dlg.ui.clear_field_btn.clicked.connect(self.dlg.clear_data_field)
        self.dlg.ui.close_window_btn.clicked.connect(self.dlg.close_item_window)

        self.dlg.exec()

    def action_edit_triggered(self):

        table = self.tableWidget
        id = table.item(table.currentRow(),0).text()
        name = table.item(table.currentRow(),1).text()
        desc = table.item(table.currentRow(),2).text()
        price = table.item(table.currentRow(),3).text()
        quantity = table.item(table.currentRow(),4).text()

        data = {
            "id" : id,
            "name":name,
            "description":desc,
            "price":price,
            "quantity":quantity
        }

        self.edit_item_data(data)

    def action_delete_triggered(self):

        table = self.tableWidget

        if table.rowCount() >0:
            currentRow = table.currentRow()
            item_name = table.item(table.currentRow(),1).text()
            choice = QMessageBox.warning(self, "Delete data", f"Are you sure to delete {item_name} ?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            if choice == QMessageBox.StandardButton.Yes:
                table.removeRow(currentRow)
                self.update_summaryFrame()

    def show_data(self, data):

        try:
            id = str(data['id'])
            name = str(data['name'])
            desc = str(data['description'])
            price = str(f"{float(data['price']):.2f}")
            quantity = str(data['quantity'])
            amount = str(f"{float(data['price'])*int(data['quantity']):.2f}")

        except ValueError:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Input Error")
            dlg.setText("""Invalid data value \nQuantity must be an integral number""")
            dlg.setIcon(QMessageBox.Icon.Warning)
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Close:
                print("Close")

            return

        table = self.tableWidget
        row_count = table.rowCount()
        table.insertRow(row_count)
        table.setItem(row_count, 0, QTableWidgetItem(id))
        table.setItem(row_count, 1, QTableWidgetItem(name))
        table.setItem(row_count, 2, QTableWidgetItem(desc))
        table.setItem(row_count, 3, QTableWidgetItem(price))
        table.setItem(row_count, 4, QTableWidgetItem(quantity))
        table.setItem(row_count, 5, QTableWidgetItem(amount))

        action_edit = QtGui.QAction("Edit", self)
        action_delete = QtGui.QAction("Delete", self)

        # Connect actions to functions
        action_edit.triggered.connect(lambda: self.action_edit_triggered())
        action_delete.triggered.connect(lambda: self.action_delete_triggered())

        menu = QMenu(self)

        menu.addActions([action_edit, action_delete])

        option_btn = QPushButton(self)
        option_btn.setText("Option")
        option_btn.setMenu(menu)
        table.setCellWidget(row_count,6,option_btn)

        self.update_summaryFrame()

    def new_item_save(self):

        add_item = self.dlg.add_new_item()
        self.show_data(data=add_item)

    def generate_invoice(self):

        InvoiceData(self.companyName.text(),
                    self.companyAddress.text(),
                    self.tableWidget,
                    self.company_logo,
                    self.subtotal.text(),
                    self.discount.text(),
                    self.vat_rate.text(),
                    self.vat.text(),
                    self.total.text(),
                    self.clientName.text(),
                    self.clientAddress.text(),
                    self.n_invoice.text()
                    )

    def saveInvoice(self):

        self.generate_invoice()
        invoiceNumber = self.n_invoice.text()
        client = self.clientName.text()
        file = invoiceNumber+"_"+client+".pdf"
        shutil.copy(f'{file}', f'./saved_invoices/{file}')
        os.remove(file)

    def close_window(self):
        self.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

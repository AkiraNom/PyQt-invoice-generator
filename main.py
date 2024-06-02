import sys
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget, QTableWidgetItem, QMessageBox

from invoice import Ui_MainWindow
from add_item import Ui_add_item

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Invoice Generator")
        self.SignIn_btn.clicked.connect(self.invoice_page)


        #### invoice_page ####
        # header button action
        self.new_btn.clicked.connect(self.new_invoice)
        self.add_btn.clicked.connect(self.open_add_item_dialog)
        self.clear_btn.clicked.connect(self.clear_table_data)
        self.update_summary_btn.clicked.connect(self.update_summaryFrame)

        ### add_item_dialog ###

    def invoice_page(self):
        self.stackedWidget.setCurrentIndex(1)

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
        self.tax.setText("0.00")
        self.set_tax.setText("7.50")

    def clear_table_data(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)

        self.update_summaryFrame()


    def new_invoice(self):
        self.clear_table_data()
        self.cancelInvoice()


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
        _set_tax = float(self.set_tax.text().strip())

        _tax = (_subtotal - _discount) * (_set_tax*0.01)
        _total = _subtotal + _tax - _discount


        self.total.setText(str(f"{_total:.2f}"))
        self.total_quantity.setText(str(f"{_total_quantity:.2f}"))
        self.subtotal.setText(str(f"{_subtotal:.2f}"))
        self.discount.setText(str(f"{_discount:.2f}"))
        self.tax.setText(str(f"{_tax:.2f}"))

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

        self.update_summaryFrame()

    def new_item_save(self):

        add_item = self.dlg.add_new_item()
        self.show_data(data=add_item)

class AddItemWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_item()
        self.ui.setupUi(self)

    def new_item_data(self):
        # retrieve data from input field
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
        # Clear data in UI components
        self.ui.item_id.clear()
        self.ui.item_name.clear()
        self.ui.price.setText("0.00")
        self.ui.quantity.setText("0.00")
        self.ui.description.clear()

    def close_item_window(self):
        self.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

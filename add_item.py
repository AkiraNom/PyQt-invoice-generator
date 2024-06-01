from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_add_item(object):
    def setupUi(self, add_item):
        add_item.setObjectName("add_item")
        add_item.resize(450, 470)
        add_item.setMinimumSize(QtCore.QSize(450, 470))
        add_item.setMaximumSize(QtCore.QSize(450, 470))
        add_item.setStyleSheet("* {\n"
"    font-family: Calibri;\n"
"    font-size:12px;\n"
"}\n"
"\n"
"#window_title {\n"
"    font-size:13px;\n"
"    color:black;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"\n"
"QDialog {\n"
"/*    background-color: white;*/\n"
"    background-color: #fcfcfc;\n"
"    background-color: #f9f9f9;\n"
"}\n"
"#descriptionFrame {\n"
"    border: 0;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnFrame {\n"
"    border: 0;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QLabel  {\n"
"/*     color:#7B68EE;*/\n"
"    font-size:11px;\n"
"    font-weight:Normal;\n"
"}\n"
"\n"
"QLineEdit, QPlainTextEdit, QComboBox, QSpinBox, QDoubleSpinBox {\n"
"    font-size:11px;\n"
"    font-weight:bold;\n"
"    border: none;\n"
"    border-bottom: 2px solid #E5E4E2;\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus, QPlainTextEdit:focus,QComboBox:focus,QSpinBox:focus,QDoubleSpinBox:focus {\n"
"    border-bottom: 2px solid #7B68EE;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 12px;\n"
"    background-color:white;\n"
"    border: 2px solid  #E5E4E2;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #7B68EE;\n"
"}\n"
"\n"
"")
        self.widget = QtWidgets.QWidget(parent=add_item)
        self.widget.setGeometry(QtCore.QRect(10, 10, 433, 562))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.window_title = QtWidgets.QLabel(parent=self.widget)
        self.window_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.window_title.setObjectName("window_title")
        self.verticalLayout_2.addWidget(self.window_title)
        self.idFrame = QtWidgets.QWidget(parent=self.widget)
        self.idFrame.setObjectName("idFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.idFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.idFrame)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.item_id = QtWidgets.QLineEdit(parent=self.idFrame)
        self.item_id.setMinimumSize(QtCore.QSize(100, 25))
        self.item_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.item_id.setObjectName("item_id")
        self.horizontalLayout.addWidget(self.item_id)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.idFrame)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.item_name = QtWidgets.QComboBox(parent=self.widget_2)

        self.item_name.setMinimumSize(QtCore.QSize(200, 25))
        self.item_name.setEditable(True)
        self.item_name.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.item_name.setObjectName("item_name")
        self.item_name.addItem("")
        self.item_name.addItem("")
        self.item_name.addItem("")
        self.item_name.addItem("")
        self.item_name.addItem("")
        self.horizontalLayout_2.addWidget(self.item_name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.priceFrame = QtWidgets.QWidget(parent=self.widget)
        self.priceFrame.setObjectName("priceFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.priceFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.priceFrame)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.price = QtWidgets.QLineEdit(parent=self.priceFrame)
        self.price.setMinimumSize(QtCore.QSize(100, 25))
        self.price.setMaximumSize(QtCore.QSize(100, 16777215))
        self.price.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.price.setText("0.00")

        # self.price = QtWidgets.QDoubleSpinBox(parent=self.priceFrame)
        # self.price.setMinimumSize(QtCore.QSize(150, 25))
        # self.price.setObjectName("price")
        # self.price.setRange(0.00, 99999.99)
        # self.price.setValue(0.00)

        self.price.setEnabled(True)
        self.horizontalLayout_4.addWidget(self.price)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(parent=self.priceFrame)
        self.label_5.setMinimumSize(QtCore.QSize(70, 0))
        self.label_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.quantity = QtWidgets.QLineEdit(parent=self.priceFrame)
        self.quantity.setMinimumSize(QtCore.QSize(100, 25))
        self.quantity.setMaximumSize(QtCore.QSize(100, 16777215))
        self.quantity.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.quantity.setText("0")
        self.quantity.setObjectName("quantity")
        self.horizontalLayout_4.addWidget(self.quantity)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.priceFrame)
        self.descriptionFrame = QtWidgets.QFrame(parent=self.widget)
        self.descriptionFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.descriptionFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.descriptionFrame.setObjectName("descriptionFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.descriptionFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.descriptionFrame)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.description = QtWidgets.QPlainTextEdit(parent=self.descriptionFrame)
        self.description.setObjectName("description")
        self.horizontalLayout_6.addWidget(self.description)
        self.verticalLayout_2.addWidget(self.descriptionFrame)
        self.btnFrame = QtWidgets.QFrame(parent=self.widget)
        self.btnFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.btnFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.btnFrame.setObjectName("btnFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.btnFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.add_item_btn = QtWidgets.QPushButton(parent=self.btnFrame)
        self.add_item_btn.setMinimumSize(QtCore.QSize(60, 25))
        self.add_item_btn.setObjectName("add_item_btn")
        self.horizontalLayout_3.addWidget(self.add_item_btn)
        self.clear_field_btn = QtWidgets.QPushButton(parent=self.btnFrame)
        self.clear_field_btn.setMinimumSize(QtCore.QSize(60, 25))
        self.clear_field_btn.setObjectName("clear_field_btn")
        self.horizontalLayout_3.addWidget(self.clear_field_btn)
        self.close_window_btn = QtWidgets.QPushButton(parent=self.btnFrame)
        self.close_window_btn.setMinimumSize(QtCore.QSize(60, 25))
        self.close_window_btn.setObjectName("close_window_btn")
        self.horizontalLayout_3.addWidget(self.close_window_btn)
        self.verticalLayout_2.addWidget(self.btnFrame)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)

        self.retranslateUi(add_item)
        QtCore.QMetaObject.connectSlotsByName(add_item)

    def retranslateUi(self, add_item):
        _translate = QtCore.QCoreApplication.translate
        add_item.setWindowTitle(_translate("add_item", "Dialog"))
        self.window_title.setText(_translate("add_item", "Add New Item"))
        self.label_2.setText(_translate("add_item", "Item ID "))
        self.label_3.setText(_translate("add_item", "Item Name"))
        self.item_name.setItemText(0, _translate("add_item", "Item_1"))
        self.item_name.setItemText(1, _translate("add_item", "Item_2"))
        self.item_name.setItemText(2, _translate("add_item", "Item_3"))
        self.item_name.setItemText(3, _translate("add_item", "Item_4"))
        self.item_name.setItemText(4, _translate("add_item", "Item_5"))
        self.label_4.setText(_translate("add_item", "Price"))
        self.label_5.setText(_translate("add_item", "Quantity"))
        self.label_6.setText(_translate("add_item", "Description"))
        self.add_item_btn.setText(_translate("add_item", "Add"))
        self.clear_field_btn.setText(_translate("add_item", "Clear"))
        self.close_window_btn.setText(_translate("add_item", "Close"))



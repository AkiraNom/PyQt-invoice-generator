from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from datetime import date

import os

class InvoiceData():
    def __init__(self,company,companyAddress,table,logo,subtotal,discount,vat_rate,vat,total,client,clientAddress,invoiceNumber):
        d_ate = date.today()
        today = d_ate.strftime("%d-%m-%Y")
        file = invoiceNumber+"_"+client+".pdf"
        page = canvas.Canvas(file, pagesize=A4)
        style = ParagraphStyle("style",fontName="Helvetica",fontSize=10,leading=15)

        base_font_color = "#000000"
        highlight_font_color = "#5c6ac4"

        page.drawImage(logo, 24, 760, width=100, height=100, preserveAspectRatio=True, mask="auto")
        page.setFont("Helvetica-Bold", 18)
        page.drawString(90, 773, "Business Solution Inc.")
        page.setFont("Helvetica", 12)
        page.setFillColor(HexColor("#b1b1b1"))
        page.drawString(350, 783, "Date:")
        page.drawString(450, 783,"Invoice #:")
        page.setFont("Helvetica-Bold", 12)
        page.setFillColor(HexColor(highlight_font_color))
        page.drawString(350, 763, today)
        page.drawString(450, 763,invoiceNumber)

        left_padding = 20
        top_padding = 615
        width = 560
        height = 120
        page.setFillColor(HexColor("#f1f5f9"))
        page.setLineWidth(0.1)
        page.setStrokeColor(HexColor("#f1f5f9"))
        page.rect(left_padding, top_padding, width, height, stroke=1,fill=1)

        page.setFont("Helvetica-Bold", 12)
        page.setFillColor(HexColor(base_font_color))
        page.drawString(25, 700, company)
        page.drawString(400, 700, client)
        page.setFont("Helvetica", 10)
        page.drawString(25, 673, "Address :")
        page.drawString(400, 673, "Address:")

        p1 = Paragraph(companyAddress, style)

        p1.wrapOn(page, 100, 100)
        p1.drawOn(page, 76, 636)

        p2 = Paragraph(clientAddress, style)

        p2.wrapOn(page, 100, 100)
        p2.drawOn(page, 451, 636)

        page.setFont("Helvetica-Bold", 11)
        page.setFillColor(HexColor(highlight_font_color))

        page.drawCentredString(49 , 592, "#")
        page.drawCentredString(144, 592, "Product details")
        page.drawCentredString(250, 592, "Quantity")
        page.drawCentredString(350, 592, "Price")
        page.drawCentredString(490, 922, "Amount")

        page.setLineWidth(1.2)
        page.setStrokeColor(HexColor(highlight_font_color))
        page.line(24, 585, 571, 585)

        page.setFont("Helvetica", 9)
        page.setLineWidth(.5)
        page.setFillColor(HexColor(base_font_color))

        line_y = 585

        row = table.rowCount()

        for i in range(row):
            if line_y <= 30 and line_y >= 0:

                page.showPage()
                page.setFont("Helvetica", 9)
                line_y = 752

                page.line(24, line_y, 571, line_y)

                line_y = line_y - 13

                page.drawCentredString(49 , line_y, f"{i+1}.")
                page.drawCentredString(144, line_y, table.item(i,1).text())
                page.drawCentredString(250, line_y, table.item(i,2).text())
                page.drawCentredString(350, line_y, f"${table.item(i,3).text()}")
                page.drawCentredString(490, line_y, f"${table.item(i,4).text()}")

                line_y = line_y - 7

                page.setStrokeColor(HexColor("#e5e7eb"))
                page.line(24, line_y, 571, line_y)

            else:
                line_y = line_y - 13

                # page.drawCentredString(49, line_y, table.item(i,0).text())
                page.drawCentredString(49 , line_y, f"{i+1}.")
                page.drawCentredString(144, line_y, table.item(i,1).text())
                page.drawCentredString(250, line_y, table.item(i,2).text())
                page.drawCentredString(350, line_y, f"${table.item(i,3).text()}")
                page.drawCentredString(490, line_y, f"${table.item(i,4).text()}")

                line_y = line_y - 7

                page.setStrokeColor(HexColor("#e5e7eb"))
                page.line(24, line_y, 571, line_y)

        if line_y >= 30 and line_y <= 70:
            line_y = line_y = 817
            page.showPage()
            page.setFont("Helvetica", 9)

        page.setFont("Helvetica-Bold", 12)
        page.setFillColor(HexColor("#3d3d3d"))
        page.setLineWidth(1.2)
        page.setStrokeColor(HexColor("#3d3d3d"))
        page.drawRightString(480, line_y-35, "Subtotal :")
        page.line(480, line_y-38, 560, line_y-38)
        page.drawRightString(480, line_y-53, "Discount :")
        page.line(480, line_y-56, 560, line_y-56)
        page.drawRightString(480, line_y-71, f"VAT ({vat_rate}%) :")
        page.line(480, line_y-74, 560, line_y-74)
        page.drawRightString(480, line_y-89, "Total :")
        page.line(480, line_y-92, 560, line_y-92)

        # page.setFont("Helvetica-Bold", 10)
        page.setFillColor(HexColor(highlight_font_color))
        page.drawRightString(551, line_y-35, f"${subtotal}")
        page.drawRightString(551, line_y-53, f"-${discount}")
        page.drawRightString(551, line_y-71, f"${vat}")
        page.drawRightString(551, line_y-89, f"${total}")

        bank = "Silicon Bank"
        bank_code = " 123456"
        account_n = "132445556"
        payment_reference = "BBB-00032"
        page.saveState()
        page.setFont("Helvetica-Bold", 12)
        page.setFillColor(HexColor(highlight_font_color))
        page.drawString(24, line_y-148, "PAYMENT DETAILS")
        page.setFont("Helvetica", 12)
        page.setFillColor(HexColor(base_font_color))
        page.drawString(24, line_y-160, bank)
        page.drawString(24, line_y-172, f"Bank Code: {bank_code}")
        page.drawString(24, line_y-184, f"Account Number: {account_n}")
        page.drawString(24, line_y-196, f"Payment Reference: {payment_reference}")

        page.setFont("Helvetica-Bold", 12)
        page.setFillColor(HexColor(highlight_font_color))
        page.drawString(24, line_y-230, "Notes:")
        page.setFont("Helvetica", 12)
        page.setFillColor(HexColor(base_font_color))

        notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
        p3 = Paragraph(notes, style)

        p3.wrapOn(page, 500, 200)
        p3.drawOn(page, 75, line_y-280)

        page.save()

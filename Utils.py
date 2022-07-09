from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
from datetime import datetime


class MakeDeclarationPdf:
    def __init__(self, nameToSave, signature, signatureImg, studentName, studentRg, studentCpf, cpfOwner):
        months = {1: 'Janeiro', 2: 'Fevereiro', 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
                  7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
        currentDate = datetime.now()
        self.dateNow = f"{currentDate.day} de {months[currentDate.month]} de {currentDate.year}"
        self.filename = str(nameToSave)
        self.documentTitle = str("declaracao")
        self.signature = str(signature)
        self.signatureImg = str(signatureImg)
        self.title = str("DECLARAÇÃO")
        self.name = str(studentName)
        self.rg = str(studentRg)
        self.cpf = str(studentCpf)
        self.cpfOwner = str(cpfOwner)
        self.headerImg = str("../../img/transtourImg.jpg")
        self.headerImgTwo = str("../../img/numberTranstour.jpg")
        self.make()

    def make(self):
        p1Style = ParagraphStyle(
            "paragraph one style",
            justifyBreaks=10,
            fontName="Times-Roman",
            firstLineIndent=30,
            leading=25,
            fontSize=15,
        )

        p1 = Paragraph("""A <b>TRANS  TOUR</b> inscrita no CNPJ sob nº. 10.144.221/0001-97 e Inscrição
        Municipal nº. 003.947-0, situada a Rua: Júlio Pereira da Silva, nº 03, Salviano Santos,
        Caicó/RN, CEP: 59.300-000 vem por meio desta declarar para os devidos fins que se fizerem
        fizerem necessários que <b>%s</b> RG: <b>%s</b> CPF: <b>%s</b>, tem uma despesa mensal referente ao transporte escolar
        no valor de R$ 150.00 (CENTO E CINQUENTA REAIS).""" % (self.name, self.rg, self.cpf), p1Style)

        p2 = Paragraph(
            """A presente declaração é a expressão da verdade, pelo que assino, sob as penas e rigores da lei.""", p1Style)

        width, heigth = A4

        pdf = canvas.Canvas(self.filename, pagesize=A4)
        pdf.setTitle(self.documentTitle)

        p1.wrapOn(pdf, 510, 50)
        p1.drawOn(pdf, width-540, heigth-340)

        p2.wrapOn(pdf, 510, 50)
        p2.drawOn(pdf, width-540, heigth-450)

        pdfmetrics.registerFont(
            TTFont('OpenSansRegular', '../../fonts/OpenSansRegular.ttf'))
        pdfmetrics.registerFont(
            TTFont('OpenSansBold', '../../fonts/OpenSans-Bold.ttf'))
        pdfmetrics.registerFont(
            TTFont('TimesRoman', '../../fonts/TimesRoman.ttf'))

        pdf.setFont("TimesRoman", 14)
        pdf.drawString(400, 270, f"Caicó, {self.dateNow}")

        pdf.drawInlineImage(self.headerImg, 220, 730,
                            150, preserveAspectRatio=True)
        pdf.drawInlineImage(self.headerImgTwo, 275, 755,
                            85, preserveAspectRatio=True)

        pdf.line(200, 190, 400, 190)

        p3Style = ParagraphStyle(
            "paragraph three style",
            alignment=1,
            fontName="Times-Roman",
        )

        p3 = Paragraph(
            f"<b>{self.signature}</b><br/><b>TITULAR</b><br/><b>CPF:</b><b> {self.cpfOwner}</b>", p3Style)

        p3.wrapOn(pdf, 150, 20)
        p3.drawOn(pdf, width-370, heigth-695)

        pdf.setFont("OpenSansRegular", 22)
        pdf.drawCentredString(300, 700, self.title)

        pdf.line(230, 698, 370, 698)

        pdf.drawInlineImage(self.signatureImg, 250, 160,
                            85, preserveAspectRatio=True)

        pdf.save()

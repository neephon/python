from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50, 'learning let me happy',textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d,'learn.pdf','a simple pdf file')

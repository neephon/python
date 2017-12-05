from urllib.request import Request, urlopen
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

url = 'http://services.swpc.noaa.gov/text/27-day-outlook.txt'
Comment_chars = '#:'

drawing = Drawing(400,200)
data = []
for line in urlopen(url).readlines():
    if not line.isspace() and not line.decode()[0] in Comment_chars:
        data.append([float(n) for n in line.decode().replace('Dec','').split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times,pred)),list(zip(times,high)),list(zip(times,low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250,150, 'Sunspots', fontSize=14, fillColor=colors.red))


# drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
# drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
# drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))
# drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing,'report2.pdf','Sunspots')

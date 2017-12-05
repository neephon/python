from urllib.request import urlopen
url = 'http://services.swpc.noaa.gov/text/27-day-outlook.txt'
hh = '#:'
data = []
for line in urlopen(url).readlines():
    if not line.isspace() and not line.decode()[0] in hh:
        data.append([float(n) for n in line.decode().replace('Dec','').split()])

import json
import matplotlib.pyplot as plt
import requests

def plotCazuri():
    global cazuri
    pl1 = plt.plot(cazuri)
    plt.legend((pl1), (['Cazuri totale']))
    plt.show()

def plotNoi():
    global cazuri
    cazuriNoi = []

    l = len(cazuri)

    for i in range(1, l):
        cazuriNoi.append((cazuri[i] - cazuri[i-1]))

    pl1 = plt.plot(cazuriNoi)
    plt.legend((pl1), (['Cazuri noi']))
    plt.show()

def plotAnaliza():
    global cazuri
    cazuriNoi = []

    l = len(cazuri)

    for i in range(1, l):
        cazuriNoi.append((cazuri[i] - cazuri[i-1]))

    l = len(cazuriNoi)

    minime = []
    maxime = []

    for i in range(l - 7):
        mx = cazuriNoi[i]
        mn = cazuriNoi[i]
        for j in range(7):
            mx = max(cazuriNoi[i + j], mx)
            mn = min(cazuriNoi[i + j], mn)
        minime.append(mn)
        maxime.append(mx)

    pl1, = plt.plot(maxime)
    pl2, = plt.plot(minime)
    plt.legend((pl1, pl2), ('Maxim saptamanal', 'Minim saptamanal'))
    plt.show()

def plotRata():
    rate = []

    for i in range(3, l):
        rate.append((cazuri[i-1]/cazuri[i-2]) / (cazuri[i-2]/cazuri[i-3]))

    plt.plot(rate)
    plt.grid(color='k', linestyle='dotted', linewidth=1)
    plt.show()

url = 'https://d35p9e4fm9h3wo.cloudfront.net/latestData.json'
r = requests.get(url)

data = r.content

data = json.loads(data)

cazuri = []

for i in data["historicalData"]:
    cazuri.insert(0, data["historicalData"][i]["numberInfected"])

cazuri.append(data["currentDayStats"]["numberInfected"])

l = len(cazuri)
print("{:s}\nCazuri: {:d}\nCazuri noi: {:d}".format(data["currentDayStats"]["parsedOnString"], cazuri[l - 1], cazuri[l - 1] - cazuri[l - 2]))
print("Rata de infectare: {:f}".format((cazuri[l-1]/cazuri[l-2]) / (cazuri[l-2]/cazuri[l-3])))


a = input("\nCazuri: c\nCazuri noi: n\nAnaliza: a\nRata de infectare: r\nOptiune: ")

if a == 'c':
    plotCazuri()
elif a == 'n':
    plotNoi()
elif a == 'a':
    plotAnaliza()
elif a == 'r':
    plotRata()
else:
    print("Input invalid")


import datetime
from .database.orderOFdiagram import orderDate
from collections import Counter

def getinterval(start,end):
    start = datetime.datetime.strptime(start[:10], '%Y-%m-%d')
    end = datetime.datetime.strptime(end[:10],'%Y-%m-%d')
    aboba = start.date()
    mas = []
    while (aboba + datetime.timedelta(1))< end.date():
        mas.append(aboba.isoformat())
        aboba+= datetime.timedelta(1)

    return  mas

def GetJsonDSOC(date,ordersStation,station_list): #DSOC - date station orders count
    ordersdates = []
    countOrderMas = []
    if ordersStation == []:
        for x in station_list:
            jsonk = {
                'station': x,
                'countOrder': 0
            }
            countOrderMas.append(jsonk)
    else:
        for x in station_list:
            counts = Counter(ordersStation)
            jsonk = {
                'station': x,
                'countOrder': counts[x]
            }
            countOrderMas.append(jsonk)
    ordersdates.append(
        {
            'date': date,
            'stationOrder': countOrderMas
        }
    )
    return ordersdates

def GetMasBars(date,ordersStation,station_list): #DSOC - date station orders count
    ordersdates = []
    countOrderMas = []
    if ordersStation == []:
        for x in station_list:
            jsonk = {
                'station': x,
                'countOrder': 0
            }
            countOrderMas.append(jsonk)
    else:
        for x in station_list:
            counts = Counter(ordersStation)
            jsonk = {
                'station': x,
                'countOrder': counts[x]
            }
            countOrderMas.append(jsonk)
    ordersdates.append(
        {
            'date': date,
            'stationOrder': countOrderMas
        }
    )
    return ordersdates

def getmaxel(mas):
    maxel = 0
    for i in mas:
        for j in i :
            if j>maxel:
                maxel = j
    return maxel


def CountSumOfDict(station_list,masDicts):
    StationAndSum = []
    summ = 0
    for x in station_list:
        summ = 0
        for y in masDicts:

            try:
                summ+= y[x]

            except:
                print()
        StationAndSum.append(
            {f'{x}': summ}
        )
    return (StationAndSum)






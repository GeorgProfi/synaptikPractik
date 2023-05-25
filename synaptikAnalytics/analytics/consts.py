date_start = str
date_end = str
# период за который берём а налитику (в днях)
import datetime
from .database.orderOFdiagram import orderDate


def getinterval(start,end):
    start = datetime.datetime.strptime(start[:10], '%Y-%m-%d')
    end = datetime.datetime.strptime(end[:10],'%Y-%m-%d')
    aboba = start.date()
    mas = []
    while (aboba + datetime.timedelta(1))< end.date():
        mas.append(aboba.isoformat())
        aboba+= datetime.timedelta(1)

    return  mas

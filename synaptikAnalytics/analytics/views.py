from django.shortcuts import render
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .database.orderOFdiagram import orderDate

from collections import Counter
import json
import datetime
from .database import analiticsQuery,TopClient
from .consts import  getinterval,GetJsonDSOC,getmaxel, CountSumOfDict
# Create your views here.




@csrf_exempt
def TopClients(request):

    body = json.loads(request.body)
    userID = jwt_decode_handler(body["access"])['sub']
    date_start = body['datastart']
    date_end = body['dataend']
    statistic = TopClient.GetTopClient(analiticsQuery.GetCompany(userID),date_start,date_end)
    data = []
    for i in statistic:
        block_data = {
            'client': i[0],
            'count': i[1],
            'sum': i[2],
        }
        data.append(block_data)

    return JsonResponse(
        {'count': len(statistic),
            'data': data },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )



@csrf_exempt
def analytics(request):
    body = json.loads(request.body)
    userID = jwt_decode_handler(body["access"])

    date_start = body['datastart']
    date_end = body['dataend']

    statistic = analiticsQuery.getAnaliz(analiticsQuery.GetCompany(userID['sub']),date_start,date_end)
    data = []
    all_sum =0
    for i in statistic:
        block_data = {
            'name': i[0],
            'total': i[1],
            'avg':float(i[2]),
            "workload":  float(i[3])
        }
        data.append(block_data)
        all_sum+=i[1]

    return JsonResponse(
    {
        'sum':all_sum,
        'count': len(statistic),
        'data': data
    },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )

@csrf_exempt
def diagram(request):
    body = json.loads(request.body)
    userID = jwt_decode_handler(body["access"])['sub']
    print(analiticsQuery.GetCompany(userID))
    date_start = body['datastart']
    date_end = body['dataend']


    dates = getinterval(date_start,date_end)
    statistic = orderDate(analiticsQuery.GetCompany(userID),date_start,date_end)
    station_list = []
    for j in statistic:
        if not (j[0] in station_list):
            station_list.append(j[0])
    print(station_list)

    i = 0

    masvalue = [[]* 1 for _ in range((len(station_list)))]
    dailyIncomeMas  = [[] * 1 for _ in range((len(station_list)))]
    print(masvalue)
    negr = []
    hui = []
    formated_dates= []
    for date in dates:

        formated_dates.append( date[5:])
        for stat in statistic:

            if str(stat[1].date()) == date:
                hui.append(stat[0])

                negr.append({
                    f'{stat[0]}': stat[2]
                })
                print(stat)
                i += 1
        print(negr)
        if hui == []:
            j = 0
            for x in station_list:
                masvalue[j].append(0)
                dailyIncomeMas[j].append(0)
                j += 1
        else:
            j = 0
            sumOrders = CountSumOfDict(station_list,negr)
            for x in station_list:
                carwarshIndex = station_list.index(x)
                counts = Counter(hui)
                masvalue[j].append(counts[x])
                dailyIncomeMas[j].append(sumOrders[carwarshIndex][x])
                j += 1



        hui = []
        negr=[]
    print(dailyIncomeMas)
    print(getmaxel(masvalue))
    #orders.append( GetJsonDSOC(date,hui, station_list))

    return JsonResponse(
        { 'stationList': station_list,
            'dates': formated_dates,
            'values': masvalue,
            'maxEl': getmaxel(masvalue),
            'dailyIncomes' : dailyIncomeMas,
            'maxIncome': getmaxel(dailyIncomeMas)
          },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )

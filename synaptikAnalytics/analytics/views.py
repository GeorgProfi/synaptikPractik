from django.shortcuts import render
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .database.orderOFdiagram import orderDate

import json
import datetime
from .database import analiticsQuery,TopClient
from .consts import date_end,date_start, getinterval
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
    i = 0
    stat_json = {}
    for date in dates:
        for stat in statistic:

            if str(stat[1].date()) == date:
                print()
                print(stat)
                stat_mas.append([])
    print(date_start[:10])
    data = []
    for i in statistic:
        print(i)
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

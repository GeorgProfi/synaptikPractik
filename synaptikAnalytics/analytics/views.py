from django.shortcuts import render
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .database import analiticsQuery,TopClient
# Create your views here.

@csrf_exempt
def TopClients(request):
    print("ТВОЮ МАТЬ")
    body = json.loads(request.body)
    userID = jwt_decode_handler(body["access"])['sub']
    statistic = TopClient.GetTopClient(analiticsQuery.GetCompany(userID))
    print(statistic[0])
    data = []
    for i in statistic:
        block_data = {
            'name': i[0],
            'count': i[1],
            'sum': i[2],
        }
        data.append(block_data)

    print({'count': len(statistic),
            'data': json.dumps(data) })
    return JsonResponse(
        {'count': len(statistic),
            'data': data },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )



@csrf_exempt
def analytics(request):
    print(request.headers)
    body = json.loads(request.body)
    userID = jwt_decode_handler(body["access"])
    statistic = analiticsQuery.getAnaliz(analiticsQuery.GetCompany(userID['sub']))
    print(statistic[0])
    data = []
    for i in statistic:
        block_data = {
            'name': i[0],
            'total': i[1],
            'avg':float(i[2]),
            "workload":  float(i[3])
        }
        data.append(block_data)

    print({'count': len(statistic),
            'data': json.dumps(data) })
    return JsonResponse(
        {'count': len(statistic),
            'data': data },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )
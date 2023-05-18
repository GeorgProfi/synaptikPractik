from django.shortcuts import render
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .database import analiticsQuery
# Create your views here.
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
            "workload":  i[3].seconds
        }
        data.append(block_data)

    print({'count': len(statistic),
            'data': json.dumps(data) })
    return JsonResponse(
        {'count': len(statistic),
            'data': json.dumps(data) },
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )
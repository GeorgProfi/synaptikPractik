
from django.db import connection


def orderDate(companyId,start,end):
   query = f""" 
        select "station"."name" ,"order"."startWork","order"."priceTotal" from public."order"
inner join  station on
"order"."stationId" = "station"."id"
where ("order"."companyId" = '{companyId}')
AND ("order"."startWork") > '{start}'
		AND ("order"."endWork") < '{end}'
		order by "station"."name" 
        """
   with connection.cursor() as cursor:
       cursor.execute(query)
       row = cursor.fetchall()
       return row



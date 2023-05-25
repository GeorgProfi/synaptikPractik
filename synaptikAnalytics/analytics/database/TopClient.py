from django.db import connection



def GetTopClient(companyId,start,end):
    query = f"""
    SELECT client.name, count(client.name), sum("order"."priceTotal")
    FROM "order"
        JOIN station ON "order"."stationId" = station.id
        JOIN client ON "order"."clientId" = client.id
    where "order"."companyId" = '{companyId}' 
    		AND ("order"."startWork") > '{start}'
		AND ("order"."endWork") < '{end}'
    group by client.name
    order by sum desc
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return rows
from django.db import connection

def getAnaliz(companyId):
    query = f"""
    SELECT station.name,
        sum("order"."priceTotal") AS "all",
        avg("order"."priceTotal") AS avg,
        trunc(EXTRACT(epoch FROM sum("order"."endWork" - "order"."startWork")) / EXTRACT(epoch FROM sum(station."endWork" - station."startWork")*30) * 100::numeric, 2) AS workload
    FROM "order"
    JOIN station ON "order"."stationId" = station.id
        where ("order"."companyId" = '{companyId}') AND ((now() - "order"."startWork") < '30 days'::interval)
    GROUP BY station.id;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return rows

def GetCompany(userid):
   query = f""" 
        SELECT "companyId" FROM public.owner
        where "id" = '{userid}'
        """
   with connection.cursor() as cursor:
       cursor.execute(query)
       row = cursor.fetchone()
       print(row)
       return row[0]

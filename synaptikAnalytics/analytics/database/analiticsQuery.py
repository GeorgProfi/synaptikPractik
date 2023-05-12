from django.db import connection

def getAnaliz(companyId):
    query = f"""
    SELECT station.name,
        sum("order"."priceTotal") AS "all",
        avg("order"."priceTotal") AS avg,
        sum("order"."endWork" - "order"."startWork") AS "allTime"
    FROM "order"
    JOIN station ON "order"."stationId" = station.id
        where "order"."companyId" = '{companyId}'
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
       print(row[0])
       return row[0]
from database.DB_connect import DBConnect
from model.avvistamenti import Avvistamento
from model.stati import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getSights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from sighting s """

        cursor.execute(query,)

        for row in cursor:
            result.append(Avvistamento(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s 
                    """

        cursor.execute(query,)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  select
                    n.state1 as s1, n.state2 as s2
                    from neighbor n 
                 """

        cursor.execute(query, )

        for row in cursor:
            result.append((row["s1"],row["s2"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getPeso(anno,forma,s1,s2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
                    from sighting s 
                    where year(s.`datetime`) = %s
                    and s.shape = %s
                    and (s.state = %s
                    or s.state = %s)  
                """

        cursor.execute(query,(anno,forma,s1,s2))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getDistanza(s1, s2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select 2 * 6371 * 
                    ASIN(SQRT(
                        POWER(SIN(RADIANS(s2.Lat - s.Lat) / 2), 2) + 
                        COS(RADIANS(s.Lat)) * COS(RADIANS(s2.Lat)) * 
                        POWER(SIN(RADIANS(s2.Lng - s.Lng) / 2), 2)
                    )) as d
                    from state s, state s2 
                    where s.id = %s
                    and s2.id = %s 
                """

        cursor.execute(query, (s1, s2))

        for row in cursor:
            result.append(row["d"])

        cursor.close()
        conn.close()
        return result


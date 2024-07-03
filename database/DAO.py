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
        query = """select s.Lat as lat1,s.Lng as long1,s2.Lat as lat2,s2.Lng as long2 
from state s, state s2 
where s.id = %s
and s2.id = %s 
                """

        cursor.execute(query, (s1, s2))

        for row in cursor:
            result.append((row["lat1"],row["long1"],row["lat2"],row["long2"]))

        cursor.close()
        conn.close()
        return result


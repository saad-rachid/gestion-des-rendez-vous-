import mysql.connector
from  models import Rdv , Assistante 

class DatabaseConnection:
    

    def __init__(self):

        """Virtually private constructor."""
       
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "root"
        self.__database = "gestion_rdv"

        self.connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
        )

        
    
    def get_connection(self):
        return self.connection
    




class Rdv_dao :

    def __init__(self , con):
       
       self.db = con


    def add_rdv(self, rdv):

        try :

            curseur = self.db.cursor()
            q = "INSERT INTO rdv(cin, nomP, prenomP, telephone, date_rdv) VALUES (%s, %s, %s, %s, %s)"
            v =(rdv.getId(), rdv.get_nomP(), rdv.get_prenomP(), rdv.get_tel(), rdv.get_date())
            curseur.execute(q,v) 
            self.db.commit()
            curseur.close()
            
            return rdv

        except mysql.connector.Error as err:
                
            print("Insert failed")
            print(f"Query execution failed: {err}")

            return None


    def get_all(self):

        try:

            cursor = self.db.cursor()
            q = "SELECT cin, nomP,prenomP, telephone, date_rdv FROM rdv "
            cursor.execute(q)
            result = cursor.fetchall()
            
            L = []
            for r in result :
                rdv = Rdv(r[0], r[1], r[2], r[3], r[4])
                L.append(rdv)

            cursor.close()
            return result



        except mysql.connector.Error as err:
                
            print("selection failed")
            print(f"Query execution failed: {err}")

            return None   


    def get_by_id(self, cin):

        try :

            cursor = self.db.cursor()
            q = "SELECT * FROM rdv where cin = %s"
            cursor.execute(q, (cin,))
            result = cursor.fetchall()
            
            L = []
            for item in result:
                rdv = Rdv(item[1], item[2], item[3],item[4], item[5])
                L.append(rdv)

            cursor.close()
            return L
        

        except mysql.connector.Error as err:
                
            print("selection failed")
            print(f"Query execution failed: {err}")
            
            return L
        


    def get_by_date(self, date):

        try :

            cursor = self.db.cursor()
            q = "SELECT * FROM rdv where date_rdv = %s"
            cursor.execute(q, (date,))
            result = cursor.fetchall()

            L = []

            for r in result :
                for item in r:
                    rdv = Rdv(item[1], item[2], item[3],item[4], item[5])
                    L.append(rdv)

            cursor.close()
            return L
        

        except mysql.connector.Error as err:
                
            print("selection failed")
            print(f"Query execution failed: {err}")
            
            return L   
        

    def modify(self,cin, date):

        try :

            cursor = self.db.cursor()
            q = "UPDATE rdv SET date_rdv = %s  WHERE cin = %s "
            cursor.execute(q, (date,cin))
            self.db.commit()

            q1 = "SELECT * FROM rdv where cin = %s AND date_rdv = %s "
            cursor.execute(q1, (cin,date))
            result = cursor.fetchall()[0]
            rdv = Rdv(result[1], result[2], result[3],result[4], result[5])
            rdv.set_date(date)
            cursor.close()
            return rdv
        

        except mysql.connector.Error as err:
                
            print("selection failed")
            print(f"Query execution failed: {err}")
            
            return None    
        


    def delete(self, rdv):
        
        try :

            cursor = self.db.cursor()
            q = "DELETE FROM rdv where cin = %s "
            cursor.execute(q, (rdv.getId(),))
            self.db.commit()
            cursor.close()
            return True
        

        except mysql.connector.Error as err:
                
            print("delete failed")
            print(f"Query execution failed: {err}")
            
            return False


class Assistante_dao:

    def __init__(self , con):
       
       self.db = con

    def get_assistante(self, username, pwd):

        try :

            cursor = self.db.cursor()
            q = "SELECT * FROM assistante where username = %s AND pass_word = %s"
            cursor.execute(q, (username,pwd))
            result = cursor.fetchall()[0]
            cursor.close()
            assistante = Assistante(result[0], result[1], result[2], result[3], result[4])
            assistante.set_Loggedin()
            return assistante 
      
        

        except mysql.connector.Error as err:
                
            print("the connection failed")
            print(f"Query execution failed: {err}")
            
            return False
        





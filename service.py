from dao import Assistante_dao , Rdv_dao 




class Assistante_Metier :

    def __init__(self, assistante_dao, rdv_dao):

        self.assistante = None

        self.dao = assistante_dao
        self.dao1 = rdv_dao

    def get_assistante(self):
        return self.assistante

    def login(self, username , pwd):

        if self.assistante == None :
            self.assistante = self.dao.get_assistante(username, pwd) 

        else : 
            print("already loggedin..")



    def addRdv(self, rdv):

        if self.assistante.get_Loggedin():

            return self.dao1.add_rdv(rdv)

        else: 
            print("veuillez se connecter dabord...")
            

    def listRdv(self):

        if self.assistante.get_Loggedin():

            return self.dao1.get_all()

        else: 
            print("vous deveez se connecter dabord...")



    def searchById(self, cin):
        
        if self.assistante.get_Loggedin():

            return self.dao1.get_by_id(cin)

        else: 
            print("vous deveez se connecter dabord...")


    def searchByDate(self, date):

        if self.assistante.get_Loggedin():

            return self.dao1.get_by_id(date)

        else: 
            print("vous deveez se connecter dabord...")        


    def modifyRdv(self,cin,date):

        if self.assistante.get_Loggedin():

            return self.dao1.modify(cin,date)

        else: 
            print("vous deveez se connecter dabord...")


    def deleteRdv(self, rdv):

        if self.assistante.get_Loggedin():

            return self.dao1.delete(rdv)

        else: 
            print("vous deveez se connecter dabord...")








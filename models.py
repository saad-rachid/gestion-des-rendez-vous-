
class Assistante:

    def __init__(self, cin, nom , prenom, username, pwd):

        self.Loggedin = False
        self.cin = cin
        self.nom = nom 
        self.prenom = prenom 
        self.username = username 
        self.pwd = pwd 
        


    def get_username(self):
        return self.username
    
    def get_pwd(self):
        return self.pwd
    
    
    def set_Loggedin(self):

        self.Loggedin = True

    def get_Loggedin(self):
        return self.Loggedin 

    def __str__(self):

        return f"assistante : {self.nom} - {self.prenom} \n "
    



class Rdv:

    def __init__(self, cin, nomp, prenomp, tel, d):

        self.cin = cin
        self.nomP = nomp 
        self.prenomP = prenomp
        self.tel = tel 
        self.date = d

    def getId(self):

        return self.cin
    
    def get_nomP(self):
        return self.nomP
    
    def get_prenomP(self):
        return self.prenomP
    
    def get_tel(self):
        return self.tel
    
    def set_date(self, date):

        self.date = date 
    
    def get_date(self):

        return self.date 
    

    def __str__(self):

        return f"Patient : {self.nomP} - {self.prenomP} a un rendez-vous le {self.date}"

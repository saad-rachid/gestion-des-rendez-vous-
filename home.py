from tkinter import *
from tkinter import ttk
from dao import *
from service import Assistante_Metier
from models import Assistante, Rdv
from tkcalendar import DateEntry 



class LandinPage(Tk):

    def __init__(self, metier, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.metier = metier
        
        self.configure(bg = 'white')
        self.title("Cabinet lassili")
        self.geometry("300x300")
        self.iconbitmap("./images.ico")
        self.lbl= Label(self, text= "Gestion des rendez-vous",bg= 'white',  font = ('bold', 12))
        self.lbl.pack( pady = 30)
        self.btn = Button(self, text = "Login" , width = 18 , bg = '#f4717f',foreground= 'white', font = ('bold', 10) ,command= self.LoginForm)
        self.btn.pack(pady = 70)

        self.mainloop()


    def LoginForm(self):

        self.login_form= Toplevel(self)
        self.login_form.configure(bg = 'white')
        self.login_form.title("Sign In")
        self.login_form.geometry("300x400")
        self.login_form.iconbitmap("./images.ico")

        self.label_username = Label(self.login_form, text="Username:", bg = 'white')
        self.label_username.pack(pady = 15)

        self.entry_username = Entry(self.login_form, width = 40 )
        self.entry_username.pack(pady =5)

        self.label_password = Label(self.login_form, text="Password:",bg = 'white')
        self.label_password.pack(pady = 15)

        self.entry_password = Entry(self.login_form, show="*" , width = 40 )
        self.entry_password.pack(pady = 5)

        self.btn_submit = Button(self.login_form, text="Submit", width = 18 , bg = '#f4717f' , foreground= 'white', command=self.Login)
        self.btn_submit.pack(pady = 20)    


    def Login(self):

        user = self.entry_username.get()
        pwd = self.entry_password.get()

        self.metier.login(user, pwd)

        if self.metier.get_assistante():
            print ("Loggin successful")
            self.btn.config(state= 'disabled')
            self.login_form.destroy()
            Home(self.metier)
            

        else : 
            print("le username ou le mot de passe sont incorrecte")    




class Home(Tk):

    def __init__(self, metier, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.metier = metier   
        
        self.configure(bg = 'white')
        self.title("Cabinet lassili")
        self.geometry("400x500")
        self.iconbitmap("./images.ico")
        self.lbl= Label(self, text= "Gestion des rendez-vous",bg= 'white',  font = ('bold', 12))
        self.lbl.pack( pady = 50)

        self.btn = Button(self, text = "Ajouter rendez-vous" , width = 35 , bg = '#f4717f',foreground= 'white', font = ('bold', 10),command= self.addForm)
        self.btn.pack( pady = 10)

        self.btn = Button(self, text = "lister renez-vous" , width = 35 , bg = '#f4717f',foreground= 'white', font = ('bold', 10),command= self.displayRdv)
        self.btn.pack(pady = 10)

       # self.btn = Button(self, text = "Logout" , width = 25 , bg = '#f4717f',foreground= 'white', font = ('bold', 10))# ,command= self.Logout)
        #self.btn.pack(pady = 10)

        self.user = Label(self, text = f"{metier.get_assistante().__str__()}" , bg = 'white', font = ('bold', 10))
        self.user.pack(side= 'right', pady = 150)

        self.mainloop()


    




    def addForm(self):

        self.add_form = Toplevel(self)
        self.add_form.configure(bg = 'white')
        self.add_form.title("cabinet lassili")
        self.add_form.geometry("350x500")
        self.add_form.iconbitmap("./images.ico")
        
        self.titre = Label(self.add_form, text = "Ajouter un rendez-vous...", bg = 'white',  font = ('bold', 10)) 
        self.titre.pack(pady = 10)
    
        #form for adding 
        self.label_cin = Label(self.add_form, text="CIN:", bg = 'white',  font = ('bold', 10))
        self.label_cin.pack(pady = 5)

        self.entry_cin = Entry(self.add_form , width = 40)
        self.entry_cin.pack(pady=5)

        self.label_nom= Label(self.add_form, text="nom:", bg = 'white',  font = ('bold', 10))
        self.label_nom.pack(pady = 5)

        self.entry_nom = Entry(self.add_form, width = 40)
        self.entry_nom.pack(pady = 5)

        self.label_prenom= Label(self.add_form, text="prenom:", bg = 'white',  font = ('bold', 10))
        self.label_prenom.pack(pady = 5)

        self.entry_prenom = Entry(self.add_form,width = 40)
        self.entry_prenom.pack(pady = 5)

        self.label_tel = Label(self.add_form, text="telephone:", bg = 'white',  font = ('bold', 10))
        self.label_tel.pack(pady = 5)

        self.entry_tel= Entry(self.add_form,width = 40)
        self.entry_tel.pack(pady = 5)

        self.label_date = Label(self.add_form, text="date:", bg = 'white',  font = ('bold', 10))
        self.label_date.pack(pady = 5)

        self.entry_date = DateEntry(self.add_form, width=12 , background='white', borderwidth=2)
        self.entry_date.pack(pady = 5)

        self.btn_submit = Button(self.add_form,  width= 20,  text="Add", bg = '#f4717f',foreground= 'white', font = ('bold', 10), command=self.save)
        self.btn_submit.pack(pady = 20)  


    def valid(self, input ) :

        for i in input :
            if i == "" :
                return False
        return True
    
    def save(self):

       
        cin = self.entry_cin.get()
        nomP = self.entry_nom.get()
        prenomP = self.entry_prenom.get()
        tel = self.entry_tel.get()
        date = self.entry_date.get_date().strftime('%Y-%m-%d')

        if self.valid([cin,nomP,prenomP,tel,date]):

            rdv = Rdv(cin, nomP, prenomP, tel , date)

            if self.metier.addRdv(rdv) != None :
                print(rdv)
                print('rdv added successfully...')
                self.add_form.destroy()

            else :

                print('rdv not addes succefully...') 


    def displayRdv(self):

        Main(self.metier)            



class Main(Tk):

    def __init__(self, metier, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.metier = metier
        
        self.configure(bg = 'white')
        self.title("Cabinet lassili")
        self.geometry("1200x1200")
        self.iconbitmap("./images.ico")
        self.lbl= Label(self, text= "Gestion des rendez-vous", bg= 'white',  font = ('bold', 12))
        self.lbl.pack( pady = 5)

        #search frame 

        self.frame = LabelFrame(self, bg= 'white')
        self.frame.pack(fill='both', expand= 'yes', padx = 5, pady= 5 )

        self.search_label = Label(self.frame, text='search' , bg = 'white' , font=('bold', 12))
        self.search_label.pack(padx = 20)

        self.search_entry1 = Entry(self.frame,  width= 50 , bg = 'white')
        self.search_entry1.pack(side = 'left' , padx = 50)

        self.search_entry2 = DateEntry(self.frame, width=12 , background='white', borderwidth=2)
        self.search_entry2.pack(side = 'left' , padx = 105)

        self.search_btn = Button(self.frame, text = 'search', width = 20 ,  bg = '#f4717f',foreground= 'white', font = ('bold', 10), command= self.search)
        self.search_btn.pack(side= 'left', padx = 5)


        #list frame 

        self.frame1 = LabelFrame(self, bg = 'white')
        self.frame1.pack(fill='both', expand= 'yes', padx = 20, pady= 5 )

        self.tree = ttk.Treeview(self.frame1,columns =("cin", "nom", "prenom", "telephone", "date"), show= "headings")
        self.tree.heading("cin", text="cin", anchor=CENTER)
        self.tree.heading("nom", text="nom", anchor=CENTER)
        self.tree.heading("prenom", text="prenom", anchor=CENTER)
        self.tree.heading("telephone", text="telephone", anchor=CENTER)
        self.tree.heading("date",text="date", anchor=CENTER )

        self.tree.pack(pady =10)
        button = Button(self.frame1, text="Modifier", width = 20 ,  bg = '#f4717f',foreground= 'white', font = ('bold', 10), command= self.modifyForm)
        button1 = Button(self.frame1 ,text="supprimer", width = 20 ,  bg = '#f4717f',foreground= 'white', font = ('bold', 10), command =self.supprimer)
        button.pack( padx = 50, pady=10)
        button1.pack(padx=50, pady=10)

        l = self.metier.listRdv()

        self.display(l)

        self.tree.bind("<<TreeviewSelect>>",self.select)
        self.mainloop()

    def display(self, l):

        for item in l:
            self.tree.insert("", END, text="", values=(item[0],item[1],item[2],item[3], item[4]))    


    def select(self, *args):

        selected_item = self.tree.selection()[0] # get the first selected item
        values = self.tree.item(selected_item)['values']
        print(values)
        return selected_item, values


    def supprimer(self):
        t, v = self.select()
        rdv = Rdv(v[0], v[1], v[2], v[3],v[4])

        if self.metier.deleteRdv(rdv):
            print("rdv supprime avec succes ...")
            self.tree.delete(t)
            self.tree.update()

        else : 
            print("impossible de suprimer ....")


    def modifyForm(self):

        self.modify_form = Toplevel(self)
        self.modify_form.configure(bg = 'white')
        self.modify_form.title("cabinet lassili")
        self.modify_form.geometry("350x500")
        self.modify_form.iconbitmap("./images.ico")
        
        self.titre = Label(self.modify_form, text = "Modifier un rendez-vous...", bg = 'white',  font = ('bold', 10)) 
        self.titre.pack(pady = 10)

        t, v = self.select() 
        print(v)
    
        #form for modifying 
        self.label_cin = Label(self.modify_form, text="CIN:", bg = 'white',  font = ('bold', 10))
        self.label_cin.pack(pady = 5)

        self.entry_cin = Label(self.modify_form, text=f"{v[0]}", bg = 'white',  font = ('bold', 10), width = 40)
        self.entry_cin.pack(pady=5)

        self.label_nom= Label(self.modify_form, text="nom:", bg = 'white',  font = ('bold', 10))
        self.label_nom.pack(pady = 5)

        self.entry_nom = Label(self.modify_form, text=f"{v[1]}", bg = 'white',  font = ('bold', 10), width = 40)
        self.entry_nom.pack(pady = 5)

        self.label_prenom= Label(self.modify_form, text="prenom:", bg = 'white',  font = ('bold', 10))
        self.label_prenom.pack(pady = 5)

        self.entry_prenom = Label(self.modify_form, text=f"{v[2]}", bg = 'white',  font = ('bold', 10), width = 40)
        self.entry_prenom.pack(pady = 5)

        self.label_tel = Label(self.modify_form, text="telephone:", bg = 'white',  font = ('bold', 10))
        self.label_tel.pack(pady = 5)

        self.entry_tel= Label(self.modify_form, text=f"{v[3]}", bg = 'white',  font = ('bold', 10), width = 40)
        self.entry_tel.pack(pady = 5)

        self.label_date = Label(self.modify_form, text="date:", bg = 'white',  font = ('bold', 10))
        self.label_date.pack(pady = 5)

        self.entry_date = DateEntry(self.modify_form, width=12 , background='white', borderwidth=2)
        self.entry_date.pack(pady = 5)

        self.btn_submit = Button(self.modify_form,  width= 20,  text="Add", bg = '#f4717f',foreground= 'white', font = ('bold', 10), command=self.save_modification)
        self.btn_submit.pack(pady = 20)  


    def valid(self, input ) :
        
        for i in input:
            if i == "" :
                return False
        return True
    
    def save_modification(self):

        cin = str(self.entry_cin.cget('text'))
       
        date = self.entry_date.get_date().strftime('%Y-%m-%d')

        print(cin,date)

        if self.valid([cin,date]):

            rdv = self.metier.modifyRdv(cin,date) 

            if rdv is not None :
                #print(self.metier.modifyRdv(cin,date))
                print('modifications added successfully...')

                l = self.tree.get_children()

                for i in l :

                    if self.tree.item(i)['values'][0] == rdv.getId():
                        self.tree.delete(i)    
                
                self.tree.insert("", END, text="", values=(rdv.getId(), rdv.get_nomP(), rdv.get_prenomP(), rdv.get_tel(), rdv.get_date()))  

                self.modify_form.destroy()

            else :

                print('modifications not added succefully...')


    def search(self):

        cin = self.search_entry1.get()
        date = self.search_entry2.get_date().strftime('%Y-%m-%d')

        l = self.tree.get_children()
        existe = False

        if cin == "":
            for i in l :

                if self.tree.item(i)['values'][4] == date:
                    existe=True
                    print(self.tree.item(i)['values'])

                else :
                    self.tree.delete(i)    

            if not existe:
                print("le patient n'a pas pris un rendez-vous...")
        
        else :

            for i in l :

                if self.tree.item(i)['values'][0] == cin:
                    existe=True
                    print(self.tree.item(i)['values'])

                else :
                    self.tree.delete(i)    

            if not existe:
                print("le patient n'a pas pris un rendez-vous...")   


              



#Con = DatabaseConnection().get_connection()
#assistante_dao = Assistante_dao(Con)
#rdv_dao = Rdv_dao(Con)
#metier = Assistante_Metier(assistante_dao, rdv_dao)
metier='saad'
LandinPage(metier)

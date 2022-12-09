class Lake(): 
    name=''
    content=''
    ploshina=0.0
    glibina=0.0
    def init(self,name,content, ploshina, glibina): 
        self.name = str(name) 
        self.content= str(content) 
        self.ploshina = float(ploshina) 
        self.glibina= float(glibina) 

    def SetPloshina(self,ploshina:float):
        self.ploshina=ploshina
        print('Площа була змінена',ploshina)
        
    def SetGlibina(self,glibina:float):
        self.glibina=glibina
        print('Глибана була змінена',glibina)
    def __del__(self):
        print("All delete")

a=Lake()
a.init('air','australia',89,250)

a.SetPloshina(54)
a.SetGlibina(189)
 
   
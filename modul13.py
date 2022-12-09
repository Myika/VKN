class Child(): 
    SN=''
    Age=''
    Year=0.0
    def init(self,SN, Year,): 
        self.SN = str(SN)  
        self.Year = int(Year)

    def SetAge(self,Year):
        self.Age=2022-Year
        print('Вік дитини',self.Age)

    
        if self.Age == 6 or self.Age== 7:
            print(f"Іде у перший клаc {self.SN}")

        elif self.Age== 3:
            print(f"Іде у дит садок {self.SN}")

        else:
            print(f"Не підходить за віком {self.SN}")

        

    def GetAge(self):
        return (self.Age)
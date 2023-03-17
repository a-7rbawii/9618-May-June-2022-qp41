class Balloon:
    def __init__(self, dfcit, clr):
        self.__Health = 100 #as INTEGER
        self.__Colour = clr #as STRING
        self.__DefenceItem = dfcit #as STRING
    
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self, addnum):
        self.__Health = self.__Health + addnum
    
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

def Defend(Balloon1):
    strength = int(input("Input level of strength: "))
    Balloon1.ChangeHealth(-strength)
    print("Defense against {}".format(Balloon1.GetDefenceItem()))
    if Balloon1.CheckHealth() == True:
        print("Defence fail !")
    else:
        print("Defence success !")
    return Balloon1

useritem = input("Enter defence item: ")
usercolour = input("Enter colour of balloon: ")

Balloon1 = Balloon(useritem, usercolour)

Balloon1 = Defend(Balloon1)
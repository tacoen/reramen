init -50 python:

    class mc_function():
    
        def withdrawn(self,ammount):
            if mc.bank >= ammount:
                mc.bank -= ammount
                mc.money += ammount
                return True
            else:
                return False
                
        def deposite(self,ammount):
            if mc.money >= ammount:
                mc.bank += ammount
                mc.money -= ammount
                return True
            else:
                return False
                
                
    mcfunc = mc_function()
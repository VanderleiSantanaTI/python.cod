
class Funtion2gaus:
    def __init__(self,a,b,c):
        
           self.a=a
           self.b=b
           self.c=c
    def raizes(self):
        if  ((self.b)**2 - 4*self.a*self.c) < 0:

            nc =   (((self.b)**2 - 4*self.a*self.c)*(-1)) 
            nc1 = f"Raízes complexas {(-self.b)/(2*self.a)} ± {(nc)/(2*self.a)}i"
            return nc1  
        x1 =  float(-self.b + ((self.b)**2 - 4*self.a*self.c)**(1/2))/(2*self.a)
        x2 =  float(-self.b - ((self.b)**2 - 4*self.a*self.c)**(1/2))/(2*self.a)

        
            
        return f" As raízes sao : {x1:.1f} e {x2:.1f}"


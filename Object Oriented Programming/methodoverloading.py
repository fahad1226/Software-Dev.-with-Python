

class A:

    def sum(self,a= None,b=None,c=None):

        s = 0
        if a != None and b != None and c!=None:

            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a
        return s





a = A()
res = a.sum(20,45,34) # method overloading ,ekhane sum(a,b) o dite parbo
print(res)

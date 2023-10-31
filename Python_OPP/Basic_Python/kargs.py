def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s =%s" % (key, value))
 
 
# Driver code
myFun("Name", first='MD Nur Hasan', dpt='CSE', year='1st')
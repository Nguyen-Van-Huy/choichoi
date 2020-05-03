def outerFunction():
    global a
    a=20
    def innerFunction():
        global a
        a=30
        print('a =' ,a)
a=10
outerFunction()
print('a= ',a)

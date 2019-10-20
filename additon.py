def getNonnegativeNum():
    while True:
        num = int(input('Please enter integer to add.\n'));
        if num>=0:
            return num
        else:
            print('Please enter non negative number')
    


while True:
    first = getNonnegativeNum()
    sec = getNonnegativeNum()

    print('Result is %d\n\n\n'%(first+sec))




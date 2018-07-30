def error1():
    try:
        print('Are you OK?')
        a = 'a'
        b = chr(a) 
        i = 10 /0
        print('I\'m OK!')
    except ZeroDivisionError as e:
        print('I\'m not OK because some exception.')
        print(e)
    except Exception as e:
        print('I\'m not OK because an unknown exception.')
        raise e
    finally:
        print('Finally there is silence...')

def error2():
    for i in range(10):
        print(i)
        assert i!=5, print('i==5')


if(__name__ == '__main__'):
    try:
        error1()
    except Exception as e:
        print(e)    

    error2()

i=1




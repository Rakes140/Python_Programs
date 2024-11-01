def func1():
    try:
        list = [3,2,6,9]
        i = int(input("enter the index: "))
        print(list[i])
        return 1
    
    except:
        print("some error occurred")
        return 0

    finally: 
        print("I am always executed")


x = func1()
print(x)

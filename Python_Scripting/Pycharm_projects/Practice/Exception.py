a = 1
b = 1
try:
    print("Open the resources")
    print(a/2)
    int()
except ZeroDivisionError as e:
    print("Can not Devide by zero: ", e)
except ValueError as e:
    print("Can not covert char to int")
except Exception as e:
    print("General exception ", e)
else:
    print("Reached else block")
finally:
    print("Close the resources")
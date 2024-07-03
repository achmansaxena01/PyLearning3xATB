# try , except and finally
try:
    # code
    file = open('example.txt', 'r')
    print(file.read())
except FileNotFoundError as fnf:
    print("I am not able to find the file,Please check the path")
finally:
    print("Executed")
    try:
        file.close()
    except NameError as ne:
        print(ne)

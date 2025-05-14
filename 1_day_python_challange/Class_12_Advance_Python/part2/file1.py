try:
    with open("1.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)             #OUtput: [Errno 2] No such file or directory: '1.txt'


try:
    with open("2.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)             #OUtput: [Errno 2] No such file or directory: '2.txt'

try:
    with open("3.txt" , "r") as f:
        print(f.read())
except Exception as e:
    print(e)             #OUtput: [Errno 2] No such file or directory: '3.txt'
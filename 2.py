def check_password(a, b):
    return True if a == b else False

def main():
    a = input("Input your password: ")
    b = input("Verify your password: ")

    result = check_password(a, b)



if __name__ == '__main__':
    main()
def calc_even_numbers(num1, num2, num3):
    count = 0
    if num1 % 2 == 0:
        count += 1
    if num2 % 2 == 0:
        count += 1
    if num3 % 2 == 0:
        count += 1
    return count

def main():
    num1, num2, num3 = int(input()), int(input()), int(input())

    result = calc_even_numbers(num1, num2, num3)
    result = f"The number contains {result} even numbers"

    print(result)

if __name__ == '__main__':
    main()
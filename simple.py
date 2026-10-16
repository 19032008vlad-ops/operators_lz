import math
def is_simple(number):
        for i in range(2,int(math.sqrt(number))):
             if number % i == 0:
                  return False
        return True


def main():
    string = input("Enter a number: ").split()

    n = int(string[0])
    if not (1 <= n <= 25):
        print("Error a number: 1 ≤ n ≤ 25")
        return 1
    if is_simple(n):
     print("Y")
    else:
     print("N")
     

main()
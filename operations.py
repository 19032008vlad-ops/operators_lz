import math
def operation(number):
    return math.ceil(number/3) 
         
         

def main():
    string = input("Enter a number: ").split()
    n = int(string[0])
    if not (1 <= n <= 100000):
            print("Error a number: 1 ≤ n ≤ 25")
            return 1
    print(operation(n))
    

main()
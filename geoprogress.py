def progressi(parameters):
     b = int(parameters[0]) #first_element
     n = int(parameters[2]) #last_element
     q = int(parameters[1]) #mnogitel_progressy
     result = int (b * (q**n - 1) / (q - 1))
     return result

def main():
  string = input("Enter three number with probel: ").split()
  b = int(string[0])
  q = int(string[1])
  n = int(string[2])
  if not (-10000 <= b <= 10000):
        print("Error first number: -10_000 ≤ b ≤ 10_000")
        return 1
  if not (1 <= q <= 50):
        print("Error second number: 1 ≤ q ≤ 50")
        return 1
  if not (2 <= n <= 100):
        print("Error third number: 2 ≤ n ≤ 100")
        return 1
  print(progressi(string))



main()
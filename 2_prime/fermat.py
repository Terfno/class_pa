import math
import random
import time

def getTime():
  return time.time()

def isPrime(n):
  if n==2:
    return True
  if n==1 or n%2==0:
    return False

  for _ in range(10):
    a = random.randint(2, n - 1)

    if gcd(n, a) != 1:
      return False

    if pow(a, n - 1, n) != 1:
      return False

  return True

def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a

def main():
  inputnum = int(input("input 1 integer: "))
  
  startTime = getTime()
  if(isPrime(inputnum)):
    print("Probably prime")
    print("calc time: " + str(getTime() - startTime) + "[ms]")
    return 0
  
  print("calc time: " + str(getTime() - startTime) + "[ms]")
  print("composite")

main()

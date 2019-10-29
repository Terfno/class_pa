import math
import time

def getTime():
  return time.time()

def isPrime(a):
  if a==1:
    return False
  
  if a==2:
    return True

  if a%2==0:
    return False

  ra = int(math.sqrt(a))

  for i in range(3,ra,1):
    if i == 1:
      continue
    if a%i==0:
      return False
  
  return True

def main():
  inputnum = int(input("input 1 integer: "))
  
  startTime = getTime()
  if(isPrime(inputnum)):
    print("Yes. Prime number.")
    print("calc time: " + str(getTime() - startTime) + "[ms]")
    return 0
  
  print("calc time: " + str(getTime() - startTime) + "[ms]")
  print("No. not Prime number.")

main()

import math
import random
import time

def getTime():
  return time.time()

def isPrime(p):
  if p==2:
    return True
  if p==1 or p%2==0:
    return False

  for _ in range(10): # 試行10回
    y = random.randint(2, p-1) # step1 choose y randomly(1<y<p)

    if gcd(p, y) != 1: return False # step2 gcd(p,y)!=1, p is a composite number.

    if pow(y, p-1, p) != 1: return False # step3 y^{p-1}≡k!=1, p is a composite number.

  return True

def gcd(a, b): # 前回作ったユークリッド互除法によるgcd
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

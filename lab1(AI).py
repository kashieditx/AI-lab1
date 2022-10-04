                  #Activity 1


n = int(input("Enter a number "))
if n%2==0:
    print("The Given is an even number")
else:
    print("The Given is an odd number")


              #Activity2


sum = 0
s=input("Eneter an Integer")
n = int(s)


while n!=0:
    sum = sum+n
    n = int(input("Enter an Integer  :"))
        
    

print("sum of Given Number is  ", sum)



         #Activity3

isPrime = True
i=2
n= int(input("Enter a Number: "))
while i<n:
    rem = n%i
    if rem==0:
        isPrime =False
        break
    else :
        i=i+1
if isPrime:
    print("Number is Prime")
else:
    print("Number is not Prime")

    


                          #Activity4


suum =0
i=0

while i<=4:
      s=int(input("enter a number"))
      suum = suum +n
      i=i+1
print("sum :  ",suum)



                         #Activity5



name = input('What is your name? ') 
print('Hello ' + name)
job = input('What is your job? ') 
print('Your job is ' + job)
num = input('Give me a number? ') 
print('You said: ' + str(num))




                        #Activity6



import random
# Awroken
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print("Alright...")
while RUNNING:
    GUESS = raw_input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
       print("Wrong, too low.")
    elif int(GUESS) > NUMBER:
       print("Wrong, too high.") 
    elif GUESS.lower() == "exit":
       print("Better luck next time.")
    elif int(GUESS) == NUMBER:
       print(("Yes, that's the one, %s.") % str(NUMBER))
    if TRY < 2:
       print (("Impressive, only %s tries.") % str(TRY))
    elif TRY > 2 and TRY < 10:
       print(("Pretty good, %s tries.") % str(TRY))
    else:
       print(("Bad, %s tries.") % str(TRY))
    RUNNING = False
    TRY += 1





                 #Task 1


numb = int(input("Enter a number "))
temp = numb
reverse=0
while temp>0:
    digit = temp%10
    reverse= digit + reverse*10
    temp= int(temp/10)
print("Reverse of",numb,"is",reverse)



         #Task 2

sum = 0 

i =0

while i<4:
    
    num = int (input("Enter a Number :"))
    if num%2==0:
      sum= sum+num
    i=i+1

print("sum of Even Number is  ", sum)



         #Task 3


num=int(input(' Terms to be displayed :'))

fibonacci=(0,1)

for i in range(2,num):
    
    fibonacci +=(fibonacci[i-2] + fibonacci[i-1] , )

print(fibonacci)



          #Task 4


num = int(input("Enter  Marks between 1 & 100: "))

if (num>=91):
    print("You got Grade 'A' ")
elif num>=81 and n<91:
    print("You got Grade 'B' ")
elif num>=71 and n<81:
    print("You got Grade 'C' ")
elif num>=61 and n<71:
    print("You got Grade 'D' ")
elif num>=50 and n<61:
    print("You got Grade 'E' ")
else:
    print("Sorry! Better luck next time ")


          #Task 5


num = int(input("Enter  Number: "))
facto = 1
for i in range(1, num + 1):
    facto = facto * i
print("factorial of ", num, " is ", facto)



#Challenge Questions

# for i in range(1,11,1):
#     print(i)

# print(9/2, 9%2)

# for i in range(35, 58, 1):
#     if i != 47 and i != 50:
#         print(i)

# for i in range(35,47,1):
#     print(i)

# firstinput = input('enter the first name')
# secondinput = input('enter the second name')

# if len(firstinput) > len(secondinput):
#     print(firstinput.upper())
#     print(secondinput.lower())
# if len(firstinput) < len(secondinput):
#     print(secondinput.upper())
#     print(firstinput.lower())
# if len(firstinput) == len(secondinput):
#     print(firstinput.upper())
#     print(secondinput.upper())

# integers = (1,2,3,4,5,6,7,7,9,10)
# # integers.count(x)
# # print(x)
# for x in integers:
#     integers.count(x)
#     # print(x)
# # integers.count(1)

# x=1
# while True:
#     print(x**2)
#     # x+=1
#     if x >= 512:
#         break

# data = {1: 'a', 2: 'b', 3: 'c'}
# for x in data:
#     strings = ''.join(data[x])
#     print(strings.upper())

# sentence = 'YoungWonks online Coding Class'
# print(sentence[0].split())
# print(sentence[2].split())
# import random
# count = 0
# listx = []
# listx.append(40)
# listx.append(120)
# for x in range(1,9,1):
#     integers = random.randint(40,120)
#     listx.append(integers)
# print(listx)
# dictionaryx = {}
# for x in range(1,10,1):
#     dictionaryx[count]=x
#     count =+ count
 

num = int(input("enter an integer: "))

if num > 1:
  
    for i in range(2, int(num/2)+1):
  
        if (num % i) == 0:
            print(num, "You entered a composite number")
            break
    else:
        print(num, "You entered a prime number")
  
else:
    print(num, "You entered a composite number (1 is not a prime number)")


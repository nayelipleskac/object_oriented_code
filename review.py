
# for x in range(10,-6,-1):
#     print(x)
# print('complete')

# names = [['John', 'Stuart'],  ['Alice', 'Goldman'], ['Mike', 'Smith'], ['Hannah', 'Johnson']]
# for x in names:
#     print(len(names[0][0]))

#     lenght = len(names[0][0]+ names[0][1])
#     for y in range(len(names)[0][0], len(names)[3][1]):
        
fruits = ["Apple", "Banana", "Pear", "Apple", "Pineapple", "Apple", "Pear", "Guava", "Grapes", "Watermelon"]
appleC=fruits.count('Apple')

fruitdic = {'Apple': appleC, 'Banana': [], 'Pear': []}
# fruitdic.append(fruits[0])

for x in fruits:

    count=fruits.count('Apple')
    fruitdic[fruits].append(count )


print(fruitdic)


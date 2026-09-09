my_list = [1,2,3,4,5,6,7,8,9,10]

for number in my_list:
    print(number)
    
for number in my_list:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
      
addition = 0
for number in my_list:
    addition += number
    print(addition)
    
    
# for index, number in enumerate(list(range(0, 101, 10))):
    # print (index, number)
for number in enumerate(list(range(0, 101, 10))):
    print(number)

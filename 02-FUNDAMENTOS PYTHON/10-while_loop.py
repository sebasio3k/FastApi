# Do while loop     

counter = 0
while True:
    counter += 1
    print(f"{counter} - I'm a infinite loop")
    if counter == 5:
        break
    
counter2 = 1
while counter2 <= 5:
    print(f"Number: {counter2}")
    counter2 += 1
else:
    print("End of the loop")
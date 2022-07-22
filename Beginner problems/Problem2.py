import random
number = random.randint(0,100)
print(number)
for i in range(0,3):
    prediction = int(input("Predict a number between 0 and 100: "))
    if prediction == number :
        print('Congratulations, your prediction is RIGHT!')
        break
    else:
        if i==2:
            print("You have run out of chances, the randomely generated number was: ", number)
            break
        if prediction < number :
            print('The number you are looking for is higher than your last prediction.')
        else :
            print('The number you are looking for is lower than your last prediction.')

    


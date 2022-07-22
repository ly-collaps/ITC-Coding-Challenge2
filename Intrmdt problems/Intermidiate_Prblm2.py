numbers = input("Please entre a list of numbers: ")
list = numbers.split()
for number in list   :
    if  list.count(number) > 1 :
        print('1 (Cycle)')
        break
    else:
        print("0 (Pas de cycle)")
        break

#PROBLEM, it doesnt go untill the last set of numbers 

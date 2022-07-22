array = input("please enter an array of numbers: ")
reversedArray= array[::-1]
if array == reversedArray:
    print("The array [",array, "] is palindrome")
else:
    print("The array [",array, "] is not palindrome")



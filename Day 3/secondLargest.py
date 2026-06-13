l = [10, 5, 8, 20, 15]

largest = 0
second = 0

for num in l:

    # If current number is bigger than largest
    if num > largest:

        # old largest becomes second largest
        second = largest

        # current number becomes largest
        largest = num

    # If number is between largest and second largest
    elif num > second and num != largest:
        second = num


print(second)
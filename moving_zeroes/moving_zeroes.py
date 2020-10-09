'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    no_zero = True
    for num in arr:
        if num == 0:
            no_zero = False
    if no_zero == True:
        return arr

    index = 0
    while index < (len(arr) - 1):
        if arr[index] == 0:
            for i in range(index + 1, len(arr)):
                if arr[i] != 0:
                    arr[index], arr[i] = arr[i], arr[index]
        index += 1

    return arr




    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
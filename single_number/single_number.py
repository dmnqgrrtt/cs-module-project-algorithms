'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    count = 2
    index = 0
    while count == 2:
        for num in arr:
            if arr[index] == num:
                count -= 1
        if count == 0:
            count = 2
            index += 1
        else:
            return arr[index]

    



    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
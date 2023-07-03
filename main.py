def insert_at_middle(arr, pos, val):
    """Function to add value to given position of an array."""
    i = len(arr)-1
    arr.append(None)
    # shift elements to right
    while pos <= i:
        arr[i+1] = arr[i]
        i -= 1   
    arr[pos] = val

    return arr

def insert_to_sorted(arr, val):
    """Function to add value to the sorted array."""
    for i in range(0, len(arr)):
        if arr[i] > val:
            temp = arr[i:] # copy right elements of the array
            arr[i] = val
            del arr[i+1:] # delete right elements from the array
            arr.extend(temp) # merge two arrays
            return arr
    arr.append(val)
    return arr

if __name__ == "__main__":
    temp = [3,7,8,9]
    temp2 = [5,11,4,7]
    print(insert_at_middle(temp2, 2, 2))
    print(insert_to_sorted(temp, 5))
    print(insert_to_sorted(temp, 10))
    print(insert_to_sorted(temp, 1))
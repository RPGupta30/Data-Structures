def BinarySearchRecursive(number_list,number_to_find,left_index,right_index):

    if left_index > right_index:
        return -1

    mid_index =(left_index+right_index)//2
    mid_number = number_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return BinarySearchRecursive(number_list, number_to_find, left_index, right_index)


if __name__ == '__main__':

    number_list = [1,3,4,8,12,15,19,32,36,45,49]
    number_to_find = 45
    left_index = 0
    right_index = len(number_list) - 1

    bsr = BinarySearchRecursive(number_list,number_to_find,left_index,right_index)
    print(f'Number is obtained at index {bsr}')



def BinarySearch(number_list,numbet_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0

    while left_index<=right_index:
        mid_index = (left_index+right_index)//2
        mid_number = number_list[mid_index]

        if mid_number == numbet_to_find:
            return mid_index

        if mid_number < numbet_to_find:
            left_index = mid_index+1

        else:
            right_index = mid_index-1

    return -1


if __name__ == '__main__':

    number_list = [2,5,7,10,13,14,18,19,23,28,31]
    number_to_find = 7
    bs = BinarySearch(number_list,number_to_find)
    print('The position of the number is {} in the list'.format(bs))
# Store all first line numbers in array
conditions = input().strip().split(' ')

# Store all second line numbers in array
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def left_shift(array, num_left_shifts):
    """ Input: Un-shifted array, number of left shifts to perform
        Output: None. Global array is changed. """
    for step in range(num_left_shifts):
        temp = int(array[0])
        array.append(temp)
        array.pop(0)
    
    
def format_answer(answer_array):
    """ Input: Array with correct index values for solution
        Output: String that is correctly formatted for the challenge."""
    ans_string = ""  
    
    for num in arr:
        ans_string += str(num) + " "
        
    ans_string.strip(" ")
    return ans_string

left_shift(arr, int(conditions[1]))
ans = format_answer(arr)
    
print(ans)
def sum_odd_numbers(low, high):
    ### WRITE YOUR ANSWER BELOW
    if low%2!=0:
        while low <= high:
            low=low+low+2
    else:
        low=low+1
        while low<=high:
            low=low+low+2
    return low

sum_odd_numbers(1,6)       
            

        
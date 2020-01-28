def average_some_numbers():
    ### WRITE YOUR ANSWER BELOW
    times=0
    total_number=0
    number=input('Enter a number or type "bye" to average:')
    while number != "bye":
        times=times+1
        total_number=total_number+int(number)
        number=input('Enter a number or type "bye" to average:')
    return print ('the average is ' + str(total_number/times))

average_some_numbers()
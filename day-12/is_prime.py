# Check if provided number is a prime one, or not (only divided by 1 and by itself)

def is_prime(num):

    non_remainder_list = []
    for number in range(1,num+1):
        if num % number == 0:
            non_remainder_list.append(number)
    if len(non_remainder_list) == 2:
        return True
    else:
        return False


# --------- another way -------------
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True

is_prime(13)
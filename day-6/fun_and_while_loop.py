# short introductions to while loops and functions

def add_num(a, b):
    sum = a + b
    return sum

num_list = input("Provide two numbers separated with space that you want to add up: ").split()
num_list = [int(x) for x in num_list]
sum_num = add_num(num_list[0],num_list[1])
print(sum_num)

# while loops - they will be executed as lons as they return True

ten = 0
while ten < 10:
    ten+=1
    print(ten)



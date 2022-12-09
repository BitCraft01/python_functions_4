# Exercise 1
def max_num(x, y, z):
    return max([x, y, z])


print(max_num(7, 8, 3))

# Exercise 2


def mult_list(num_list):
    product = 1
    for num in num_list:
        product = product * num
    return product


print(mult_list([4, -8, 16]))

# Exercise 3


def rev_string(my_str):
    return my_str[::-1]


print(rev_string("Bachir"))

# Exercise 4


def num_within(num, range_start, range_end):
    if num >= range_start and num <= range_end:
        return True
    else:
        return False


print(num_within(4, 15, 23))
print(num_within(46, 33, 78))

# Exercise 5
triangle = [[1], [1, 1]]


def pascal(n):
    if n < 1:
        print("Not enough rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)


pascal(4)
pascal(13)
pascal(7)

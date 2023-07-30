input_num = int(input())
sum_num = input_num
sum_of_squares = abs(input_num ** 2)
while sum_num != 0:
    if sum_num == 0:
        break
    else:
        input_num = int(input())
        sum_num += input_num
        sum_of_squares += abs(input_num) ** 2
print(sum_of_squares)

# Print the ratios of positive, negative and zero values in the list(array).
# Each value should be printed on a separate line with  digits after the decimal.
# The function should not return a value.

def plus_minus(array):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for number in array:
        if number < 0:
            negative += 1
        if number == 0:
            zero += 1
        if number > 0:
            positive += 1
    proportion_of_positive = round(positive / len(array), 6)
    proportion_of_negative = round(negative / len(array), 6)
    proportion_of_zero = round(zero / len(array), 6)

    print(proportion_of_positive)
    print(proportion_of_negative)
    print(proportion_of_zero)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)

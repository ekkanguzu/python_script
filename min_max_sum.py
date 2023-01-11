
# Given an list(array) [1, 2, 3, 4, 5]
# mini is 1 + 2 + 3 + 4
# max is 2 + 3 + 4 + 5


def mini_max_sum(array):
    # Write your code here
    mini = array[0:-1]
    maxi = array[1: len(array)]

    mini_result = sum(mini)
    maxi_result = sum(maxi)

    # for mi in mini:
    #    mini_result += mi
    # for ma in maxi:
    #    maxi_result += ma

    print(mini_result, maxi_result)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
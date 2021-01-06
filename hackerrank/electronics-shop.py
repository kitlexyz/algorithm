"""
https://www.hackerrank.com/challenges/electronics-shop/problem
explanation: https://kitle.xyz/post/146/

"""
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    sum = -1
    for keyboard in keyboards:
        if keyboard < b:
            for drive in drives:
                if drive < b and keyboard + drive <= b and sum < (keyboard + drive):
                        sum = keyboard + drive
    return sum


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)

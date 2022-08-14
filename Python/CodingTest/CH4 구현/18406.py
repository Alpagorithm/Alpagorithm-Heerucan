n = list(input())
half = int(len(n)/2)


def findsum(array):
    result = 0
    for i in array:
        result += int(i)
    return result


if findsum(n[:half]) != findsum(n[half:]):
    print("READY")
else:
    print("LUCKY")
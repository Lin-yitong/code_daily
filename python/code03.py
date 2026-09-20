
nums = [10,20,30]

# for num in nums:
    # print(num)

it = iter(nums)
# print(it)
# print(type(it))
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


class CountToThree:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 3:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountToThree()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
#
# for num in counter:
#     print(num)


def count(n):
    i = 1

    while i <= n:
        yield i
        i += 1

g = count(3)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

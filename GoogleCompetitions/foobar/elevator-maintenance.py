def solution(l):
    nums = list(map(lambda x: x.split('.'), l))
    nums.sort(key=lambda x: (int(x[0]), int(x[1]) if len(
        x) >= 2 else -1, int(x[2]) if len(x) >= 3 else -1))
    nums = list(map(lambda x: '.'.join(x), nums))
    return nums


x = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
p = solution(x)

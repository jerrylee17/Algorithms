def solve(n, arr):
    total = 0
    curr = arr[0]
    for a in arr[1:]:
        if a > curr:
            print(curr, total)
            curr = a
            continue
        else:
            digits_diff = len(str(curr)) - len(str(a))
            total += digits_diff
            if int(str(curr)[:len(str(a))]) > a:
                total += 1
                curr = int(str(a) + '0'*(digits_diff + 1))
            else:
                # last digit of A matches curr's cutoff digit
                if str(a)[-1] == str(curr)[len(str(a)) - 1]:
                    # Equal --> append 0
                    if a == curr:
                        total += 1
                        curr = int(str(a) + '0'*(digits_diff + 1))
                    # No more space for appending --> append 0
                    elif curr + 1 > int(str(a) + '9'*(digits_diff)):
                        total += 1
                        curr = int(str(a) + '0'*(digits_diff + 1))
                    # Same substring
                    elif str(a) == str(curr)[:len(str(a))]:
                        curr += 1
                    else:
                        curr = int(str(a) + '0'*(digits_diff))
                else:
                    curr = int(str(a) + '0'*(digits_diff))
        print(curr, total)
    return total


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = solve(n, arr)
    print(f'Case #{i+1}: {res}')

#Tasks
def countGoodSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]
        if a != b and b != c and a != c:
            count += 1
    return count

if __name__ == '__main__':
    s = input().strip()
    print(countGoodSubstrings(s))
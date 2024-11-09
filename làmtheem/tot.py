n,t,s = map(int,input().split())
lst = list(map(int,input().split()))
if 1 <= n <= 100 and 1 <= t <= 100 and 360 <= s <= 1200:
    for i in lst:
        if i == s:
            print(s + (t/2))
        if 0 < i - s < 60:
            k = s + (i - s)
            h = (t - (i - s)) / 2
            print(k + h)
        if 0 < s - i < 60:
            k = i + ( s - i)
            h = (t - (s - i)) / 2
            print(k + h)

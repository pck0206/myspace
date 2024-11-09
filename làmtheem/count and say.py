def countAndSay( n: int):
    say = str(n)
    count = 0
    if len(say) == 1:
        say = say.replace(say[0],"1")
        count += 1
    while count != n:
        for i in say:
            if ((len(say) == 2 and len(set(say)) == 1) or len(say) == 1) and count != n:
                say = say.replace(i * say.count(i),str(say.count(i)) + i)
                count += 1
            elif count != n:
                say = say.replace(i * say.count(i),str(say.count(i)) + i)
                count += 0.5
            else:
                break
    return say
n = 5
print(countAndSay(n))
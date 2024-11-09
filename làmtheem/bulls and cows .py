def getHint(secret, guess):
    dc_s = {}
    dc_g = {}
    countA = 0
    countB = 0 
    for i in secret:
        dc_s[i] = dc_s.get(i,0) + 1
    for i in guess:
        dc_g[i] = dc_g.get(i,0) + 1
    for i in range(len(guess)):
        if guess[i] in secret and secret[i] == guess[i] and guess[i] in dc_g and guess[i] in dc_s:
            countA += 1
            dc_g[guess[i]] -= 1
            dc_s[guess[i]] -= 1
            if dc_g[guess[i]] == 0 or dc_s[guess[i]] == 0:
                del dc_g[guess[i]]
                del dc_s[guess[i]]
    for i in range(len(guess)):
        if (guess[i] in secret and secret[i] != guess[i]) and guess[i] in dc_g and guess[i] in dc_s:
            countB += 1
            dc_g[guess[i]] -= 1
            dc_s[guess[i]] -= 1
            if dc_g[guess[i]] == 0 or dc_s[guess[i]] == 0:
                del dc_g[guess[i]]
                del dc_s[guess[i]]

    result = str(countA) + "A" + str(countB) + "B"
    return result


print(getHint("1122","1222"))



""" Part 1 """
def checkPswd(pswd):
    # Check 1 - No decreasing
    currentVal = 0
    for i in pswd:
        if int(i) >= currentVal:
            currentVal = int(i)
        else:
            return False

    # Check 2 - Double adjacent digits
    pairs = [pswd[i:i+2] for i in range(0, len(pswd), 1)]

    doubleCheck = False
    for p in pairs:
        try:
            if p[0] == p[1]:
                return True
        except:
            pass

    if doubleCheck == False:
        return False
    else:
        return True

count = 0
for pswds in range(357253, 892943):
    if checkPswd(str(pswds)):
        count += 1
print(count)

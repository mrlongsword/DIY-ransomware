import random
def generate_key():
    key = ""
    charset=[]
    for i in range(48,124):
        if (i>=48 and i<=57) or (i>= 65 and i<= 90) or (i>=97 and i<=122):
            charset.append(chr(i))

    for i in range(128):
        index = random.randint(0,61)
        key+=charset[index]
    return key


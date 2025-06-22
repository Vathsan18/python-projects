def encript(m,s):
    global l
    dis = ""
    for i in msg:
        ni = l.index(i) + s
        if ni > len(l) - 1:
            ni -= len(l)
        dis += l[ni]
    print(dis)

def decript(m, s):
    global l
    dis = ""
    for i in msg:
        ni = l.index(i) - s
        if ni < 0:
            ni += len(l)
        dis += l[ni]
    print(dis)

l = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

task = int(input('''
    Type 1 - Encode
         2 - Decode\n'''))
while task in [1,2]:
    msg = input("Type the message \n").lower()
    sn = int(input("Enter the shift number \n"))
    if task == 1:
        encript(msg, sn)
    else:
        decript(msg, sn)
    c = input("continue??")
    if c.lower() == "y":
        pass
    else:
        break

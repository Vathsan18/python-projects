import random

def pick():
    cl = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cl)

def cal_score(l):
    if sum(l) == 21 and len(l) == 2:
        return 0
    if 11 in l and sum(l) > 21:
        l.remove(11)
        l.append(1)
    return sum(l)

def conclude(u, c):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "You won"
    elif c_score == 0:
        return "You lost"
    elif u_score > 21:
        return "You lost"
    elif c_score > 21:
        return "You won"
    elif u_score > c_score :
        return "You won"
    else:
        return "You lost"

is_ge = False
ul = []
cl = []

for _ in range(2):
    ul.append(pick())
    cl.append(pick())

while not is_ge:
    u_score = cal_score(ul)
    c_score = cal_score(cl)

    print(f"user cards are {ul} and score is {u_score}")
    print(f"onr of computer card is {cl[0]}")

    if u_score == 0 or c_score == 0 or u_score > 21:
        is_ge = True
    else:
        if input("do you want to pick another card ?").lower() == 'y':
            ul.append(pick())
            print()
        else:
            is_ge = True

while c_score != 0 and c_score < 17:
    cl.append(pick())
    c_score = cal_score(cl)

print()
print(f"your cards are {ul} and score is {u_score}")
print(f"computer cards are {cl} and score is {c_score}")
print(conclude(u_score , c_score))

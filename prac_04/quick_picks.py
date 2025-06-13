import random

NUM_QUICK_PICKS = int(input("How many quick picks:"))
MIN_NUMBER = 1
MAX_NUMBER = 45

for _ in range(NUM_QUICK_PICKS):
    quick_pick = []

    while len(quick_pick) < 6:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)

    quick_pick.sort()

    formatted_quick_pick = " ".join("{:2}".format(num) for num in quick_pick)

    print(formatted_quick_pick)
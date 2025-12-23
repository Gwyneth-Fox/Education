import pandas as pd
import random

def choose_date():
    date = []
    day = 0
    month = random.choice(["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July" "Aug.", "Sept.", "Oct.", "Nov.", "Dec."])
    if month == "Jan.":
        day = random.randint(1,31)
    elif month == "Feb.":
        day = random.randint(1, 28)
    elif month == "Mar.":
        day = random.randint(1, 31)
    elif month == "Apr.":
        day = random.randint(1, 30)
    elif month == "May":
        day = random.randint(1, 31)
    elif month == "June":
        day = random.randint(1, 30)
    elif month == "July":
        day = random.randint(1, 31)
    elif month == "Aug.":
        day = random.randint(1, 31)
    elif month == "Sept.":
        day = random.randint(1, 30)
    elif month == "Oct.":
        day = random.randint(1, 31)
    elif month == "Nov.":
        day = random.randint(1, 30)
    elif month == "Dec.":
        day = random.randint(1, 31)
    date.append(month)
    date.append(day)
    return date


data = []

for i in range(10000):
    count = 0 
    chosen_dates = []
    current_chosen_date = choose_date()
    not_done = True
    chosen_dates.append(current_chosen_date)
    while not_done:
        if len(chosen_dates) > 1:
            if current_chosen_date in chosen_dates[0:(len(chosen_dates) - 1)]:
                d = {"Number of days":count}
                count = 0
                not_done = False
            else:
                count += 1
        current_chosen_date = choose_date()
        chosen_dates.append(current_chosen_date)

    data.append(d)

df = pd.DataFrame(data)
df



marks  = {
    "Aman": 40,
    "Naman": 50,
    "Kabir": 60
}

# inverted = {value : key for key, value in marks.items()}

# print(inverted)


###m2
inverted = {}
for name, score in marks.items():
    if score not in inverted:
        inverted[score] = []

    inverted[score].append(name)

print(inverted)


####m3

from collections import defaultdict

def invert_safe(d):
    result = defaultdict(list)
    for key, value in d.items():
        result[value].append(key)
    return dict(result)

fav_color = {"Rahul": "blue", "Priya": "red", "Aman": "blue", "Neha": "red", "Karan": "green"}

print(invert_safe(fav_color))
    

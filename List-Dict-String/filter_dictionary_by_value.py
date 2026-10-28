# def filter_dict(d, condition):
#     return{key: value for key, value in d.items()  if condition(value)}

# marks = {"Rahul": 85, "Priya": 92, "Aman": 40, "Neha": 67, "Karan": 33}

# passed = filter_dict(marks, lambda v: v>50)
# print(passed)

# print(marks)

marks = {"Rahul": 85, "Priya": 92, "Aman": 40, "Neha": 67, "Karan": 33}

passed = {
    name:score 
    for name, score in marks.items() 
    if score >=50
}

print(passed)
records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]

"""
for r in records:   # O(n) over the number of records
    if r[1] == dept:
        print(r[0])
""" 
# initialize index
dept_idx = {}

def add_dept_idx(name, dept):
    if dept not in dept_idx:
        dept_idx[dept] = []

    dept_idx[dept].append(name)
    
# build up initial index
for name, dept in records:
    if dept not in dept_idx:
        dept_idx[dept] = []
    
    dept_idx[dept].append(name)

# Who are all the people working in the apt?
# What is the key? Dept
# What is the value? list of names

print(dept_idx["Engineering"])
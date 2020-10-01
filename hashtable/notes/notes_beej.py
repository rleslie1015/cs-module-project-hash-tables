table = [None] * 8

class HashEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __repr__(self):
		return f"HashEntry({repr(self.key)},{repr(self.value)})"

def hashf(s):
	"""Naive hashing function--do not use!"""
	total = 0

	bytes = str(s).encode()

	for b in bytes:  # O(n) over the length of the key/string s
		total += b

		# If this is a 64-bit hash, add this line:
		#total &= 0xffffffffffffffff

		# If this is a 32-bit hash, add this line:
		#total &= 0xffffffff


	return total

def get_index(s):
	value = hashf(s)

	return value % len(table)

def put(key, value):
	"""
	O(n) over the length (number of bytes) of the key
	O(1) over the number of items in the table
	"""
	index = get_index(key)
	table[index] = HashEntry(key, value)

def get(key):
	index = get_index(key)
	hash_entry = table[index]

	return hash_entry.value

put("Beej", 3490)

print(table)

put("Goats!", 9999)

print(table)

print(get("Beej"))  # 3490
print(get("Goats!"))  # 9999

# add a cache dict
cache = {}


def fib(n):
	if n<= 1: return n
	# if not in cache put it in cache
	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)
	# return it
	return cache[n]

for i in range(100):
	print(f'{i:3} {fib(i)}')

d = {
	'foo': 1,
	'bar': 2,
	'boo': 3
}
## sort dict by key
# makde dict into list
items = list(d.items())

items.sort(key=lambda t: t[1])

print(items)
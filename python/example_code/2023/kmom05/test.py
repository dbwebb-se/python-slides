from operator import itemgetter

warehouse = {
    "köttfärs" : 20,
    "grädde" : 80,
    "krossade tomater": 33,
    "gul lök" : 42
}

print(warehouse)
print(warehouse["köttfärs"])

warehouse["köttfärs"] = 35
print(warehouse["köttfärs"])

warehouse["bröd"] = 22
print(warehouse)

print(warehouse.keys())
print(warehouse.items())

print(sorted(warehouse.items()))
print(sorted(warehouse.items(), reverse=True))

print(sorted(warehouse.items(), key=itemgetter(0)))
print()
print(warehouse.items())
print(sorted(warehouse.items(), key=itemgetter(1), reverse=True))

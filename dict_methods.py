marks ={"harry": 98, "sally": 100, "john": 95, "jane": 90}
print(marks.keys())
print(marks.values())
print(marks.items())
marks.pop("john")
print("After removing John:", marks)
marks.clear()
print("After clearing all entries:", marks)

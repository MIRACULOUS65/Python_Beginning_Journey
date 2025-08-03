marks=[2,45,6,7,8,97,6,8,9]
marks_extend=[1,2,3]

marks.append(100)  # adding an element to the end of the list
print(marks)
marks.insert(2, 55)  # inserting an element at index 2
print(marks) 
marks.remove(6)  # removing the first occurrence of 6
print(marks)    
marks.pop()  # removing the last element
print(marks)
marks.sort()  # sorting the list in ascending order
print(marks)
marks.extend(marks_extend)  # extending the list with another list
print(marks)
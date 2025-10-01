questions=[
    ["colour of the sky","blue","green",1],
    ["colour of water","colourless","blue",1]
]

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")

    a=int(input("enter your answer. 1 for a, 2 for b"))
    if(question[3]==a):
        print("correct ans")
    else:
        print(f"incorrect ans , correct ans is : {question[3]}")
        print("better luck next time!")
        break

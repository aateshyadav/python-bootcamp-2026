questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["\nWhat is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["\nWhich planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["\nWhat is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["\nWho wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["\nWhat is the square root of 64?", "8", "10", "6", "12", 1],
    ["\nWhich country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["\nWho painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["\nWhat is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["\nWhich ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["\nWhat is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i = 0 
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer correct or not
    contestant_answer=int(input("enter the number -> 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5]==contestant_answer):
        print("correct answer")
    else:
        print("incorrect,  the correct answer was {question[5]}")
        print("better luck next time!")
        break
    print(f"You won {prizes[i]}")
    i +=1    

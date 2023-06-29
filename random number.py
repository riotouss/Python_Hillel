import random

def guess_number_game():
    number = random.randint(1, 100)
    
    print("Хай! Я загадав число від 1 до 100. Спробуй вгадати число.")
    
    while True:
        guess = int(input("Введи своє число "))
        
        if guess < number:
            print("Загадане число більше")
        elif guess > number:
            print("Загадане число менше")
        else:
            print("Ура! ти вгадав :)")
            break

guess_number_game()

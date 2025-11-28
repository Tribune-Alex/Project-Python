import random
import time
name = input('Hello, What is your name? ').capitalize()
print(f"Hello {name}. Now we will play very funny game which call HANGMAN")
print()
time.sleep(3)
print("The soft will choose some word and you must gues it. \n GOOD LUCK")
print()

time.sleep(3)



def gues_what():
        words = ['car', 'motobike', 'human', 'animal', 'apple', 'banana', 'juice', 'computer', 'python', 'dog','cat']
        random_word = random.choice(words)
        chossen_word = ["_"] * len(random_word)
        life = len(random_word) + 3
        used_letters =set()
        print(f"Now you see hidden word {chossen_word} which contains {len(random_word)} letters \n So I will give you {life} chances to gues it")
        print()
        while life > 0:
            user_letter = input("Enter the letter: ").lower()
            
            if not user_letter.isalpha() or len(user_letter) !=1:
                  print("Enter only one letter")
                  continue
            
            if user_letter in used_letters:
                  print(f"You have already used {user_letter}")
                  continue
            
            used_letters.add(user_letter)

            if user_letter in random_word:
                  print("Well done")
                  for i,char in enumerate(random_word):
                        if char == user_letter:
                         chossen_word[i] = user_letter
                         print(chossen_word)
            else:
               print(f"There is no {user_letter.upper()} in word")
               life -= 1
               print(f"Now you have {life} chances")

            if life < len(chossen_word):
                 print(f"Looks like the remaining chances are not enough to guess the words. \n Unfortunately you lose, the word was {random_word.upper()}")
                 break

            if life == 1:
                 print(f"Be carefull you have only {life} chance")

            if "_" not in chossen_word:
                 print(f"Congratulation {name} you WIN, that was {random_word.upper()}")
                 break
        else:
         print(f"Unfortunately you lose, the word was {random_word.upper()}")              
            


                     
        
        

        
        

gues_what()
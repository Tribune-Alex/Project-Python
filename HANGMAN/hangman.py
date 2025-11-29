import random
import time
name = input('Hello, What is your name? ').capitalize()
print(f"Hello {name}. Now we will play very funny game which call HANGMAN")
print()
time.sleep(3)
print("The soft will choose some word and you must gues it. \n GOOD LUCK")
print()

time.sleep(3)

def load_words(filename):
     with open(filename, 'r') as file:
      lines = file.readlines()
      words =[]
     for line in lines:
      w = line.strip().lower()
      if w and w.isalpha():
       words.append(w)
       

     return words     


def gues_what():
 print(f'There are 3 categories: 1-Cities, 2-Movies and 3-Animals\n Choose one of them')

 choice = int(input("Your Choise: "))
 if choice == 1:
  return 'cities.txt'
 elif choice == 2:
  return 'movies.txt'
 elif choice == 3:
  return 'animals.txt'
 else:
  print("In this way the words will be from category 'OTHERS'")
  return 'others.txt'
             
       

filename = gues_what()
words = load_words(filename)
random_word = random.choice(words)
chossen_word = "_" * len(random_word)
life = 5
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
                  letters = list(chossen_word)
                  for i,char in enumerate(random_word):
                        if char == user_letter:
                         letters[i] = user_letter.upper()
                         chossen_word = "".join(letters)
                         print(chossen_word)
            else:
               print(f"There is no {user_letter.upper()} in word")
               life -= 1
               print(f"Now you have {life} chances")

            if life == 1:
                 print(f"Be carefull you have only {life} chance")

            if "_" not in chossen_word:
                 print(f"Congratulation {name} you WIN, that was {random_word.upper()}")
                 break
else:
    print(f"Unfortunately you lose, the word was {random_word.upper()}")              

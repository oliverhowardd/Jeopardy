import requests
import random

response = requests.get('http://jservice.io/api/clues?category=139').json()

score = 0


randomNumber = random.randint(0, len(response))
responseElement = response[randomNumber]
question = responseElement["question"]
print("*********")
pointValue = responseElement["value"]
print("This question is worth " + str(score) + " points!")
answer = responseElement["answer"]
print(answer)
userAnswer = input(question)
print(userAnswer)

if userAnswer == answer:
    print("CORRECT")
    score += pointValue
else:
    print("INCORRECT")
    score -= pointValue

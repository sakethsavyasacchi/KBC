questions = [["Who is known as the 'Father of the Nation' in India?"],
             ["Which planet is known as the 'Red Planet'?"],
             ["Who invented the telephone?"],
             ["Which Indian city is known as the 'Pink City'?"],
             ["Who wrote the Indian National Anthem?"],
             ["Which gas do plants absorb from the atmosphere?"],
             ["Which country gifted the Statue of Liberty to the USA?"],
             ["Who was the first woman Prime Minister of India?"],
             ["Which Indian cricketer is known as the 'Master Blaster'?"],
             ["Which is the highest civilian award in India?", "Padma Shri"]]

options = [
    [
        "Sardar Patel", "Subhas Chandra Bose", "Mahatma Gandhi",
        "Jawaharlal Nehru"
    ], ["Mars", "Jupiter", "Saturn", "None"],
    ["Alexander Graham Bell", "Nikola Tesla", "None"],
    ["Udaipur", "Jaipur", "Bikaner", "None"],
    ["Bankim Chandra Chattopadhyay", "Sarojini Naidu", "Subhash Chandra Bose"],
    ["Nitrogen", "Carbon Dioxide", "Hydrogen", "None"],
    ["Germany", "France", "Italy", "Spain", "None"],
    ["Indira Gandhi", "Sonia Gandhi", "Sarojini Naidu", "Pratibha Patil"],
    ["Virat Kohli", "Sourav Ganguly", "MS Dhoni", "Sachin Tendulkar"],
    ["Padma Shri", "Padma Bhushan", "Bharat Ratna", "Padma Vibhushan"]
]

correctanswers = [3, 1, 1, 2, 4, 2, 2, 1, 4, 3]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(len(questions)):
  question = questions[i][0]
  print(
      f"For level {i+1} you have to answer the following question for Rs. {levels[i]}"
  )
  print(f"Question is: {question}")
  print(f"Here are your options:")
  for j in range(len(options[i])):
    print(f"{j+1}. {options[i][j]}")
  reply = int(input("Enter your answer (1-4) or Enter 0 to quit:"))
  if reply == 0:
    print("Thanks for playing!")
    if i == 10:
      print("Congratulations! You have won 320000!")
      break
    elif i==4:
      print("Congratulations! You have won 10000!")
    elif 4<i<8:
      print("Congratulations! You have won 80000!")
    break
  elif reply == correctanswers[i]:
    print(f"Correct answer! You have won Rs. {levels[i]}")
    money = levels[i]
    break

# wow look at this ridiculously inefficient and dumb code wow
# I want to rewrite this

name = input('Enter your name, hero: ')
print(name + ". Wake up, " + name + '.')
print("Hyrule needs a new hero.")
print()

print("You're in Ordon village. You can see Jackie in the distance. You should go up and say hello, " + name + '.')
print('a. Go up to Jackie')
print("b. Go to the town hall")
introduction = input('Which of the above would you like to do?')
print()

if introduction == 'a':
  print('You walked up to Jackie.')
  print()
  print("Jackie: Hi, " + name + "! Hey, I see that you don't have an Ordon Sword yet. You need to go get one! Go get the Ordon Sword from Erica at the town hall!")
  print()
  print('a. Go to the town hall')
  getting_ordon_sword = input('Where would you like to go now?')
  print()
  
  ordon_sword = str(" Ordon Sword ")
  
  if getting_ordon_sword == 'a':
    print("You are now at town hall. There's Erica.")
    print()
    print("Erica: Hello, " + name + ". Wait a minute. You don't have the" + ordon_sword + "! It's dangerous to go alone!!")
    print("Erica: The" + ordon_sword + "only costs 100 rupees. How many rupees do you have?")
    print()
    rupees = int(input("How many rupees do you have?"))
    print()
    
    if rupees == 100:
      print("Erica: Wow! Exact change! Well, here you go!")
      print("You got the" + ordon_sword + ".")
      print()
      print("a. Thank Erica")
      print("b. Go outside to show Jackie the" + ordon_sword)
      print("c. Swing the" + ordon_sword)
      
      got_the_sword = input('What do you want to do now?')
      print()
      
      if got_the_sword == 'a':
        print("Erica: No problem! I'm glad that you like it.")
        print()
      
      if got_the_sword == 'b':
        print("You are now outside.")
        print()
        print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
        print()

      if got_the_sword == 'c':
        print("You swung the" + ordon_sword)
        print()
        print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
        print()
        
    if rupees > 100:
      print("Erica: Alright, let me give you the change. I need to give you " + str(rupees-100) + " rupees back.")
      print("Erica: Here you go, and here's the" + ordon_sword + "!")
      print()
      print("Erica gave you " + str(rupees-100) + " rupees.")
      print("You got the" + ordon_sword + ".")
      print()
      print("a. Thank Erica")
      print("b. Go outside to show Jackie the" + ordon_sword)
      print("c. Swing the" + ordon_sword)
      
      got_the_sword = input('What do you want to do now?')
      print()
      
      if got_the_sword == 'a':
        print("Erica: No problem! I'm glad that you like it.")
        print()
      
      if got_the_sword == 'b':
        print("You are now outside.")
        print()
        print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
        print()
      
      if got_the_sword == 'c':
        print("You swung the" + ordon_sword)
        print()
        print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
        print()
      
    if rupees < 100: 
      print("Erica: Wait a minute! That's not enough. Hmph. Well, I'll give you the" + ordon_sword + "for now, but you're in debt!")
      print()
      print("You got the" + ordon_sword + ".")
      print("You are now in " + str(100-rupees) + " rupees of debt, which you owe to Erica.")
      print()
      print("a. Thank Erica")
      print("b. Go outside to show Jackie the" + ordon_sword)
      print("c. Swing the" + ordon_sword)
      
      got_the_sword = input('What do you want to do now?')
      print()
      
      if got_the_sword == 'a':
        print("Erica: No problem! I'm glad that you like it.")
        print()
      
      if got_the_sword == 'b':
        print("You are now outside.")
        print()
        print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
        print()
      
      if got_the_sword == 'c':
        print("You swung the" + ordon_sword)
        print()
        print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
        print()

if introduction == 'b':
  print("You are now at town hall. There's Erica.")
  print()
  ordon_sword = str(" Ordon Sword ")
  print("Erica: Hello, " + name + ". Wait a minute. You don't have the" + ordon_sword + "! It's dangerous to go alone!!")
  print("Erica: The" + ordon_sword + "only costs 100 rupees. How many rupees do you have?")
  print()
  rupees = int(input("How many rupees do you have?"))
  print()
  
  if rupees == 100:
    print("Erica: Wow! Exact change! Well, here you go!")
    print("You got the" + ordon_sword + ".")
    print()
    print("a. Thank Erica")
    print("b. Go outside to show Jackie the" + ordon_sword)
    print("c. Swing the" + ordon_sword)
    
    got_the_sword = input('What do you want to do now?')
    print()
    
    if got_the_sword == 'a':
      print("Erica: No problem! I'm glad that you like it.")
      print()
    
    if got_the_sword == 'b':
      print("You are now outside.")
      print()
      print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
      print()
    
    if got_the_sword == 'c':
      print("You swung the" + ordon_sword)
      print()
      print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
      print()
      
  if rupees > 100:
    print("Erica: Alright, let me give you the change. I need to give you " + str(rupees-100) + " rupees back.")
    print("Erica: Here you go, and here's the" + ordon_sword + "!")
    print()
    print("Erica gave you " + str(rupees-100) + " rupees.")
    print("You got the" + ordon_sword + ".")
    print()
    print("a. Thank Erica")
    print("b. Go outside to show Jackie the" + ordon_sword)
    print("c. Swing the" + ordon_sword)
    
    got_the_sword = input('What do you want to do now?')
    print()
    
    if got_the_sword == 'a':
      print("Erica: No problem! I'm glad that you like it.")
      print()
    
    if got_the_sword == 'b':
      print("You are now outside.")
      print()
      print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
      print()
    
    if got_the_sword == 'c':
      print("You swung the" + ordon_sword)
      print()
      print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
      print()
    
  if rupees < 100: 
    print("Erica: Wait a minute! That's not enough. Hmph. Well, I'll give you the" + ordon_sword + "for now, but you're in debt!")
    print()
    print("You got the" + ordon_sword + ".")
    print("You are now in " + str(100-rupees) + " rupees of debt, which you owe to Erica.")
    print()
    print("a. Thank Erica")
    print("b. Go outside to show Jackie the" + ordon_sword)
    print("c. Swing the" + ordon_sword)
    
    got_the_sword = input('What do you want to do now?')
    print()
    
    if got_the_sword == 'a':
      print("Erica: No problem! I'm glad that you like it.")
      print()
    
    if got_the_sword == 'b':
      print("You are now outside.")
      print()
      print("Jackie: Wow! I told you the" + ordon_sword + "would be great! You're really a hero now, " + name + " !")
      print()
    
    if got_the_sword == 'c':
      print("You swung the" + ordon_sword)
      print()
      print("Erica: Wow, you're good at handling the" + ordon_sword + "!")
      print()

print("You have awoken, " + name + ". Hyrule awaits.")
print()

print("You are in Ordon village, wielding the Ordon Sword.")
print("Oh no! You were robbed!! All your money is gone!!")
print("Erica: " + name + ", what's wrong. Huh? What do you mean you were robbed?! That's horrible! I'll tell you what, if you had any debt on me, I clear it all away!!")
print("Erica: No need to thank me. I'm here to help, " + name + "!")
print()

rupees = int(0)

print("You now have 0 rupees.")
print("You need to find some way to get more rupees. Try looking for some way to get some.")
print()
print("a. Beg Jackie for money.")
print("b. Beg Erica for money.")
print("c. Break that pot over there. It belongs to Ayesha, and she won't give you money the easy way.")
print("d. Cut some grass. You could become a part-time lawnmower.")
get_rupees = input("Which of the above would you like to do?")
print()
if get_rupees == "a":
  print("Jackie: Hmm? You need rupees. Gah, here you go, " + name + ". I suppose a hero needs all the help they can get.")
  rupees = rupees + 20
  print()
  print("Jackie gave you 20 rupees. You now have " + str(rupees) + " rupees.")

elif get_rupees == "b":
  print("Erica: Huh? Well, I'm sorry, " + name + ", but I can't give you any. You'll have to find some rupees yourself.")
  print("You now have " + str(rupees) + " rupees.")

elif get_rupees == "c":
  print("Heh, heh. Good choice, " + name + ". Ayesha was never nice to you anyway.")
  print("The pot broke open. How nice.")
  rupees = rupees + 20
  print("You now have " + str(rupees) + " rupees.")

elif get_rupees == "d":
  print("Well, I suppose all heroes have to do some honest hard work.")
  print("You swung the Ordon Sword.")
  print("Sweet. Grass has money in it.")
  rupees = rupees + 10
  print("You now have " + str(rupees) + " rupees.")

print()
print("Jackie: " + name + "!! I have a quest for you!! The Gorons of Death Mountain are terrified!")
print("Jackie: Mr. Seidel, their leader, has disappeared into the mountain, and threatens to fight anyone that goes in after him!")
print("Jackie: " + name + ", You're the only one that can save the Gorons from Mr. Seidel's wrath, but you'll need a Hylian Shield to face him.")
print()
print("Erica came outside to join you and Jackie.")
print()
print("Erica: Are you talking about the Hylian Shield? I can give you one for just 300 rupees!")
print("Jackie: That's perfect! " + name + ", you're going to have to find that many rupees!!")
print()
print("You have at least started getting some rupees, which is a good start. Maybe you could go play Jasmine's game.")
print()

print("a. Play Jasmine's game.")
play_game = input("What would you like to do?")

if play_game == "a":
  print("You are now inside of Jasmine's Game Emporium.")
  print("Jasmine: Welcome! Welcome! How are you today, " + name + "?")
  print()
  print("a. I'm fine, thank you.")
  print("b. Eh? Why do you care?!")
  being_nice = input("What do you want to say to Jasmine?")
  print()
  if being_nice == "a":
    print("Jasmine: It is good to see you, " + name + "! Well, then would you like a chance to win 300 rupees?")
    print("Jasmine: Ah, I knew you would! Well step right up and play Jasmine's Game!!")
    print()
    print("Jasmine: Now the game is, you have to guess the number, which is from 1 to 50, I am thinking of in 3 tries!")
    secret_number = int(47)
    print("Jasmine: Alright, I have decided on my secret number! Try guessing now!")
    print()
    
    guess_1 = int(input("What do you think the secret number is?"))
    print()
    if guess_1 == secret_number:
      print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
      print("Jasmine: I can hardly believe it!")
      print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
      rupees = rupees + 300
      print()
      print("You now have " + str(rupees) + " rupees.")
      print()
      print("You are now outside.")
      print("Jackie: Wow! You won Jasmine's game! I knew you would!")
      print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
      print()
      print("You gave Erica " + str(rupees) + " rupees.")
      print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
      print("Erica gave you " + str(rupees-300) + ".")
      print()
      print("You now have the Hylian Shield.")
      print()
      print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
      print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      
    elif (guess_1 > secret_number) and (guess_1 <= 50): 
      print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
      print("Jasmine: Why don't you try again, " + name + ".")
      print()
      guess_2 = int(input("What do you think the secret number is?"))
      print()
      if guess_2 == secret_number:
        print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
        print("Jasmine: I can hardly believe it!")
        print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
        rupees = rupees + 300
        print()
        print("You now have " + str(rupees) + " rupees.")
        print()
        print("You are now outside.")
        print("Jackie: Wow! You won Jasmine's game! I knew you would!")
        print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
        print()
        print("You gave Erica " + str(rupees) + " rupees.")
        print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
        print("Erica gave you " + str(rupees-300) + ".")
        print()
        print("You now have the Hylian Shield.")
        print()
        print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
        print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      elif (guess_2 > secret_number) and (guess_2 <= 50): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      elif (guess_2 < secret_number) and (guess_2 >= 1): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      else:
        print("Jasmine: Hmm? Well if you're not going to play by the rules, then I don't wish to play the game with you!!")
        print("You are now outside.")
        print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
        print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
        print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
        print()
        print("GAME OVER")
          
    elif (guess_1 < secret_number) and (guess_1 >= 1): 
      print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
      print("Jasmine: Why don't you try again, " + name + ".")
      print()
      guess_2 = int(input("What do you think the secret number is?"))
      print()
      if guess_2 == secret_number:
        print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
        print("Jasmine: I can hardly believe it!")
        print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
        rupees = rupees + 300
        print()
        print("You now have " + str(rupees) + " rupees.")
        print()
        print("You are now outside.")
        print("Jackie: Wow! You won Jasmine's game! I knew you would!")
        print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
        print()
        print("You gave Erica " + str(rupees) + " rupees.")
        print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
        print("Erica gave you " + str(rupees-300) + ".")
        print()
        print("You now have the Hylian Shield.")
        print()
        print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
        print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      elif (guess_2 > secret_number) and (guess_2 <= 50): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      elif (guess_2 < secret_number) and (guess_2 >= 1): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      else:
        print("Jasmine: Hmm? Well if you're not going to play by the rules, then I don't wish to play the game with you!!")
        print("You are now outside.")
        print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
        print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
        print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
        print()
        print("GAME OVER")
      
    else: #guess 1 else
      print("Jasmine: Hmm? Well if you're not going to play by the rules, then I don't wish to play the game with you!!")
      print("You are now outside.")
      print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
      print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
      print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
      print()
      print("GAME OVER")

  if being_nice == "b":
    print("Jasmine: Why, how rude of you! Hmph! Well, if you're here to play my Game, I certainly hope you don't win!!")
    print("Jasmine: Now the game is, you have to guess the number, which is from 1 to 50, I am thinking of in 3 tries!")
    secret_number = int(47)
    print("Jasmine: Alright, I have decided on my secret number! Try guessing now!")
    print()
    
    guess_1 = int(input("What do you think the secret number is?"))
    print()
    if guess_1 == secret_number:
      print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
      print("Jasmine: I can hardly believe it!")
      print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
      rupees = rupees + 300
      print()
      print("You now have " + str(rupees) + " rupees.")
      print()
      print("You are now outside.")
      print("Jackie: Wow! You won Jasmine's game! I knew you would!")
      print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
      print()
      print("You gave Erica " + str(rupees) + " rupees.")
      print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
      print("Erica gave you " + str(rupees-300) + ".")
      print()
      print("You now have the Hylian Shield.")
      print()
      print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
      print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      
    elif (guess_1 > secret_number) and (guess_1 <= 50): 
      print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
      print("Jasmine: Why don't you try again, " + name + ".")
      print()
      guess_2 = int(input("What do you think the secret number is?"))
      print()
      if guess_2 == secret_number:
        print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
        print("Jasmine: I can hardly believe it!")
        print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
        rupees = rupees + 300
        print()
        print("You now have " + str(rupees) + " rupees.")
        print()
        print("You are now outside.")
        print("Jackie: Wow! You won Jasmine's game! I knew you would!")
        print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
        print()
        print("You gave Erica " + str(rupees) + " rupees.")
        print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
        print("Erica gave you " + str(rupees-300) + ".")
        print()
        print("You now have the Hylian Shield.")
        print()
        print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
        print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      elif (guess_2 > secret_number) and (guess_2 <= 50): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      elif (guess_2 < secret_number) and (guess_2 >= 1): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
          
    elif (guess_1 < secret_number) and (guess_1 >= 1): 
      print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
      print("Jasmine: Why don't you try again, " + name + ".")
      print()
      guess_2 = int(input("What do you think the secret number is?"))
      print()
      if guess_2 == secret_number:
        print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
        print("Jasmine: I can hardly believe it!")
        print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
        rupees = rupees + 300
        print()
        print("You now have " + str(rupees) + " rupees.")
        print()
        print("You are now outside.")
        print("Jackie: Wow! You won Jasmine's game! I knew you would!")
        print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
        print()
        print("You gave Erica " + str(rupees) + " rupees.")
        print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
        print("Erica gave you " + str(rupees-300) + ".")
        print()
        print("You now have the Hylian Shield.")
        print()
        print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
        print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
      elif (guess_2 > secret_number) and (guess_2 <= 50): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is lower than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      elif (guess_2 < secret_number) and (guess_2 >= 1): 
        print("Jasmine: Nope! That's not the number I'm thinking of! My number is higher than that!")
        print("Jasmine: Why don't you try again, " + name + ".")
        print()
        guess_3 = int(input("What do you think the secret number is?"))
        print()
        if guess_3 == secret_number:
          print("Jasmine: What?!?! How did you do that?! You got it right! The secret number was " + str(secret_number) + "!!")
          print("Jasmine: I can hardly believe it!")
          print("Jasmine: Well, you win the game! Here's the 300 rupees!!")
          rupees = rupees + 300
          print()
          print("You now have " + str(rupees) + " rupees.")
          print()
          print("You are now outside.")
          print("Jackie: Wow! You won Jasmine's game! I knew you would!")
          print("Erica: Yay! Now then, the Hylian Shield is worth 300 rupees.")
          print()
          print("You gave Erica " + str(rupees) + " rupees.")
          print("Let's see. That means I need to give you " + str(rupees-300) + " rupees back.")
          print("Erica gave you " + str(rupees-300) + ".")
          print()
          print("You now have the Hylian Shield.")
          print()
          print("Jackie: Now you can face Mr. Seidel!! Go on, " + name + "! I know you'll be able to defeat him!")
          print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
        elif guess_3 != secret_number:
          print("Jasmine: Well now, I'm sorry, " + name + ", but that's your third try. You didn't get my number right.")
          print("Jasmine: I'm quite sorry. But do play the game again if you wish later!")
          print()
          print("You are now outside.")
          print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
          print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
          print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
          print()
          print("GAME OVER")
      
    else: 
      print("Jasmine: Hmm? Well if you're not going to play by the rules, then I don't wish to play the game with you!!")
      print("You are now outside.")
      print("Jackie: What happened, " + name + "? Did you not win Jasmine's game?")
      print("Erica: Oh dear, I guess that means you can't buy the Hylian Shield.")
      print("Jackie: Don't worry, " + name + "! I'm sure you'll be able to get enough rupees to get the Hylian Shield!!")
      print()
      print("GAME OVER")

print("Jackie: " + name + "!! What are you waiting for? We must go defeat Mr. Seidel and save the Gorons from his wrath.")
print("Erica: Indeed! " + name + " even has the Hylian Shield, so we can surely beat him!")
print("Jackie: Off to the Death Mountains!!")
print()
time.sleep(1)

print("a. Jackie")
print("b. Erica")
print("c. Jasmine")
print("d. Ayesha")
print("e. All of the above! I need all the help I can get!!")
go_to_death_mountain = input("Who would you like to take with you?")
print()

if go_to_death_mountain == "a":
  print("Jackie: Yeah! Let's go, " + name + "! I swear my life to your cause, hero!!")
  print()
  time.sleep(1)
  print("You and Jackie head off towards Death Mountain on Epona.")
  print()
  time.sleep(1)
  print("After a grueling horse ride listening to Jackie's dad jokes, you finally make it to the Death Mountains.")
  print("Wait a minute!! You hear a sound in the bushes over there.")
  print("You take out the Ordon Sword and get ready to strike.")
  print("Jackie: Who's there?!")
  time.sleep(1)
  print("???: Aarghhh! I've had enough of Ayesha's terrible puns!")
  print()
  time.sleep(1)
  print("Erica, Jasmine, and Ayesha come out of the bushes.")
  print()
  time.sleep(1)
  print("Jackie: What are you all doing here?!")
  print("Erica: No need to thank us! We knew you would need all the help you could get!")

if go_to_death_mountain == "b":
  print("Erica: Alright! " + name + ", we're going to destroy Mr. Seidel!!")
  print()
  time.sleep(1)
  print("You and Erica head off towards Death Mountain on Epona.")
  print()
  time.sleep(1)
  print("After a grueling horse ride listening to Erica's dad jokes, you finally make it to the Death Mountains.")
  print("Wait a minute!! You hear a sound in the bushes over there.")
  print("You take out the Ordon Sword and get ready to strike.")
  print("Erica: Who's there?!")
  time.sleep(1)
  print("???: Aarghhh! I've had enough of Ayesha's terrible puns!")
  print()
  time.sleep(1)
  print("Jackie, Jasmine, and Ayesha come out of the bushes.")
  print()
  time.sleep(1)
  print("Erica: What are you all doing here?!")
  print("Ayesha: No need to thank us! We knew you would need all the help you could get!")

if go_to_death_mountain == "c":
  print("Jasmine: Are you sure? Money is my only superpower. Also take care of Jasmine at all costs.")
  print("Jasmine is top priority, okay?")
  print()
  time.sleep(1)
  print("You and Jasmine head off towards Death Mountain on Epona.")
  print()
  time.sleep(1)
  print("After a pleasant horse ride listening to Jasmine's good jokes, you finally make it to the Death Mountains.")
  print("Wait a minute!! You hear a sound in the bushes over there.")
  print("You take out the Ordon Sword and get ready to strike.")
  print("Jasmine: Who's there?!")
  time.sleep(1)
  print("???: Aarghhh! I've had enough of Ayesha's terrible puns!")
  print()
  time.sleep(1)
  print("Jackie, Erica, and Ayesha come out of the bushes.")
  print()
  time.sleep(1)
  print("Jasmine: What are you all doing here?!")
  print("Erica: No need to thank us! We knew you would need all the help you could get!")

if go_to_death_mountain == "d":
  print("Ayesha: Let's go!! " + name + ", I'll do everything in my power to obliterate Mr. Seidel!!")
  print()
  time.sleep(1)
  print("You and Ayesha head off towards Death Mountain on Epona.")
  print()
  time.sleep(1)
  print("After a grueling horse ride listening to Ayesha's dad jokes and terrible puns, you finally make it to the Death Mountains.")
  print("Wait a minute!! You hear a sound in the bushes over there.")
  print("You take out the Ordon Sword and get ready to strike.")
  print("Ayesha: Who's there?!")
  time.sleep(1)
  print("???: Aarghhh! I've had enough of Erica's terrible puns!")
  print()
  time.sleep(1)
  print("Erica, Jasmine, and Jackie come out of the bushes.")
  print()
  time.sleep(1)
  print("Ayesha: What are you all doing here?!")
  print("Erica: No need to thank us! We knew you would need all the help you could get!")

if go_to_death_mountain == "e":
  print("All of them: Let's go!!")
  print("After a grueling horse ride listening to Ayesha's dad jokes and terrible puns, you finally make it to the Death Mountains.")

print()
print("Jackie: Arm yourselves! We need to go into the mountains before facing Mr. Seidel.")
time.sleep(1)
print()
print("You make your way into the Death Mountains with your friends.")
time.sleep(2)
print("As you head in to the heart of the dark mountain, the only light in the tunnels is from the Goron lanterns.")
print("You equip the Ordon Sword and Hylian Shield, and your friends ready themselves to fight.")
print()
advice = input("Do you have any advice for your friends for facing Mr. Seidel?")
#needed to break up the text

print("Erica: That's a good idea!")
print("Ayesha: We should keep that in mind when in battle.")


print()
time.sleep(1)
print("Jackie: Hmm, I can't see anyone. Maybe Mr. Seidel is deeper in the mountain?...")
time.sleep(1)
print("You all look in dread behind Jackie.")
print()
time.sleep(1)
print("Ayesha: J-Jackie. L-look behind you.")
print("Jackie turns around slowly, her soul withering in fear.")
time.sleep(1)
print(".")
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print("You all freeze with fear at the sight of Mr. Seidel wielding a chromebook, a giant Python at his side.")
time.sleep(3)
print()

print("Erica: We need to fight!! Get ready!")
print("You have 50 HP to start with!")
print("Mr. Seidel has 1,000 HP!!")
user_hp = 50
seidel_hp = 1000
time.sleep(4)

print()
print("You are now in battle mode.")
print("Ayesha runs at Mr. Seidel, wielding a Hardware Assignment.")
print("Mr. Seidel burns Ayesha alive by grabbing the Hardware Assignment and setting it ablaze.")
print("Ayesha's HP drops drastically:")
for ayesha_hp in range(40, -1, -5):
  time.sleep(1)
  print(str(ayesha_hp))
print("You see the light fading from Ayesha's eyes, her third degree burns rendering her unhealable.")
print("Erica: *whispers* She looks so peaceful, like a piece of blackened burned toast.")
print()
time.sleep(2)
print("Erica makes a loud platypus noise!!")
print("Mr. Seidel's HP drops to " + str(seidel_hp - 500) + "HP!!")
seidel_hp = seidel_hp - 500
print()
time.sleep(3)
print("Jackie looks over at Mr. Seidel's chromebook.")
print("Mr. Seidel's HP drops to " + str(seidel_hp - 400) + "HP!!")
seidel_hp = seidel_hp - 400
print()
time.sleep(3)
print("You need to attack!!")
print("a. Program Exercise 2")
print("b. Make a flawless flowchart")
print("c. Do your Emerging Technology Assignment on Green Bullets")
print("d. Say Windows Vista CPU")
print()
attack1 = input("How would you like to attack?")

if attack1 == "a":
  print("You programmed Exercise 2, and put your heart and soul into it!")
  print("Mr. Seidel: Although Erica is a proper name, since you are choosing to use pot_hole_case, you still only use lowercase letters!!!")
  print("Your HP drops to 45!")
  print()
  user_hp = user_hp - 5

if attack1 == "b":
  print("You made a flawless flowchart and put your heart and soul into it!")
  print("Mr. Seidel: Does it have LIVE VIDEO?!?!?!")
  print("Your HP drops to 40!")
  print()
  user_hp = user_hp - 10

if attack1 == "c":
  print("You do your emerging tech assignment on Green Bullets, and put your heart and soul into the research!")
  print("Mr. Seidel: I cannot condone violence.")
  print("Mr. Seidel shoots you with a Green Bullet.")
  print("Your HP drops to 30!")
  print()
  user_hp = user_hp - 20
  
if attack1 == "d":
  print("You say Windows Vista CPU!! It was an honest mistake...")
  print("Mr. Seidel: W i N d O w S  v I s T a  C p U ? ! ? !")
  print("Your HP drops to 0!!!")
  print()
  user_hp = user_hp - 50

if user_hp == 0:
  time.sleep(4)
  print("You drop to your knees, struggling to take a breath.")
  time.sleep(1)
  print("You faintly hear a raccoon looking for cotton candy and smile slightly at the thought.")
  time.sleep(1)
  print("Your friends crowd around you, and you see your Learning Skills drop.")
  time.sleep(1)
  print("Farewell, brave " + name + ".")
  time.sleep(3)
  print("GAME OVER")
  import sys
  sys.exit()

print("Erica: Attack again! We need to keep fighting!")
print()
print("a. Fix your flowchart")
print("b. Do another Emerging Tech assignment in a single NIGHT")
print("c. Put your heart and soul into all the other exercises")
print("d. Memorize what CAPTCHA stands for")
attack2 = input("How would you like to attack?")
print()

if attack2 == "a":
  print("You fix your flowchart, and even add live video!")
  print("Mr. Seidel takes a massive blow!!")
  print("Mr. Seidel: *fixes stuff on feedback document*")
  print("Mr. Seidel's HP drops to 65!")
  for seidel_hp in range(100, 64, -5):
    time.sleep(1)
    print(str(seidel_hp))
  seidel_hp = 65

if attack2 == "b":
  print("You did another Emerging Tech assignment in a night! Very impressive, " + name + "!!")
  print("Mr. Seidel takes a massive blow!!")
  print("Mr. Seidel: *fixes stuff on feedback document*")
  print("Mr. Seidel's HP drops to 60!")
  for seidel_hp in range(100, 59, -5):
    time.sleep(1)
    print(str(seidel_hp))
  seidel_hp = 60

if attack2 == "c":
  print("You programmed all the exercises flawlessly!")
  print("Mr. Seidel takes a huge hit!!")
  print("Mr. Seidel: *fixes stuff on feedback document*")
  print("Mr. Seidel's HP drops to 65!")
  for seidel_hp in range(100, 64, -5):
    time.sleep(1)
    print(str(seidel_hp))
  seidel_hp = 65

if attack2 == "d":
  print("You scream at the top of your lungs: COMPLETELY AUTOMATED PUBLIC TURING TEST TO TELL COMPUTERS AND HUMANS APART!!!!")
  print("Mr. Seidel TAKES A CRITICAL HIT!!")
  print("Mr. Seidel: *fixes stuff on feedback document*")
  print("Mr. Seidel's HP drops to 50!")
  for seidel_hp in range(100, 49, -5):
    time.sleep(1)
    print(str(seidel_hp))
  seidel_hp = 50

time.sleep(2)
print()
print("Jasmine: Good work, " + name + "!! Keep fighting, I know you can defeat him!!")
print()

print("a. Say 'Why are you still here?'")
print("b. Actually prepare in advance for the interrogation.")
print("c. Don't put any acronyms in your assignment")
print("d. Refuse any appreciation")
print()

attack3 = input('How would you like to attack?')
print()

if attack3 == "a":
  print("You ask Mr. Seidel why he's still here!! It's super effective!!")
  print("Mr. Seidel TAKES A CRITICAL HIT!!")
  print("Mr. Seidel's HP DROPS TO ZERO!!")
  while seidel_hp >= 0:
    time.sleep(1)
    print(str(seidel_hp))
    seidel_hp = seidel_hp - 5
  seidel_hp = 0
    
if attack3 == "b":
  print("You actually prepared for the interrogation!!! Nothing can stop you now!")
  print("Mr. Seidel TAKES A CRITICAL HIT!!")
  print("Mr. Seidel's HP DROPS TO ZERO!!")
  while seidel_hp >= 0:
    time.sleep(1)
    print(str(seidel_hp))
    seidel_hp = seidel_hp - 5
  seidel_hp = 0

if attack3 == "c":
  print("HAHAHAHA! YOU DON'T HAVE TO KNOW WHAT ACRONYMS ARE IF YOU DON'T USE THEM!!")
  print("Mr. Seidel TAKES A CRITICAL HIT!!")
  print("Mr. Seidel's HP DROPS TO ZERO!!")
  while seidel_hp >= 0:
    time.sleep(1)
    print(str(seidel_hp))
    seidel_hp = seidel_hp - 5
  seidel_hp = 0
    
if attack3 == "d":
  print("You, with your soul of wurtzite boron nitride, refuse any appreciation! Your defence is IMPENETRABLE!!!")
  print("Mr. Seidel TAKES A CRITICAL HIT!!")
  print("Mr. Seidel's HP DROPS TO ZERO!!")
  while seidel_hp >= 0:
    time.sleep(1)
    print(str(seidel_hp))
    seidel_hp = seidel_hp - 5
  seidel_hp = 0

if seidel_hp == 0:
  print()
  time.sleep(4)
  print(name + "!! You defeated Mr. Seidel!!!")
  print()
  print("Jackie: You did it! The Gorons of Death Mountain are saved!!")
  print("Erica: You must decide what to do now!")
  print()
  print("a. Destroy Mr. Seidel")
  print("b. Spare his life!")
  print("c. Life imprisonnment")
  print("d. INTERROGATE MR. SEIDEL. THEN HE'LL KNOW HOW WE FEEL. THE YEARS OF TORTURE WILL BE RECOUPED.")
  print()
  ending = input("What have you decided?")
  print()
  
  if ending == "a":
    time.sleep(2)
    print("You decided to destroy Mr. Seidel.")
    print()
    print("Jackie: A terrible fate, but fitting all the same.")
    print("Jasmine: *TURNS MR. SEIDEL INTO A PIECE OF TOAST*")
    print()
    print("Jackie and Erica carry the piece of toast to a ceremonial toaster.")
    print("JACKIE AND ERICA TURN THE TOASTER ON HIGH AND BURN THE SEIDEL TOAST.")
    print()
    print("AYESHA RESPAWNS FROM THE SMELL OF TOAST, FROM THE INCREDIBLE TOAST HEALING ABILITY.")
    print()
    print("JACKIE, ERICA, JASMINE, AND AYESHA EAT THE SEIDEL TOAST, WHILE LAUGHING MANIACALLY!!!")
    time.sleep(3)
    print()
    print()
    print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
  
  if ending == "b": 
    print("You decided to spare Mr. Seidel. How noble of you, " + name + "!")
    print()
    print("Mr. Seidel can help you with your quest, with his chromebook and giant Python!")
    print()
    print("Jackie: Good choice, " + name + "! We need all the help we can get!")
    print()
    print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
  
  if ending == "c":
    print("You sentenced Mr. Seidel to life imprisonnment.")
    print()
    print("Jasmine: Life imprisonnment? That seems sort of harsh.")
    print("Jackie: If we sentence Mr. Seidel to life imprisonnment, who will lead the Gorons?")
    print("Ayesha: Erica should be the leader! She'd make a good dictator for them.")
    print("Jackie: But the Gorons like for and while loops, and Erica still hasn't figured them out.")
    print("Jasmine: Why don't the Gorons just have a constituional democracy?")
    print("Jackie: Good idea! That's what we'll do.")
    print()
    print("Your adventure will continue in another exercise. Farewell, for now, " + name + ".")
  
  if ending == "d":
    for communist_propaganda in range (1, int(user_hp), 1):
      print("SEIZE THE MEANS OF PRODUCTION.")
      print("YOU HAVE NOTHING TO LOSE BUT YOUR CHAINS.")
      print("ALL POWER TO THE SOVIETS.")
      print()
   

"""
Name(s): Veryan Johnson
Name of Project: Jungle Adventure Game
"""

#Write the main part of your program here. Use of the other pages is optional.
def start():
  print("You're about to fall asleep, but want to read a book. Do you try to fall asleep, or choose a book to read?\n")
  choice = input("Enter S to go to sleep and R to read: ")
  if choice == "S":
    sleep()
    river()
    pantherattack()
    panthercounterattackidiot()
  elif choice == "R":
    choosebook()

def sleep():
  print("\nYou fall into a deep sleep.")
  
def pantherattack():
  print("\nYou find yourself on a sunny beach. There is no one around, and behind you is the forest.\nYou are just trying to gauge the situation when a panther jumps out of the forest. It growls and begins to approach.")

def choosebook():
  print("\nYou look through your bookshelf for a suitably soporific tome. You browse through George Eliot, Shakespeare, and Tolstoy; knitting manuals, wilderness survival guides, and three volumes on the history of Serbia. You narrow it down to either the wilderness survival guide or Tolstoy. Which topic would you like to choose to put you to sleep?")
  choice = input("\nEnter T for Tolstoy or W for the wilderness guide: ")
  if choice == "T":
    sleep()
    river()
    pantherattack()
    panthercounterattackidiot()
  elif choice == "W":
    sleep()
    river()
    pantherattack()
    panthercounterattacksmart()
    poisonousberries()
def river():
  print("\nWhen you wake up, you find yourself in a forest with an ecclectic mix of tropical and pine trees. To one side of you, the forest stretches as far as you can see. To the other, you can hear a river flowing at the bottom of a deep gorge. Suddenly, you smell smoke and see flames rising from the trees ahead of you. You must cross the river to avoid the fire.\nYou look into the gorge and see a boat by the river with which to cross. There is also a bridge stretching across the gorge, but it looks unstable. How will you escape the fire?")
  choice = input("\nEnter B to try your luck on the bridge, or G to test your rowing skills in the river: ")
  if choice == "B":
    ropescourse()
  elif choice == "G":
    downstream()
def ropescourse():
  print("\nYou begin to gingerly cross the bridge, trying not to dislodge any of the precarious fixtures. It begins to creek more and more, and you can hear the wood cracking. You decide to make a run for it, and as soon as you reach the other side of the gorge, the bridge collapses behind you. You are left shaken but unharmed. You walk further into the woods on the other side of the gorge, in case the fire somehow crosses the river.")
def downstream():
  print("\nYou descend a narrow trail to reach the bottom of the gorge, where you find the boat. You push it into the water and jump in, rowing as fast as possible to get to the other side of the river. But the current is too strong, and you are swept downstream. Up ahead, you can see a waterfall, which you are quickly approaching. Do you jump out of the boat and hope to get to shore, or hope that the waterfall is short?")
  choice = input("\nEnter J to jump out of the boat, or S to stay on your current course: ")
  if choice == "J":
    swim()
  elif choice == "S":
    waterfall()
def swim():
  print("\nYou swim as fast as you can to the nearest land, where you climb out of the river, exhausted on the shore.")
def waterfall():
  print("\nYou get closer and closer to the waterfall until the boat hits the edge, standing there for a moment before the moment of truth. Then you and the boat go over the edge, oars and all, and you know this is the end.\n\nWhen you wake up, you are on dry land.")
def panthercounterattackidiot():
  print("\nYou panic, having no idea what to do. Perhaps you should have read the wilderness survival guide, instead of falling asleep or reading one of those other useless books. As the panther approaches, you make the idiotic decision to run for cover in the jungle. This provokes the panther, and the last thing you think you're ever going to see is the panther's jaws open wide--\nYou wake up suddenly in your own room, heart racing, and realize it was all a dream.")
def panthercounterattacksmart():
  print("\nYou tense and your heart races faster, but keep your cool. Remembering your knowledge from the useful wilderness survival guide you read, you know what to do. You stand up to the panther, becoming as threatening as possible to deter the beast. The panther backs away in fear, and you are able to stand your ground, unharmed.")
def poisonousberries():
  print("\nExhausted, you sit down in a small patch of strawberries. You're tired and hungry, but aren't sure whether the berries are really strawberries or not, and whether they are safe to eat. Will you take a chance on them, or go hungry?")
  choice = input("\nEnter E to eat the strawberries and H if you're hesitant to taste a potentially poisonous fruit: ")
  if choice == "E":
    poisoned()
  elif choice == "H":
    starved()
def poisoned():
  print("\nYou eat handfuls of the berries until there are none left. After a few minutes, you start to feel drowsy and your vision blurs. In another minute, you can't keep your eyes open anymore.\nYou wake up suddenly in your own room, and realize it was all a dream.")
def starved():
  print("\nYou resist the temptation to eat the likely poisonous berries, but can barely sit up from lack of energy. You fall to the ground, and the world goes dark.\nYou wake up suddenly in your own room, and realize it was all a dream.")
start()
#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

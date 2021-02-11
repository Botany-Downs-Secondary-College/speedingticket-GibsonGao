import math
#asking the big question
prisoner_list = ["Gibson", "Damian"]
#secret varible for use later
a = 0
again = "N"

#fine amount function using math floor
def fine_amount(x):

    return ((math.floor(x) - 100) * 10)


#selects which summar to use
def summary_number(x):
    if (x == 1):
        print("you were not speeding, move along")
    elif (x == 2):
        print(
            f"You have a fine amount of ${fine_amount(speed)} as you were {speed - 100}KM/h over the speed limit"
        )
    elif (x == 3):
        print(
            f"Your licensse is confiscated as you were {speed - 100}KM/h over the speed limit"
        )
    elif (x == 4):
        print(
            f"Your license is now invalid as you were {speed - 100}KM/h over the speed limit"
        )
    elif (x == 5):
        print(
            f"You now have a jail sentence as you were {speed - 100}KM/h over the speed limit"
        )
    else:
        print("unexpected error")
while True:
  while True:
    name = input("Please input your name ")
    count = prisoner_list.count(name)
    if count > 0:
        print("go jail")
    elif name == "N":
        print(prisoner_list)
    else:
        print("please input your speed")
        while True:
          try:
              speed = float(input())
              break
          except ValueError:
              print("please enter a Valid Number")
    break
    #logic checking if the input is a float
  #checking speed and and selecting summary
  if speed <= 100:
      print("Not speeding")
      a = 1

  elif speed > 100 and speed < 150:
      print(f"your fine amount is ${fine_amount(speed)}")
      a = 2
  elif speed >= 150 and speed < 160:
      print("license confiscated")
      a = 3
  elif speed >= 160 and speed < 180:
      print("license lost")
      a = 4
  elif speed >= 180:
      print("jail time")
      a = 5
  #asking the user if they want a summary
  summary = "no"
  summary = input("Whold you like to have your sumamry? ")
  if summary != "no":
      summary_number(a)
  else:
      print("ok")
  again = input("would you like to try again?(Y/N) ")
  while True:
    if again == "N":
      exit()
    elif again == "Y":
      break
    else :
      again = input("Y/N")
print("code executed goodbye")
    
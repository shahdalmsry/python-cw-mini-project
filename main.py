# write your code here
def padel_court_cost(court_type):
    if court_type == ("indoor") :
        return 30 
    elif court_type == ("outdoor") :
        return 20
print(padel_court_cost("indoor"))
print(padel_court_cost("outdoor"))


def rackets_costs(racket_brand):
    if racket_brand=="Bullpadel":
        return 100
    elif racket_brand== "Nox":
        return 140
    elif racket_brand=="Siux":
        return 200
print(rackets_costs("Bullpadel"))   
print(rackets_costs("Nox"))  
print(rackets_costs("Siux"))   


def padel_balls_cost(ball_boxes):
    if ball_boxes ==1:
        return 2
    elif ball_boxes ==2:
        return 3.5
    elif ball_boxes ==3:
        return 5
print(padel_balls_cost(1))    
print(padel_balls_cost(2))    
print(padel_balls_cost(3))    

def padel_game_cost():
  court_type=input("enter the court type")
  racket_brand=input(" enter the racket brand")
  ball_boxes=int(input("enter the number of ball boxes"))
  total=padel_court_cost(court_type) + rackets_costs(racket_brand) + padel_balls_cost(ball_boxes)
  return total
print(padel_game_cost())

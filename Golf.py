import random
import time
import os 
os.system('color')
class Golfbag:
  def __init__(self,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13): #just bag setup for now, need to add distances and miss percentage
    self.c1 = c1
    self.c2 = c2
    self.c3 = c3
    self.c4 = c4
    self.c5 = c5
    self.c6 = c6
    self.c7 = c7
    self.c8 = c8
    self.c9 = c9
    self.c10 = c10
    self.c11 = c11
    self.c12 = c12
    self.c13 = c13
    self.club_list = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13]

    
  def club_distance(self):
    bag_dist = {}
    dist_dict = {'lob wedge':range(15,36),'sand wedge':range(25,41),'gap wedge':range(50,101),'pitching wedge':range(125,156),'9 iron':range(130,166),'8 iron':range(150,176),'7 iron':range(165,186),'6 iron':range(180,196),'5 iron':range(195,211),'4 iron':range(210,221),'3 iron':range(225,241),'3 wood':range(235,261),'driver':range(250,301)}
    for club in self.club_list:
      if club in dist_dict.keys():
        bag_dist[club] = dist_dict[club] 
    return bag_dist
  def __repr__(self):
    return ('Bag:\n{}'.format(self.bag_dist))
  
  #####################################PLAYER##################################################################
  def player(self,hole):
    self.putt_counter = 0
    distance_remaining = (hole.length())
    print('You are playing a {} yard par {}.'.format(distance_remaining,hole.par))
    self.shot_number = 0
    while abs(distance_remaining) > 20:
      print('Distance remaining: {} yards'.format(distance_remaining))

      club = input('Choose a club from the following.\n\n{}\n:'.format(self.club_distance()))
      club = club.lower()
      club_range = list(self.club_distance()[club])
      hit = random.randint(club_range[0],club_range[-1])
      print('Your shot went {} yards.'.format(hit))
      distance_remaining-=hit
      distance_remaining = abs(distance_remaining)
      self.shot_number += 1
    print('{}Congrats you\'re on the green!'.format("\033[31;1;4m"))
    while abs(distance_remaining) > 0:
      print('You have a {} foot putt left.'.format(int(distance_remaining*3,)))
      putt = random.randint(round(distance_remaining*.75,0),distance_remaining)
      print('Your putt went {} feet'.format(putt*3))
      distance_remaining -= putt
      distance_remaining = abs(distance_remaining)
      self.shot_number += 1
      self.putt_counter += 1
      time.sleep(1)
    
    score = self.shot_number
    

    print('{}You\'ve finished this hole in {} strokes with {} putts.'.format('\033[0m',score,self.putt_counter))
  
  ##############################################PLAYER#########################################################
  
  def score(self):
    return self.shot_number




    


      



    

#######################################END GOLF###########################################



class Hole:
  def __init__(self,par):
    self.par = par
  def length(self):
    if self.par == 3:
      return random.randint(135,235)
    elif self.par == 4:
      return random.randint(335,400)
    elif self.par == 5:
      return random.randint(450,600)
  


############################################PLAY##########################################

class Course:
  def __init__(self,bag,lst):
    par_total = 0
    score = 0
    hole_number = 1
    for hole in lst:
      print("You are on hole {}".format(hole_number))
      bag.player(hole)
      score += bag.score()
      hole_number += 1
      par_total += hole.par
      print('Current score: {}'.format(score))
    print('Par: {}'.format(par_total))
    print( '\n\nYou shot {} on a par {} course!'.format(score,par_total))
    print('Well Done!!')


    
    
    
    

  



#bag_1_dist_dict = bag_1.club_distance()


#print(hole_1.par)
#print(hole_1.length())

#bag_1.player(hole_1)

#print(bag_1.c1)
#print(list(bag_1.club_distance()[bag_1.c1]))
#pw_list = list(bag_1.club_distance()[bag_1.c1])


#rand_dist = random.randint(pw_list[0],pw_list[-1])
#print(rand_dist)



#hole_1 = Hole(random.randint(3,5))
#bag_1.player(hole_1)
#print(bag_1.score()) DOES print the score after bag_1.player is called 

def hole_list():
  hole_1 = Hole(random.randint(3,5))
  hole_2 = Hole(random.randint(3,5))
  hole_3 = Hole(random.randint(3,5))
  '''
  hole_4 = Hole(random.randint(3,5))
  hole_5 = Hole(random.randint(3,5))
  hole_6 = Hole(random.randint(3,5))
  hole_7 = Hole(random.randint(3,5))
  hole_8 = Hole(random.randint(3,5))
  hole_9 = Hole(random.randint(3,5))
  hole_10 = Hole(random.randint(3,5))
  hole_11 = Hole(random.randint(3,5))
  hole_12 = Hole(random.randint(3,5))
  hole_13 = Hole(random.randint(3,5))
  hole_14 = Hole(random.randint(3,5))
  hole_15 = Hole(random.randint(3,5))
  hole_16 = Hole(random.randint(3,5))
  hole_17 = Hole(random.randint(3,5))
  hole_18 = Hole(random.randint(3,5))
  '''
  return [hole_1,hole_2,hole_3]#,hole_4,hole_5,hole_6,hole_7,hole_8,hole_9,hole_10,hole_11,hole_12,hole_13,hole_14,hole_15,hole_16,hole_17,hole_18]
c_1 = hole_list()
bag_1 = Golfbag('lob wedge','sand wedge','gap wedge','pitching wedge','9 iron','8 iron','7 iron','6 iron','5 iron','4 iron','3 iron','3 wood','driver')
course_1 = Course(bag_1,c_1)

















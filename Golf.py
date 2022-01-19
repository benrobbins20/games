import random
import time
class Golfbag:
  def __init__(self,c1,c2,c3,c4): #just bag setup for now, need to add distances and miss percentage
    self.c1 = c1 
    self.c2 = c2 
    self.c3 = c3 
    self.c4 = c4 
    self.club_list = [c1,c2,c3,c4]
    cyan = r'\033[96m'
  def club_distance(self):
    bag_dist = {}
    dist_dict = {'Putter':range(0,15),'Lob wedge':range(15,60),'Sand wedge':range(35,80),'Gap wedge':range(50,100),'Pitching wedge':range(125,156),'9 iron':range(130,166),'8 iron':range(150,176),'7 iron':range(165,186),'6 iron':range(180,196),'5 iron':range(195,211),'4 iron':range(210,221),'3 iron':range(225,241),'3 wood':range(235,261),'Driver':range(250,301)}
    for club in self.club_list:
      if club in dist_dict.keys():
        bag_dist[club] = dist_dict[club] 
    return bag_dist
  def __repr__(self):
    return ('Bag:\n{c1}\n{c2}\n{c3}\n{c4}'.format(c1=self.c1,c2=self.c2,c3=self.c3,c4=self.c4))
  def player(self,hole):
    distance_remaining = (hole.length())
    print('You are playing a {} yard par {}.'.format(distance_remaining,hole.par))
    self.shot_number = 0
    while abs(distance_remaining) > 20:
      print('Distance remaining: {} yards'.format(distance_remaining))
      club = input('Choose a club from the following.\n\n{}\n:'.format(self.club_distance()))
      club_range = list(self.club_distance()[club])
      hit = random.randint(club_range[0],club_range[-1])
      print('Your shot went {} yards.'.format(hit))
      distance_remaining-=hit
      distance_remaining = abs(distance_remaining)
      self.shot_number+=1
    print('Congrats you\'re on the green!')
    while abs(distance_remaining) > 0:
      print('You have a {} foot putt left.'.format(int(distance_remaining*3,)))
      putt = random.randint(int(distance_remaining*.75),distance_remaining)
      print('Your putt went {} feet'.format(putt*3))
      distance_remaining -= putt
      distance_remaining = abs(distance_remaining)
      self.shot_number += 1
      time.sleep(1)
    print('You\'ve finished this hole with {} strokes.'.format(self.shot_number))


      



    

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

bag_1 = Golfbag('Lob wedge','9 iron','4 iron','Driver')
bag_1_dist_dict = bag_1.club_distance()
hole_1 = Hole(5)
#print(hole_1.par)
#print(hole_1.length())

bag_1.player(hole_1)

#print(bag_1.c1)
#print(list(bag_1.club_distance()[bag_1.c1]))
#pw_list = list(bag_1.club_distance()[bag_1.c1])


#rand_dist = random.randint(pw_list[0],pw_list[-1])
#print(rand_dist)

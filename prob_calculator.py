import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball in balls:
            self.contents += [ball] * balls[ball]
    def draw(self,number):
        if number > len(self.contents):
            balls_out = copy.copy(self.contents)
            self.contents = []
        else: 
            balls_out = random.sample(self.contents,number)
            for ball in balls_out:
                self.contents.remove(ball)
        return balls_out
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    number_success = 0
    
    for i in range(num_experiments):
        c_hat = copy.deepcopy(hat)
        balls_drawn = c_hat.draw(num_balls_drawn)
        bool_check = True
        for key in expected_balls:
            bool_check = bool_check and (expected_balls[key] <= balls_drawn.count(key))
            
        number_success += 1 if bool_check  else 0
    return number_success/num_experiments
        
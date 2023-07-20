import random
import matplotlib.pyplot as plt

# step = [1,-1]
# choice = random.choice(step)

# walk = []
# walk.append(choice)
# for st in range(1,1000):
#     nextst = walk[st-1] + random.choice(step)
#     walk.append(nextst)
# # print(walk)
# plt.plot(walk)
# plt.show(walk)

def rand_walk(num):
    walk =[]
    
    choice = random.choice([1,-1])
    walk.append(choice)
    for i in range(1,num):
        next_step = walk[i-1] + random.choice([1,-1])
        walk.append(next_step)
        
    return walk

    
    
# rand = rand_walk(100)
# print(rand)
# plt.plot(rand)
# plt.show()

def plots(num,stwalks):
    lab_list = list(range(1,num+1))
    for i in range(0,num):
        
        x = list(range(1,stwalks+1))
        
        plt.plot(x,rand_walk(stwalks),label = 'plot number' + '' + str(lab_list[i]))
            
        
# step_choice = [1,-1]
# ch = random.choice(step_choice)
# walk = []
# walk.append(ch)
# for step in range(1,1000):
#     next_step = walk[step-1] + random.choice(step_choice)
#     walk.append(next_step)
#     print(walk)
    
    
def rand_walk(num):
    walk = []
    ch = random.choice([1,-1])
    walk.append(ch)
    for step in range(1,num):
        next_step = walk[step-1] + random.choice([1,-1])
        walk.append(next_step)
    return walk

print(rand_walk(10))    
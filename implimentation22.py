# strange = ('''{"Doctor Strange" is a: "2016" , "American superhero film": "based on the Marvel Comics character of the same name" ,  "Produced by": "Marvel Studios and distributed by Walt Disney Studios Motion Pictures" , "14th film": "in the Marvel Cinematic Universe (MCU)"}  The film was directed by Scott Derrickson from a screenplay he wrote with Jon Spaihts and C. Robert Cargill, and stars Benedict Cumberbatch as neurosurgeon Stephen Strange along with Chiwetel Ejiofor, Rachel McAdams, Benedict Wong, Michael Stuhlbarg, Benjamin Bratt, Scott Adkins, Mads Mikkelsen, and Tilda Swinton. In the film, Strange learns the mystic arts after a career-ending car crash.

# Various incarnations of a Doctor Strange film adaptation had been in development since the mid-1980s, until Paramount Pictures acquired the film rights in April 2005 on behalf of Marvel Studios. Thomas Dean Donnelly and Joshua Oppenheimer were brought on board in June 2010 to write a screenplay. In June 2014, Derrickson was hired to direct, with Spaihts re-writing the script. Cumberbatch was chosen for the eponymous role in December 2014, necessitating a schedule change to work around his other commitments. This gave Derrickson time to work on the script himself, for which he brought Cargill on to help. Principal photography on the film began in November 2015 in Nepal, before moving to England and Hong Kong, and wrapping up in New York City in April 2016.

# Doctor Strange had its world premiere in Hong Kong on October 13, 2016, and was released in the United States on November 4, as part of Phase Three of the MCU. The film grossed over $677 million worldwide and was met with praise for its cast, visual effects, and musical score. The film received an Academy Award nomination for Best Visual Effects. A sequel, Doctor Strange in the Multiverse of Madness, was released in May 2022
# ''')
# from collections import Counter

# # print(Counter(strange.lower()))

# new_dict = dict(Counter(strange.lower()))

# new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}

# print(new_dict)

# capital = {"France":"Paris","Spain":"madrid","United Kingdom":"london", "India":"New Delhi", "United states":"Washington DC", "Italy":"Rome",
#             "Denmark":"Copenhamegn", "Germany":"Berlin","Greese":"Athems","Bulgeria":"Sofia","Ierland":"Dublin","Mexico":"Mexico city"}

# user_input = input('Which City Do U Want To Check in?:>> ')

# user_input = (user_input.lower())

# while ("United Kingdom " not in user_input and not user_input.isalpha()):
#     if user_input == "United states":
#         break
#     print ('U must enter a string')
#     user_input = input('which country u want to go :>>')
    
# user_input = user_input.title()
    
# if user_input in capital:
#     print(f'The capital of {user_input} is {capital[user_input]}')    
# else:
#     print ('no data avaiable')    
    
#fibonacco in dict
# n = 12
# a = 0
# b = 1
# d = dict()
# for i in range (1,n+1):
#     d[i] = a
#     a,b = b,a+b
# print(d)


# companies with dictt

# companies = ('pyrhon os','python soft','pythazon','pybook')
# key_values = ('open','high','low','close')
# prise = [[25,36,23,45,54],[55,66,44,87],[25,897,65,49],[45,89,78,56]]
# d = dict()

# for i in range(len(key_values)):
#     d[companies[i]] = dict(zip(key_values,prise[i]))
# print(d)

# import datetime
# today = datetime.date.today()
# print(f'todays date is {today}')
# exam = datetime.date(2022,7,15)
# delta = exam - today

# print(f'just{delta.days} days more until exam')

# import Fibo
# b = Fibo.fab(20)
# print(b)
 

# random values for a to z and  create a bar graph

# import random

# keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# D = dict()

# for letters in keys:
#     D[letters] = random.randint(1, 100)
# print(D)

# import matplotlib.pyplot as plt

# x,y = zip(*D.items())
# plt.bar(x,y)
 
# dict for cards

suits = ['spades','clubs','hearts','diamonds']
rank = ['ace','1','2','3','4','5','6','7','8','9','10','jack','queen','king']
d =dict()
for i in suits:
    d[i] = rank
print(d,end=('  '))    
    
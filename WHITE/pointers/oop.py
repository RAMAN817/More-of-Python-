#Mini Application
class movie:
    '''This class  develop by Romanson Thapa for Demo'''
    def __init__(self,title,hero,heroine): #a,b,c can be there because self.title is imp but it is recommend to keep the name same to self 
        self.title= title
        self.hero=  hero
        self.heroine= heroine
    
    def info(self):
        print('Movie name',self.title)
        print('Hero Name',self.hero)
        print('Heroine Name',self.heroine)
    
list_of_movie=[]
while True:
    title = input('Enter Movie Name')
    hero = input('Enter Hero Name')
    heroine= input('Enter Heroine Name')
    m= movie(title,hero,heroine)
    list_of_movie.append(m)
    print('Movie added Suceessfully')
    option= input('Do you want to add one more movie [Yes/No]')
    if option.lower()== 'no':
        break
print('This is the begenning')
for movie in list_of_movie:
    movie.info()
    print()
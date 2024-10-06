#Another Apporach and you can use according to your requirement
class SportNews:
    def sportnews(self):
     print('Movie Information-1')
     print('Movie Information-2')
     print('Movie Information-3')
     print('Movie Informaation-4')

class MovieNews:
    def movienews(self):
     print('Movie Information-1')
     print('Movie Information-2')
     print('Movie Information-3')
     print('Movie Information-4')

class PoliticsNews:
   def politicalnews(self):
      print('Politics Information-1')
      print('politics Information-2')
      print('Politics Information-3')
      print('Political Inforamtion-4')

class RomanNews:
   def __init__(self,sports, movies,politics):
      self.sports= sports
      self.movie= movies
      self.politics= politics

   def getTotalNews(self):
      print('Welcome to Durga news')   
      self.sports.sportnews()
      self.movie.movienews()
      self.politics.politicalnews()
sports= SportNews()
movie= MovieNews()
poitics= PoliticsNews()
dnews= RomanNews(sports,movie,poitics)
dnews.getTotalNews()

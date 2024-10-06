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
   def __init__(self):
      print('Welcome to Roman News')
      self.sports= SportNews()
      self.movie= MovieNews()
      self.politics= PoliticsNews()
  
   def getTotalNews(self):
      print('Welcome to Durga News')
      self.sports.sportnews()
      self.movie.movienews()
      self.politics.politicalnews() 

roman= RomanNews()
roman.getTotalNews()
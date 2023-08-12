import requests as r
from lxml import html
try:
  url='https://editorial.rottentomatoes.com/guide/best-movies-2022/'
  tree=html.fromstring(r.get(url).text)
  movie_name=tree.xpath('.//div[@class="row countdown-item"]//div[@class="article_movie_title"]//a')
  movie_director=tree.xpath('.//div[@class="row countdown-item"]//div[@class="info director"]//a')
  movie_synopsis=tree.xpath('.//div[@class="row countdown-item"]//div[@class="info synopsis"]')
  movie_rank=tree.xpath('.//div[@class="row countdown-item"]//div[@class="countdown-index"]')
  def viewdata():
    for i,j,k,l in zip(movie_name,movie_rank,movie_director,movie_synopsis):
      print(f'movie_name: {i.text_content()}')
      print(f'movie_rank: {j.text_content()}')
      print(f'movie_director: {k.text_content()}')
      print(l.text_content())
      print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  def savedata():
   file_name=input('Enter your file name to save: ')
   with open(f"{file_name}.txt", "a", encoding="utf-8") as file:
    for i, j, k, l in zip(movie_name, movie_rank, movie_director, movie_synopsis):
        file.write(f"movie_name: {i.text_content()}\n")
        file.write(f"movie_rank: {j.text_content()}\n")
        file.write(f"movie_director: {k.text_content()}\n")
        file.write(f"{l.text_content()}\n")
        file.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


  while True:
   print('BEST MOVIES OF 2022')
   print('1. I WANT TO SEE THE DATA')
   print('2. I WANT TO SAVE THE DATA AS A TEXT FILE')
   option=input('Enter option from above[1,2]: ')
   if option == '1' or option == '2':
     if option=='1':
       viewdata()
       break
     if option=='2':
       savedata()
       break
   print('Wrong input, Enter the option 1 or 2')
   continue
except Exception as e:print(f'AN ERROR OCCURED : {e}')




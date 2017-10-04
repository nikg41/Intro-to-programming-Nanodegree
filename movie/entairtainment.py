import fresh_tomatoes#it import the fresh tomatoes file to my page
import media#it imports media file which i have created
#here the details of all movies which are needed
kungfu_panda3=media.Movie("Kung fu Panda 3","It is a story of panda who is dedicated to kungfu and discipline",
               "https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg",
               "https://youtu.be/fGPPfZIvtCw")
avatar = media.Movie("Avatar",
                     "a marine on an alien plane",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
Pink=media.Movie("Pink","Fight For women rights",
      "https://upload.wikimedia.org/wikipedia/en/a/ae/Pinkmovieposter.jpg",
      "https://www.youtube.com/watch?v=AL2TShb6fFs")
MS_dhoni=media.Movie("M.S.Dhoni",
                     "Biopic on indian cricketer",
                     "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                     "https://www.youtube.com/watch?v=6L6XqWoS8tw&itct=CAkQpDAYDCITCMDayYyWsc8CFQoVTgodhfUJzTIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo&client=mv-google-%27N&gl=IN&hl=hi")
frozen=media.Movie("Frozen",
                   "story on what is true love",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=FLzfXQSPBOg")
cars=media.Movie("Cars","Story of a Car who is eager to win piston cup i.e best car of year",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Cars_2006.jpg/220px-Cars_2006.jpg",
                 "https://www.youtube.com/watch?v=uxx75HVd-F0")
nysm2=media.Movie("Now You See Me 2","movie based on the magic tricks",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Now_You_See_Me_2_poster.jpg/220px-Now_You_See_Me_2_poster.jpg",
                  "https://www.youtube.com/watch?v=InqU8CLwbPg")
xmen=media.Movie("X-Men:Apocalypse",
                 "Movie is based on persons having extra ordinary power i.e mutants",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/X-Men_-_Apocalypse.jpg/220px-X-Men_-_Apocalypse.jpg",
                 "https://www.youtube.com/watch?v=Jer8XjMrUB4")
titanic=media.Movie("Titanic",
         "Love story of jack and rose",
         "https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg",
         "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
movies=[MS_dhoni,Pink,kungfu_panda3,frozen,nysm2,xmen,avatar,cars,titanic]
#list of all movies i.e how i want to show them
fresh_tomatoes.open_movies_page(movies)
#it open the movies page on browser

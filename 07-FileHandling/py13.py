movie_array=["tak","nie","niewiem","moze",]
file=open("movie.txt",'w')
len=len(movie_array)
for line in movie_array:
    file.write(line+"\n")


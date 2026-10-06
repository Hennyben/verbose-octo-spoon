
artists= {}
while True:
        artist=input("enter a musician: ").lower()
        if artist == "done":
            break
        
      

        if artist in artists:
            artists[artist] += 1
        else:
            artists[artist] =1


x = dict(sorted(artists.items()))
        

print("Votes\n ----------\n")
print("-",x, "\n")

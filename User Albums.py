def make_album(artist, album_title):
    return {artist: album_title}


# *uncomment line below to test while loop when Dictionary has values
# albums = {"Eric Prydz": "Opus"}

albums = {}

while not albums:
    albums = make_album(input("Enter an artist: "), input("Enter an album title: "))
    if albums:
        break

print(albums)

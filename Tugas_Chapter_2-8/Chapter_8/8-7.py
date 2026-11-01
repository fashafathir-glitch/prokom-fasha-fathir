def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album
print(make_album("Tulus", "Manusia"))
print(make_album("Sheila on 7", "07 Des"))
print(make_album("Nadin Amizah", "Selamat Ulang Tahun", 10))

from models import db, connect_db, Playlist, Song, PlaylistSong
from app import app



s1 = Song(title="I See Fire", artist="EdSheran")
s2 = Song(title="Give Me Love", artist="EdSheran")
s3 = Song(title="Bloodstream", artist="EdSheran")
s4 = Song(title="Big Girls Dont Cry", artist="Sia")
s5 = Song(title="Thunderstorm", artist="Sia")
s6 = Song(title="Counting stars", artist="OneRepublick")


p1 = Playlist(name="Ed's", description="EdSheran songs")
p2 = Playlist(name="Sia's", description="Sia songs")

ps1 = PlaylistSong(playlist_id=1, song_id=1)
ps2 = PlaylistSong(playlist_id=1, song_id=2)
ps3 = PlaylistSong(playlist_id=1, song_id=3)

db.session.add_all([s1,s2,s3,s4,s5,s6])
db.session.commit()

db.session.add_all([p1,p2])
db.session.commit()

db.session.add_all([ps1,ps2,ps3])
db.session.commit()
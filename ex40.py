class Song(object):
    def __init__(self,lyr):
        self.lyrics=lyr
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
hbd= Song(["Happy birthday to you","I don't want to get sued",
"So I'll stop right there"])
bop=Song(["They rally around tha family", "With pockets full of shells"])
hbd.sing_me_a_song()
bop.sing_me_a_song()

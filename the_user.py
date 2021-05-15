class Myuser:
    def __init__(self):
        self.myuser_name = ""
        self.song_list = []

    def setmyuser_name(self, name):
        self.myuser_name = name
    
    def getuser_name(self):
        return self.myuser_name

    def getsong_list(self):
        return self.song_list

    def setsong_list(self, tempS):
        self.song_list = tempS

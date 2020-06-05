class Track:

    def __init__(self, num, name, time, volume=50):
        self.name = name
        self.time = time
        self.num = num
        self.volume = volume
        self.work = False

    def get_num(self):
        return self.num

    def turn_on(self):
        self.work = True
        return self.work

    def turn_off(self):
        self.work = False

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if value=='up':
            if self.work and self.volume < 75:
                self.volume += 25
        elif value=='down':
            if self.work and self.volume > 25:
                self.volume -= 25

    def __str__(self):
        return '|{:^15}|{:^15}|'.format(self.name, self.time)

    def __repr__(self):
        return self.name


class Album(Track):

    def __init__(self, num, album, singer, year, name, time):
        Track.__init__(self, num, name, time)
        self.album = album
        self.singer = singer
        self.year = year
        self.work = False

    def get_num(self):
        return self.num


    def __str__(self):
        return '|{:^5}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(self.num, self.album, self.singer,
                                                            self.year, self.name,
                                                             self.time)

    def __repr__(self):
        return self.__str__()
import datetime


class Shrek(object):

    def are_we_there_yet(self):
        return datetime.datetime.now() < datetime.datetime(2019, 7, 15, 20, 39)

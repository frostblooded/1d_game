import datetime


class TimeManager:
    __instance = None

    def __init__(self):
        self.start_time = datetime.datetime.now()

    @staticmethod
    def setup():
        TimeManager.get_instance()

    @staticmethod
    def destroy():
        TimeManager.__instance = None

    @staticmethod
    def get_instance():
        if TimeManager.__instance is None:
            TimeManager.__instance = TimeManager()

        return TimeManager.__instance

    def time_since_start(self):
        return datetime.datetime.now() - self.start_time

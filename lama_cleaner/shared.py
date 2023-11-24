
class State:
    job = ""
    job_count = 0

    def __init__(self):
        pass

    def start(self, job="[None]", job_count=1):
        self.job = job
        self.job_count = job_count

    def end(self):
        self.job = ""
        self.job_count = 0

    def to_json(self):
        return {
            "job": self.job,
            "job_count": self.job_count,
        }

state = State()

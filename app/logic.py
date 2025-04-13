class Task:
    def __init__(self, title: str, date, priority: str, status: str):
        self.title = title
        self.date = date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.date} | {self.priority} | {self.status}"

    def to_list(self):
        return [self.title, self.date, self.priority, self.status]

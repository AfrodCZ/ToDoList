class Task:
    def __init__(self, title: str, description: str, date, priority: str, status: str):
        self.title = title
        self.description  = description
        self.date = date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.description} |{self.date} | {self.priority} | {self.status}"

    def to_list(self):
        return [self.title, self.description, self.date, self.priority, self.status]

    def to_dict(self):
        return {"title": self.title, "description": self.description, "date": self.date, "priority": self.priority, "status": self.status}
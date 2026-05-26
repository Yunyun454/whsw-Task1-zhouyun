class Member:
    next_id = 1
    
    def __init__(self, name, group):
        self.member_id = f"RM{Member.next_id:04d}"
        self.name = name
        self.group = group
        self.score = 0
        Member.next_id += 1
    
    def __str__(self):
        return f"{self.member_id}    {self.name}      {self.group}      {self.score}"
    
    def add_score(self, points):
        self.score += points
    
    def deduct_score(self, points):
        if points > self.score:
            return False
        self.score -= points
        return True
from member import Member

class MemberManager:
    def __init__(self):
        self.members = []
    
    def add_member(self, name, group):
        member = Member(name, group)
        self.members.append(member)
        return member
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def add_score(self, member_id, points):
        member = self.find_member(member_id)
        if member:
            member.add_score(points)
            return member
        return None
    
    def deduct_score(self, member_id, points):
        member = self.find_member(member_id)
        if member:
            success = member.deduct_score(points)
            return member, success
        return None, False
    
    def rank_all(self):
        sorted_members = sorted(self.members, key=lambda x: x.score, reverse=True)
        return sorted_members
    
    def delete_member(self, member_id):
        member = self.find_member(member_id)
        if member:
            self.members.remove(member)
            return member
        return None
    
    def get_all_members(self):
        return self.members
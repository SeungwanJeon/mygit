class Set:
    def __init__(self,member=[]):
        self.member=member
    def __repr__(self):
        return str(self.member)
    def append(self,a):
        return Set(self.member+[a])
    def delete(self,a):
        return Set([el for el in self.member if el not in [a]])
    def union(self,S2):
        return Set(self.member+[el for el in self.member if el not in S2.member])
    def intersection(self,S2):
        return Set([el for el in self.member if el in S2.member])
    def difference(self,S2):
        return Set([el for el in self.member if el not in S2.member])


a=set([1,2,3])
b=set([2,3,4])
a.union(b)
a.intersection(b)
a.difference(b)

a=Set([1,2,3])
b=Set([2,3,4])
a.append(2)
a.delete(2)
a.union(b)
a.intersection(b)
a.difference(b)

from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent.setdefault(x, x)
        self.parent.setdefault(y, y)
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                dsu.parent.setdefault(email, email)
                dsu.union(first_email, email)
                email_to_name[email] = name

        groups = defaultdict(list)
        for email in email_to_name:
            root = dsu.find(email)
            groups[root].append(email)


        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result

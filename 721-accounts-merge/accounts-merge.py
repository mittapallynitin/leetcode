class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = dict() # email to parent email
        email_name = dict()
        
        def find(mail):
            root_mail = parent[mail]
            while root_mail != parent[root_mail]:
                parent[root_mail] = parent[parent[root_mail]]
                root_mail = parent[root_mail]
            return root_mail
        
        def union(mail1, mail2):
            root1, root2 = find(mail1), find(mail2)
            if root1 != root2:
                parent[root2] = root1

        for account in accounts:
            name = account[0]
            root = account[1]
            for mail in account[1:]:
                if mail not in parent:
                    parent[mail] = mail
                email_name[mail] = name
            for mail in account[2:]:
                union(root, mail)

        merged = defaultdict(list)
        for email in parent:
            root = find(email)
            merged[root].append(email)
        
        result = []

        for root, mails in merged.items():
            result.append(
                [email_name[root]] + sorted(mails)
            )
        return result
 
            

                
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for p in path:
            if p in [".", ""]:
                continue
            elif ".." == p:
                if stack: stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)
       
        


        
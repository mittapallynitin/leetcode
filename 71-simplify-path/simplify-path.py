class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for cleaned in path:
            if cleaned in [".", "/", ""]:
                continue
            elif cleaned == "..":
                if stack: stack.pop()
            else:
                stack.append(cleaned)
        return "/" + "/".join(stack)
        


        
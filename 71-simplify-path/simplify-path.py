class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for df in path:
            cleaned = df.strip()
            if cleaned in [".", "/", ""]:
                continue
            elif cleaned == "..":
                if stack: stack.pop()
            else:
                stack.append(cleaned)
        return "/" + "/".join(stack)
        


        
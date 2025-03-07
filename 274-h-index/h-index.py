class Solution:
    def hIndex(self, citations: List[int]) -> int:
        total_papers = len(citations)
        paper_counts = [0] * (total_papers + 1)

        for ct in citations:
            paper_counts[min(ct, total_papers)] += 1
        
        res = 0
        curr_papers = 0 
        for ct in range(total_papers, -1, -1):
            curr_papers += paper_counts[ct]
            if curr_papers >= ct:
                return ct
        return 0
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = deque([])
        while deck:
            if res:
                res.appendleft(res.pop())
            res.appendleft(deck.pop())
        return res
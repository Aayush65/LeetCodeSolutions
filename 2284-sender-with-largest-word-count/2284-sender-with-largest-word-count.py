class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hm = defaultdict(int)
        for i in range(len(senders)):
            messages[i] = len(messages[i].split())
            hm[senders[i]] += messages[i]
        maxMsgs = messages[0]
        maxMsgSender = senders[0]
        for sender in hm:
            if hm[sender] > maxMsgs:
                maxMsgs = hm[sender]
                maxMsgSender = sender
            elif hm[sender] == maxMsgs:
                maxMsgSender = max(maxMsgSender, sender)
        return maxMsgSender
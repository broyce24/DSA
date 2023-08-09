class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nn = self.next
        out = str(self.val)
        while nn:
            out += ', ' + str(nn.val)
            nn = nn.next
        return out


class Solution:
    def mergeKLists(self, lists):
        # setting first value to min node value
        value = 10001
        for ll in lists:
            value = min(ll.val, value)

        result = ListNode(None, None)
        iter_res = result
        next_min = 10001
        # While we have lists left
        for _ in range(5):  # debug
            # For each list we have
            print(list(map(str, lists)), "min:", value)
            for i in range(len(lists)):
                while lists[i] and lists[i].val == value:
                    iter_res.next = ListNode(lists[i].val, None)
                    iter_res = iter_res.next
                    lists[i] = lists[i].next
                #print("Done with list")
                if lists[i] and lists[i].val < next_min:
                    next_min = lists[i].val
                    #print(next_min)
            value = next_min
            next_min = 10001
        return result.next

l1 = ListNode(1, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, ListNode(6, None))
#print(l1)
lists = [l1, l2, l3]
S = Solution()
ans = S.mergeKLists(lists)
while ans:
    print(ans.val, end=', ')
    ans = ans.next
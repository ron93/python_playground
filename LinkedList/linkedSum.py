class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next
	

class Solution:
	def addtwo(self,l1,l2):
		
		carry = 0
		result = ListNode()
		result_tail = result

		while l1 or l2 or carry:
			#assign li and l2 val to val1 and val2 if val exists
			val1 = (l1.val if l1 else 0)
			val2 = (l2.val if l2 else 0)
			
			#divmod(q,r) returns Quotient(10/2 = 5):output and remainder assigned to carry
			carry, output = divmod(val1+val2+carry,10)
			
			result_tail.next = Listnode(output)
			result_tail = result_tail.next
			
			
			l1  = (l1.next if l1 else None)
			l2 = (l2.next if l2 else None)
		return result.next
s = Solution()
l1 = [7]
l2 = [4]
r = s.addtwo(l1,l2)

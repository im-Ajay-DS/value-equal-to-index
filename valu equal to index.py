class Solution:

	def valueEqualToIndex(self,arr, n):
		answer=[]
		for i in range(len(arr)):
		    if arr[i]==i+1:
		        answer.append(arr[i])
		return answer

class Solution:
    def addTwoLists(self, num1, num2):
        a=''
        while num1:
            a+=str(num1.data)
            num1=num1.next
        b=''
        while num2:
            b+=str(num2.data)
            num2=num2.next 
        k=str(int(a)+int(b))
        i=1
        ans=Node(int(k[0]))
        res=ans
        while i<len(k):
            ans.next=Node(int(k[i]))
            i+=1
            ans=ans.next
        return res

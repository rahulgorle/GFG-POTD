def compute(head): 
    str1 = []
    while head is not None:
        str1.append(head.data)
        head = head.next
    
    str2 = ""
    for i in str1:
        str2 += i
    if str2 == str2[::-1]:
        return True
    return False

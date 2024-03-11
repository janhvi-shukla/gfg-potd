def removeDuplicates(self,str):
	    string=''
	    s=set(str)
	    for i in str:
	        if i in s:
	            string+=i
	            s.remove(i)
	    return string

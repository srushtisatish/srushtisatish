def count_substring(string, sub_string):
    count=0
    j=len(sub_string)
    for i in range(0,len(string)):
        if sub_string[0]==string[i]:
            if sub_string==string[i:i+j]:
                count+=1
            

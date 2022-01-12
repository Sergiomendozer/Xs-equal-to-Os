def counts(string):
    count_x=0
    count_o=0
    i=-1
    while i<len(string)-1:
        i+=1
        if string[i]=="x":
            count_x=count_x+1
        if string[i]=="o":
            count_o=count_o+1
        
    return count_o == count_x

print(counts ("xoxoi3xo"))
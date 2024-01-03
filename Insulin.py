"""
Your module description
"""
file1 = open("/home/ec2-user/environment/preproinsulin-seq.txt","r")
#print("Output of Readlines")

#print(file1.readlines())
counted = 0
for line in file1.readlines():
    #print(type(line))
    
    line = line.strip()
    line = line.replace('//','')
    line= line.replace('ORIGIN','')
    for i in "0123456789":
        line=line.replace(i,'')
        line=line.replace(' ','')
    counted += len(line)
    
    print(line)
print("number of carachters is", counted)
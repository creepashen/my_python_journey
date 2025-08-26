dic = dict()
lis = []


with open('sample_emails.txt', 'r') as Fhand:
    for line in Fhand:
       
        for drop_dash in '-':
           
            line = line.replace(drop_dash, '')           
            
            if line.startswith('From: '):
                
                line = line.rstrip().split()
                lis.append(line[1])

for one_mai in lis:
   
    one_mai = one_mai.split('@')
    one_mai = str(one_mai[0])
    dic[one_mai] = dic.get(one_mai, 0) + 1

print(dic)
c={'A','B','C','E','H','K','M','O','P','T','Y','X'} # can add russian letter if need
a = ['A123AA11','A222AA123','A12AA123','A123CC1234','AA123A12',
     'hsbvbsks','a876oi89','123354684','gchcffhg','AAAAAAAA','Ó789MH59']
for elem in a:
    b=elem
    if len(b)>9 or len(b)<8:
        continue   
    if b[1:4].isdigit() and b[6:].isdigit() and b[0].isalpha() and b[4:6].isalpha():
        x=b
        if x[0] in c and x[4] in c and x[5] in c:
            print(x)
        
    


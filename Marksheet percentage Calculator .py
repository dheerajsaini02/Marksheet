#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##MARKSHEET :


marks = 600
obt_marks = float(input("\nEnter The Obtained marks :"))
per = (obt_marks/marks)*100
print("\npercent Is :",round(per),"%")
if per>90:
    print("\nGrade Is :A+")
elif per>80 and per <=90:
    print("\nGrade Is : A")
elif per >70 and per <=80:
    print("\nGrade Is :B+")
elif per >60 and per <=70:    
    print("\nGrade Is :B")
elif per >50 and per <=60:
    print("\nGrade Is :c+")
elif per >40 and per <=50:
    print("\nGrade Is :c")
    print("\nLow Grade .. \nImprove Your self ")
else:
    print("\nfailed...")
    


#!/usr/bin/env python
# coding: utf-8

# In[1]:


panjang = int(input("Masukkan Panjang Rows : "))
print("")

fibo = [0,1]

for i in range(2, panjang):
    angka1 = fibo[i - 2]
    angka2 = fibo[i - 1]
    angkaSelanjutnya = angka1 + angka2
    
    fibo.append(angkaSelanjutnya)

for i in range(1, panjang):
    for j in range(0, i+1):
        print(fibo[j], end=" ")
    print()


# In[ ]:


# In[ ]:





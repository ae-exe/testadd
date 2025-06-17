#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 最初にHello, World!を表示
print("Hello, World!")

# ユーザーから2つの数字を入力してもらう
num1 = float(input("1つ目の数字を入力してください: "))
num2 = float(input("2つ目の数字を入力してください: "))

# 足し算をして結果を表示
result = num1 + num2
print(f"{num1} + {num2} = {result}")


# In[2]:


get_ipython().system('jupyter nbconvert --to script test1.ipynb')


# In[ ]:





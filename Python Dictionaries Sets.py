#!/usr/bin/env python
# coding: utf-8

# # Creating tuples

# In[1]:


emp=()
print(type(emp))


# In[2]:


print(emp)


# In[3]:


city="Pune",


# In[4]:


type(city)


# In[6]:


city=("Pune",)
city


# In[7]:


city= ("Pune", "Bangalore", "Delhi", "Mumbai")
city


# In[8]:


city= "Pune", "Bangalore", "Delhi", "Mumbai"
city


# In[9]:


list1=[1,2,3,4]
tuple1=(1,2,3,4)
list.append(5)
print(list1)


# In[10]:


tuple.append(5)


# In[11]:


print(city)


# In[12]:


city[1]


# In[13]:


len.(city)


# In[14]:


len.city


# # Concatenation

# In[15]:


print(city)


# In[16]:


num=1,2,3,4


# print(city+num)

# In[17]:


print(city+num)


# In[18]:


nest=(city,num)


# In[19]:


print(nest)


# # Repetiton

# In[20]:


rep=("Python",)*5
rep


# In[22]:


rep=("Python",)
print(rep*10)


# In[23]:


rep


# # Slicing

# In[24]:


num


# In[25]:


num[1:]


# In[26]:


num[::-1]


# # Unpacking

# In[27]:


tuple("Simplilearn")


# In[28]:


print(num)


# In[29]:


a,b,c,d=num


# In[30]:


print(a,b,c,d)


# In[31]:


a,*b,c=num
print(a,b,c)


# # Deleting a tuple

# In[32]:


tuple1=(1,2,3,4)
print(tuple1)


# In[33]:


del tuple1


# In[34]:


print(tuple1)


# # Built in function

# In[35]:


num1=(3,5,2,2,2,2,6,5,8)


# In[36]:


num1.count(2)


# In[37]:


sum(num1)


# In[38]:


len(num1)


# In[39]:


max(num1)


# In[40]:


min(num1)


# # Converting list to tuple

# In[41]:


lst=[1,2,3,4]
print(type(lst))


# In[42]:


tpl=tuple(lst)


# In[43]:


print(tpl)


# In[44]:


type(tpl)


# # Nesting tuples in a list

# In[46]:


lst=[(1,2,3,),(4,5,6)]


# In[47]:


print(lst)


# In[48]:


lst.append(("Tuple","Inside","list"))


# In[49]:


print(lst)


# In[50]:


lst.remove((1,2,3))


# In[51]:


print(lst)


# # Nesting Lists within tuples

# In[52]:


tpl=(['a','b','c'],['d','e','f'])


# In[53]:


print(tpl)


# In[54]:


tpl[0].append('z')


# In[55]:


print(tpl)


# In[57]:


tpl[0].remove('z')


# In[58]:


print(tpl)


# In[ ]:


tpl.append(['x',y])


# # Sets and dictionaries
# 
# #Creating dictionaries

# In[2]:


d1={}
print(d1)
print(type(d1))


# In[3]:


d2={1:"Welcome",2:"to",3:"Python",4:"tutorial"}
print(d2)


# In[4]:


d3={"name":"Sam","age":22,"profession":"student"}
print(d3)


# In[5]:


d4=dict({1:"Welcome",2:"to",3:"Python",4:"tutorial"})
print(d4)


# In[7]:


d5=dict([(1,"Welcome"),(2,"to"),(3,"Python"),(4,"tutorial")])
print(d5)


# In[8]:


d6={"name":{"first":"Sam","last":"Crew"},"age":22,"profession":"student"}
print(d6)


# # Adding elements

# In[10]:


d={}
d[0]="Welcome"
print(d)


# In[11]:


d[1]=("How","are", "you")
print(d)


# In[13]:


d["name"]="Sam"
print(d)


# In[14]:


d["name"]={"first":"Sam","last":"Crew"}
print(d)


# # Accessing elements

# In[15]:


print(d)


# In[16]:


print(d["name"])


# In[17]:


print(d["name"]["first"])


# In[18]:


print(d.get(1))


# # Deleting elements

# In[19]:


print(d)


# In[20]:


d.pop(0)


# In[21]:


print(d)


# In[22]:


d.popitem()


# In[24]:


print(d)


# In[25]:


print(d)


# # using built in functions

# In[26]:


d.values()


# In[27]:


keys={'a','b','c','d'}
value=1
dict.fromkeys(keys,value)


# In[28]:


d.clear()


# In[29]:


print(d)


# # Sets

# In[30]:


s=set([1,2,3,4])
print(s)
print(type(s))


# In[31]:


s.add('a')


# In[32]:


print(s)


# In[33]:


fs=frozenset([1,2,3,4])
print(fs)


# In[34]:


fs.add('a')


# In[35]:


s1=set([1,3,7,2])
s2=set([3,2,8,9])


# In[36]:


s1.union(s2)


# In[37]:


s1.difference(s2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





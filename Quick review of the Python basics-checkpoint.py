#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1 / 10


# In[ ]:


a = 10


# In[ ]:


a


# In[ ]:


print(a)


# In[ ]:


type(a)


# In[ ]:


a = 'this is a string'


# In[ ]:


a


# In[ ]:


type(a)


# In[ ]:


a = 10
b = 20


# In[ ]:


a


# In[ ]:


b


# In[ ]:


temp = a
a = b
b = temp


# In[ ]:


a


# In[ ]:


b


# In[ ]:


a, b = b, a


# In[ ]:


a


# In[ ]:


b


# In[ ]:


c, d, e = 100, 200, 300


# In[ ]:


c


# In[ ]:


d


# In[ ]:


e


# In[ ]:


msg = "Hello World!"


# In[ ]:


type(msg)


# In[ ]:


msg


# In[ ]:


len(msg)


# In[ ]:


reversed(msg)

for ( int i; i < len(msg); i++) {         
    cout << msg[i];
}
# In[ ]:


for ch in msg:
    print(ch)


# In[ ]:


for ch in reversed(msg):
    print(ch)


# In[ ]:


msg


# In[ ]:


msg[0]


# In[ ]:


msg[1]


# In[ ]:


msg[-1]


# In[ ]:


msg[-2]


# In[ ]:


msg[6]


# In[ ]:


msg[-6]


# In[ ]:


len(msg)


# In[ ]:


msg[11]


# In[ ]:


msg[12]


# In[ ]:


msg


# In[ ]:


msg[4:8]


# In[ ]:


msg[:8]


# In[ ]:


msg[4:]


# In[ ]:


msg


# In[ ]:


msg[:]


# In[ ]:


msg[::2]


# In[ ]:


msg


# In[ ]:


msg[2:10:2]


# ### [ ] notation supports START : STOP : STEP for ANY sequence

# In[ ]:


msg[::3]


# In[ ]:


msg[::-2]


# In[ ]:


msg[::-1]


# In[ ]:


msg


# In[ ]:


msg[0]


# In[ ]:


msg[0] = 'h'


# In[ ]:


msg


# In[ ]:


list(msg)


# In[ ]:


list_msg = list(msg)


# In[ ]:


list_msg


# In[ ]:


list_msg[0]


# In[ ]:


list_msg[-1]


# In[ ]:


list_msg[0] = 'h'


# In[ ]:


list_msg


# In[ ]:


''.join(list_msg)


# In[ ]:


msg


# In[ ]:


msg[1:]


# In[ ]:


'h' + msg[1:]


# In[ ]:


msg = 'h' + msg[1:]


# In[ ]:


msg


# In[ ]:





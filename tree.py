#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
#import numpy as np
#from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree
#import graphviz


# In[6]:


dados = pd.ExcelFile('/home/dagoberto/Documentos/TRABALHO/DADOS_TREE_TESTE_X.xlsx')
df = pd.read_excel(dados, 'Planilha1')


# In[27]:


features = list(df.columns[4:6])
X = df[features]

target = list(df.columns[9:13])
Y = df[target]


# In[28]:


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


# In[36]:


tree.plot_tree(clf.fit(X, Y))


# In[21]:


dadosXP = pd.ExcelFile('/home/dagoberto/Documentos/TRABALHO/DADOS_PRED_XP1.xlsx')
dfXP = pd.read_excel(dadosXP, 'Planilha1')


# In[35]:


dfXP.columns[4:6]


# In[32]:


features = list(dfXP.columns[4:6])
XP = dfXP[features]


# In[33]:


result = clf.predict(XP)


# In[34]:


result


# In[26]:


dfXP


# In[ ]:





# In[ ]:





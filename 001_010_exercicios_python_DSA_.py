#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)


# In[2]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista = ['laranja', 'macã', 'banana', 'arroz', 'carne']
print(lista)


# In[3]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
frase1 = 'Ando devagar '
frase2 = 'porque já tive pressa!'
frase_final = frase1 + frase2
print(frase_final)
# Exemplo 2
print(frase1+frase2)


# In[5]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5, 6, 6 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 6 aparece na tupla
tup1 = (1,2,2,3,4,4,4,5,6,6)
tup1.count(6)


# In[6]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict3 = {}
print(dict3)


# In[8]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict = {'k1':'Miqueias', 'k2':'Larryssa', 'k3':'Felipe'}
print(dict)


# In[9]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict['k4'] = 'Yasmin'
print(dict)


# In[10]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dict1 = {'chave1':'PowerBi', 'chave2':[30,50], 'chave3':'SQL'}
print(dict1)


# In[11]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
list1 = ['Casa', (30,22), {'chave1':'vendedor', 'chave2':'produto'}, 10.5]
print(list1)


# In[13]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]


# In[ ]:





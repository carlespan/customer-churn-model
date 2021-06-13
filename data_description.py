#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

sentences = ("State: the US state in which the customer resides, indicated by a two-letter abbreviation; for example, OH or NJ",
"Account Length: the number of days that this account has been active", 
"Area Code: the three-digit area code of the corresponding customer’s phone number", 
"Phone: the remaining seven-digit phone number", 
"Int’l Plan: whether the customer has an international calling plan: yes/no", 
"VMail Plan: whether the customer has a voice mail feature: yes/no", 
"VMail Message: presumably the average number of voice mail messages per month", 
"Day Mins: the total number of calling minutes used during the day", 
"Day Calls: the total number of calls placed during the day", 
"Day Charge: the billed cost of daytime calls", 
"Eve Mins: Number of calls minutes during the evening", 
"Eve Calls: Number of calls placed during the evening", 
"Eve Charge: The billed cost for calls placed during the evening", 
"Night Mins: Number of calls minutes during nighttime", 
"Night Calls: Number of calls placed during nighttime", 
"Night Charge: The billed cost for calls placed during nighttime", 
"Intl Mins: Number of calls minutes for international calls", 
"Intl Calls: Number of calls for international calls", 
"Intl Charge: The billed cost for calls for international calls",
"CustServ Calls: the number of calls placed to Customer Service", 
"Churn: whether the customer left the service")  

# Procesando el texto
lista = list(sentences)
variables = [elemento.split(sep=': ')[0] for elemento in lista]
descripciones = [elemento.split(sep=': ')[1] for elemento in lista]

# Creando el DataFrame: Variables y Descripcion
df = pd.DataFrame(zip(variables,descripciones), columns=['Variable','Description'])

data = pd.read_csv('Customer Churn Model.txt')

df

df_types = pd.DataFrame(data.dtypes).reset_index().drop("index", axis=1)
df_types = df_types.rename(columns={0:'Type'})

df = pd.concat([df,df_types], axis=1)

array = np.array(["{} - {}".format(data.values.transpose()[i].min(), data.values.transpose()[i].max())
                       for i in range(1,data.values.transpose().shape[0])])
array = np.hstack([np.array(['State Name']), array])

df_values = pd.DataFrame(array, columns=['Values'])
df = pd.concat([df[['Variable','Description']], df_values, df['Type']], axis=1)
df

#Format
d = {
    'Variable': [dict(selector="td", props=[('width','15em')]),
                dict(selector="th", props=[('text-align','center')])],
    'Description': [dict(selector="td", props=[('width','35em')]),
                   dict(selector="th", props=[('text-align','center')])],
    'Type': [dict(selector="td", props=[('width','15em')]),
            dict(selector="th", props=[('text-align','center')])],
    'Values': [dict(selector="td", props=[('width','7em')]),
            dict(selector="th", props=[('text-align','center')])]}

df = df.style.set_properties(**{'text-align':'center', 'padding-right':'30px'})        .set_table_styles(d)

display(df)





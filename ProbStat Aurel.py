#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, -5, 0.3, 6, -2, 4]  # numeric vector
b = ["one", "two", "three"]     # character vector
c = [True, True, True, False, True]  # logical vector
print(a)
print(b)
print(c)


# In[3]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_aurel = ["R1", "R2"]
c_aurel = ["C1", "C2"]
aurel_matrix = np.matrix(cells).reshape(2, 2)
print(aurel_matrix)


# In[4]:


import pandas as pd
import numpy as np

aurel1 = [1, 2, 3, 4]
aurel2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
aurel3 = [True, True, True, False]

dataku = pd.DataFrame({'ID': aurel1, 'Color': aurel2, 'Passed': aurel3})
print(dataku)


# In[5]:


import pandas as pd

data_aurel = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_aurel)


# In[6]:


pip install mysql-connector-python


# In[8]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices3"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM aurel_houseprices;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[9]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Brick'] == 'No']

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[10]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kondisi yang kompleks
df_filtered = df[(df['Brick'] == 'No') | (df['Neighborhood'] == 'East')]

# Menampilkan hasil filter
print(df_filtered)


# In[11]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ps2[aurel]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM nama_data;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[13]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['GENDER'] == 'P')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:





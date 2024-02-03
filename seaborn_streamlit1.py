import streamlit as st
import seaborn as sns
import pandas as pd
import xlwings as xw
import numpy as np



df0 = pd.DataFrame(np.random.randn(5000, 8), columns=("col %d" % i for i in range(8)))
categorical_fields = []
numeric_fields = []
option2 = ''

def user_input(df0):
    
    for col in df0.columns:
        if df0[col].dtypes == 'object':
            categorical_fields.append(col)
            unique = df0[col].unique()
            option = st.sidebar.multiselect('Choose your ' + str(col), unique,unique)
            #st.write('# You selected:', option)
            df0 = df0[df0[col].isin(option)]
    for col in df0.columns:
        #st.write('my header isssssss ' +str(col))
        if df0[col].dtypes == 'float64' and int(df0[col].min()) != int(df0[col].max()):
            numeric_fields.append(col)
            param1 = st.sidebar.slider(col,int(df0[col].min()), int(df0[col].max()), int(df0[col].min()))
            df0 = df0[df0[col]>=param1]
        
			
    option2 = st.sidebar.selectbox('Select the field', categorical_fields)
    
    st.dataframe(df0.describe())
    #st.write(df0.columns.to_list())
    
    import matplotlib.pyplot as plt
    for col in categorical_fields:
        
        fig2 = plt.figure(figsize=(10, 4))
        sns.countplot(x=df0[col], data = df0)
        st.pyplot(fig2)

    fig = sns.pairplot(df0, hue = option2)
    st.pyplot(fig)
  
    st.write(categorical_fields)
    st.write(numeric_fields)
    

user_input(df0)











import pandas as pd

dfwwwww = pd.DataFrame([[1,2,'field3_0','field4_0'],[5,526,'field3_1','field4_1'], [9,371,'field3_2','field4_2']], columns = ['fld1','fld2','fld3','fld4'])
print (dfwwwww)
dfwwwww.to_clipboard()

df1dfwwwww = pd.read_clipboard()
df1dfwwwww




















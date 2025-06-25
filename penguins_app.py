import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import random

st.title('Penguins Rock 🐧🐧🐧🐧🐧')

#Bring in the data
df=sns.load_dataset('penguins')
df=df.dropna()

#Show the data
st.dataframe(df)

#Show the barplot
fig=px.bar(tips_by_day,x='day',y='total_bill',title='Average Bill by Day')
st.plotly_chart(fig)

#Show the boxplot
fig=px.box(df,x='island',y='body_mass_g',title='Body Mass by Island')
st.plotly_chart(fig)

#Show the scatterplot
fig_scatter=px.scatter(df,x='body_mass_g',y='bill_length_mm',color='species',title='Body Mass vs Bill Length')
st.plotly_chart(fig_scatter)

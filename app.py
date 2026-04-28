import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Bike Sharing Dashboard 🚲")

# load data
day_df = pd.read_csv('day.csv')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# tambah fitur
day_df['year'] = day_df['dteday'].dt.year
day_df['month'] = day_df['dteday'].dt.month

# sidebar filter
year = st.sidebar.selectbox("Pilih Tahun", day_df['year'].unique())

filtered_df = day_df[day_df['year'] == year]

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Rentals", int(filtered_df['cnt'].sum()))
col2.metric("Avg Rentals", int(filtered_df['cnt'].mean()))
col3.metric("Registered Users", int(filtered_df['registered'].sum()))

st.subheader("Monthly Trend")
monthly = filtered_df.groupby('month')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=monthly, x='month', y='cnt', marker='o', ax=ax)
st.pyplot(fig)

st.subheader("Weather Impact")
weather = filtered_df.groupby('weathersit')['cnt'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=weather, x='weathersit', y='cnt', ax=ax2)
st.pyplot(fig2)

st.subheader("User Type Comparison")
user = filtered_df[['casual','registered']].sum()

fig3, ax3 = plt.subplots()
user.plot(kind='bar', ax=ax3)
st.pyplot(fig3)

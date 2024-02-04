import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit App
st.title('Early Warning System For Dropout Prediction')

# Read data from file (replace 'your_file.csv' with the actual file path)
file_path = 'C:/Users/khush/Desktop/dataset-MachineKnight/dataset.csv'

new_data = pd.read_csv(file_path)

# Display pie chart
if 'Target' in new_data.columns:  # Check if the 'Target' column exists in the DataFrame
    x = new_data['Target'].value_counts().index
    y = new_data['Target'].value_counts().values

    df = pd.DataFrame({
        'Target': x,
        'Count_T': y
    })

    # Create pie chart using Plotly Express
    fig = px.pie(df,
                 names='Target', 
                 values='Count_T',
                 title='How many dropouts, enrolled & graduates are there in Target column')

    fig.update_traces(labels=['Graduate', 'Dropout', 'Enrolled'], hole=0.4, textinfo='value+label', pull=[0, 0.2, 0.1])
    st.plotly_chart(fig)

else:
    st.warning("The 'Target' column is not found in the dataset.")


st.subheader("Box plot for Age distribution by Target:")
fig, ax = plt.subplots()
sns.boxplot(x='Target', y='Age at enrollment', data=new_data, ax=ax)
ax.set(xlabel='Target', ylabel='Age at enrollment', title='Box plot for Age distribution by Target')
st.pyplot(fig)

st.subheader("Count Plot of Daytime/Evening Attendance by Target:")
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x='Daytime/evening attendance', hue='Target', data=df, ax=ax)
ax.set(xlabel='Daytime/Evening Attendance', ylabel='Count', title='Count Plot of Daytime/Evening Attendance by Target')
st.pyplot(fig)

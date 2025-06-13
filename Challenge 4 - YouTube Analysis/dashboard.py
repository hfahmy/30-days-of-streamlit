import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import millify as mil

@st.cache_data
def load_data():
    """Loads in 4 dataframes and does light feature engineering"""
    df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]
    df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes',
                        'Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration',
                        'Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)']
    df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'], format='mixed')
    df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x,'%H:%M:%S'))
    df_agg['Avg_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.second + x.minute * 60 + x.hour * 60 * 60)
    df_agg['Engagement_ratio'] = (df_agg['Comments added'] + df_agg['Shares'] + df_agg['Likes']) / df_agg['Views']
    df_agg['Views / sub gained'] = df_agg['Views'] / df_agg['Subscribers gained']
    df_agg.sort_values('Video publish time', ascending = False, inplace = True)
    df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('All_Comments_Final.csv')
    df_time = pd.read_csv('Video_Performance_Over_Time.csv')
    df_time['Date'] = pd.to_datetime(df_time['Date'], format='mixed')
    return df_agg, df_agg_sub, df_comments, df_time 

#create dataframes from the function 
df_agg, df_agg_sub, df_comments, df_time = load_data()

st.sidebar.title('Filters')
st.sidebar.selectbox('Select a video', ['Aggregate Metrics', 'Individual Video Analysis'])

df_agg_metrics = df_agg[['Video publish time','Views','Likes','Subscribers','Shares','Comments added','RPM(USD)','Average % viewed',
                             'Avg_duration_sec', 'Engagement_ratio','Views / sub gained']]
metric_date_12mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months = 12)
metric_medians12mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_12mo].median()
metric_date_6mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months = 6)
metric_medians6mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_6mo].median()

col1, col2, col3, col4, col5 = st.columns(5)
columns = [col1, col2, col3, col4, col5]

count = 0
for i in metric_medians6mo.index:
    if isinstance(metric_medians6mo[i], pd.Timestamp): 
        continue
    with columns[count]:
        delta = (metric_medians6mo[i] - metric_medians12mo[i]) / metric_medians12mo[i]
        st.metric(
            label = i, 
            value = mil.millify(metric_medians6mo[i], precision=1), 
            delta = "{:.2%}".format(delta))
        count += 1
        if (count >= 5): 
            count = 0
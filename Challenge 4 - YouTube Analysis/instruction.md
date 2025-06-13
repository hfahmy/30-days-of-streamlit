## **Project Setup**
1. **Create a New Environment:**
    - [x] Open your terminal or Anaconda Prompt.
    - [x] Navigate to the folder where you want to store your project.
    - [x] Create a new virtual environment.
2. **Install Libraries:**
    - [x] Activate your new environment.
    - [x] Install the necessary Python libraries: `streamlit` and `plotly`.
3. **Download Data:**
    - [x] Download the YouTube channel dataset from the source mentioned in the video (e.g., Kaggle).
    - [x] Save the data files in your project folder.
4. **Set Up Your IDE:**
    - [x] Open your preferred Integrated Development Environment (IDE), such as Spyder or VS Code.
    - [x] Navigate to your project directory.
    - [x] Create a new Python script and save it in the project folder.

---

## **Data Preparation**

1. **Load Data:**
    - [x] Import the required libraries in your Python script: `pandas`, `numpy`, `plotly.graph_objects`, `plotly.express`, `streamlit`, and `datetime`.
    - [x] Load the `df_agg`, `df_agg_sub`, `df_comments`, and `df_time_series` datasets into pandas DataFrames.
    - [x] When loading `df_agg`, skip the first row to remove the "total" row.
2. **Clean and Transform Data:**
    - [x] Rename the columns in the `df_agg` DataFrame to remove special characters.
    - [x] Convert the 'Video publish time' column in `df_agg` to a datetime object.
    - [x] Convert the 'Date' column in `df_time_series` to a datetime object.
    - [x] Convert the 'Average view duration' column to a datetime object, then calculate the total seconds and store it in a new column named `Avg_duration_sec`.
    - [x] Create a new column named `Engagement_ratio` by calculating (`Comments added` + `Shares` + `Likes`) / `Views`.
    - [x] Create a new column named `Views_per_sub_gained` by calculating `Views` / `Subscribers gained`. Handle cases where `Subscribers gained` is zero to avoid division errors.
    - [x] Encapsulate these data loading and preparation steps into a single function and use Streamlit's caching (`st.cache_data`) to improve performance.

---

## **Dashboard Development**

### **Structure**

1. **Run the Streamlit App:**
    - Open a new terminal or Anaconda Prompt.
    - Activate your environment and navigate to your project folder.
    - Run the command to start your Streamlit application.
2. **Create a Sidebar:**
    - Add a sidebar to your app.
    - Include a select box in the sidebar to switch between "Aggregate Metrics" and "Individual Video Analysis."

### **Aggregate Metrics**

1. **Filter and Calculate Metrics:**
    - Filter the `df_agg` DataFrame to create a baseline dataset containing data from the last 12 months.
    - Calculate the median for your key metrics (e.g., Views, Likes, Subscribers gained) over this 12-month baseline.
    - Filter the `df_agg` DataFrame again to create a comparison dataset with data from the most recent 6 months.
    - Calculate the median for the same key metrics over this 6-month period.
2. **Display Metrics:**
    - Organize the metrics display using `st.columns`.
    - For each metric, use `st.metric` to display its 6-month median value and the percentage change (delta) compared to the 12-month median.

### **Video Performance Table**

1. **Prepare Data for Table:**
    - Select the relevant columns from your aggregated data to display, such as video title, views, and the calculated engagement ratios.
    - Format the 'Video publish time' column to show only the date (e.g., YYYY-MM-DD).
2. **Style and Display Table:**
    - Apply custom styling to the DataFrame to color-code numerical values (e.g., red for negative, green for positive).
    - Format columns with ratios as percentages.
    - Display the styled DataFrame using `st.dataframe`.

### **Individual Video Analysis**

1. **Video Selection:**
    - Add a `st.selectbox` dropdown menu populated with video titles from your data.
2. **Subscriber and Country Analysis:**
    - Filter the `df_agg_sub` DataFrame based on the video selected in the dropdown.
    - Create a new column to categorize viewers' countries. For example, use the country code to label entries as 'USA', 'India', or 'Other'.
    - Create a horizontal bar chart using Plotly Express (`px.bar`) to visualize views by subscriber status and the new country category.
    - Display the chart using `st.plotly_chart`.
3. **Cumulative Views Analysis:**
    - Merge your time series data (`df_time_series`) with your aggregated data (`df_agg`) on the video ID to link video publish times.
    - Calculate the 'Days since published' for each row in the time series data.
    - Create a pivot table from the time series data to show the daily views for each video within the first 30 days of its publication.
    - Using this pivot table, calculate the 20th, 50th (median), and 80th percentile for cumulative views across all videos for that 30-day period. This will be your performance baseline.
    - Calculate the cumulative views for the single video selected by the user.
    - Create a line chart using Plotly Graph Objects (`go.Figure`) with four lines: one for the selected video's cumulative views and three for the 20th, 50th, and 80th performance percentiles.
    - Display this comparative chart using `st.plotly_chart`.

---

## **Deployment (Optional)**

1. **Prepare for Deployment:**
    - Create a new public repository on GitHub.
    - Upload all your project files (Python script, data files) to the repository.
    - Generate a `requirements.txt` file that lists all the necessary libraries.
    - Upload the `requirements.txt` file to your GitHub repository.
2. **Deploy on Streamlit Cloud:**
    - Use Streamlit Cloud to deploy your app by linking it to your GitHub repository.
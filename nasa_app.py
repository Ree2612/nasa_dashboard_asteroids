import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import date, timedelta

# Streamlit UI
st.set_page_config(page_title="NASA Asteroid Dashboard", layout="wide")
st.title("🌠 NASA Asteroid Dashboard")

# --- Date Inputs ---
today = date.today()
start_date = st.date_input("Start Date", today - timedelta(days=3))
end_date = st.date_input("End Date", today)

if (end_date - start_date).days > 7:
    st.warning("⚠️ Date range should be 7 days or less (NASA API limit).")
    st.stop()

# --- NASA API Setup ---
API_KEY = "jiSCFqcXyySppVDYC6drZaySj2F1ycSZt7xMDMnh"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

# --- Fetch Data ---
with st.spinner("Fetching data from NASA..."):
    response = requests.get(url)
    data = response.json()

asteroid_data = []

for date_key in data['near_earth_objects']:
    for asteroid in data['near_earth_objects'][date_key]:
        asteroid_data.append({
            'name': asteroid['name'],
            'close_approach_date': asteroid['close_approach_data'][0]['close_approach_date'],
            'diameter_min_m': asteroid['estimated_diameter']['meters']['estimated_diameter_min'],
            'diameter_max_m': asteroid['estimated_diameter']['meters']['estimated_diameter_max'],
            'velocity_kmh': float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
            'distance_km': float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
            'is_potentially_hazardous': asteroid['is_potentially_hazardous_asteroid']
        })

df = pd.DataFrame(asteroid_data)
df['close_approach_date'] = pd.to_datetime(df['close_approach_date'])

st.success(f"Fetched {len(df)} asteroids between {start_date} and {end_date}")

# --- Show Table ---
with st.expander("📋 View Raw Data Table"):
    st.dataframe(df)

# --- Visualizations ---
st.subheader("🔍 Asteroid Insights")

# 1. Top 10 Largest Asteroids
fig1, ax1 = plt.subplots(figsize=(10, 5))
top10 = df.sort_values(by='diameter_max_m', ascending=False).head(10)
sns.barplot(x='name', y='diameter_max_m', hue='name', data=top10, ax=ax1, palette='magma', dodge=False, legend=False)
ax1.set_title('Top 10 Largest Asteroids')
ax1.set_ylabel('Max Diameter (m)')
ax1.set_xlabel('')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)

# 2. Scatter Plot - Velocity vs Distance
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(
    x='distance_km', y='velocity_kmh',
    size='diameter_max_m', sizes=(20, 200),
    data=df, alpha=0.6, ax=ax2, color='teal', legend=False
)
ax2.set_title('Velocity vs Distance')
ax2.set_xlabel('Distance (km)')
ax2.set_ylabel('Velocity (km/h)')
st.pyplot(fig2)

# 3. Daily Count of Asteroids
fig3, ax3 = plt.subplots(figsize=(10, 4))
daily_counts = df.groupby('close_approach_date').size().reset_index(name='count')
sns.lineplot(x='close_approach_date', y='count', data=daily_counts, marker='o', ax=ax3, color='darkgreen')
ax3.set_title('Daily Asteroid Count')
ax3.set_ylabel('Asteroids')
ax3.set_xlabel('Date')
plt.xticks(rotation=45)
st.pyplot(fig3)

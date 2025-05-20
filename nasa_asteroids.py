import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "YOUR API"

# --- USER INPUT FOR DATES ---
print("Enter a date range (max 7 days). Format: YYYY-MM-DD")
start_date = input("Start date: ")
end_date = input("End date: ")

# --- API REQUEST ---
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

response = requests.get(url)
data = response.json()

asteroid_data = []

for date in data['near_earth_objects']:
    for asteroid in data['near_earth_objects'][date]:
        name = asteroid['name']
        diameter_min = asteroid['estimated_diameter']['meters']['estimated_diameter_min']
        diameter_max = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
        velocity = float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
        distance = float(asteroid['close_approach_data'][0]['miss_distance']['kilometers'])
        approach_date = asteroid['close_approach_data'][0]['close_approach_date']
        hazardous = asteroid['is_potentially_hazardous_asteroid']

        asteroid_data.append({
            'name': name,
            'close_approach_date': approach_date,
            'diameter_min_m': diameter_min,
            'diameter_max_m': diameter_max,
            'velocity_kmh': velocity,
            'distance_km': distance,
            'is_potentially_hazardous': hazardous
        })

df = pd.DataFrame(asteroid_data)
df['close_approach_date'] = pd.to_datetime(df['close_approach_date'])

# --- PLOT FUNCTION ---
def plot_asteroid_data(df):
    plt.figure(figsize=(18, 5))

    # 1. Bar chart - Top 10 Largest Asteroids
    plt.subplot(1, 3, 1)
    top10 = df.sort_values(by='diameter_max_m', ascending=False).head(10)
    sns.barplot(x='name', y='diameter_max_m', hue='name', data=top10, palette='viridis', dodge=False, legend=False)
    plt.xticks(rotation=45, ha='right')
    plt.title('Top 10 Largest Asteroids')
    plt.ylabel('Max Diameter (m)')
    plt.xlabel('Asteroid Name')

    # 2. Scatter Plot - Velocity vs Distance
    plt.subplot(1, 3, 2)
    sns.scatterplot(
        x='distance_km',
        y='velocity_kmh',
        size='diameter_max_m',
        sizes=(20, 200),
        data=df,
        alpha=0.7,
        legend=False,
        color='orange'
    )
    plt.title('Velocity vs Distance')
    plt.xlabel('Distance from Earth (km)')
    plt.ylabel('Velocity (km/h)')

    # 3. Line chart - Daily count
    daily_counts = df.groupby('close_approach_date').size().reset_index(name='count')
    plt.subplot(1, 3, 3)
    sns.lineplot(x='close_approach_date', y='count', data=daily_counts, marker='o', color='green')
    plt.title('Daily Asteroid Approaches')
    plt.xlabel('Date')
    plt.ylabel('Number of Asteroids')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# --- CALLING THE FUNCTION ---
plot_asteroid_data(df)

<div align="center">
 
```
 _  _   _   ___   _     _  _ ___ ___  
| \| | /_\ / __| /_\   | \| | __/ _ \ 
| .` |/ _ \\__ \/ _ \  | .` | _| (_) |
|_|\_/_/ \_\___/_/ \_\ |_|\_|___\___/ 
```
 
**Real-time asteroid tracking powered by NASA's Near-Earth Object API.**
 
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![NASA API](https://img.shields.io/badge/NASA-NeoWs_API-0B3D91?style=flat-square&logo=nasa&logoColor=white)

 
</div>
 
---
 
## What is this?
 
**NASA Asteroid Dashboard** is an interactive Streamlit app that pulls live data from NASA's Near-Earth Object Web Service (NeoWs) and turns it into clean, readable visualizations.
 
Pick a date range, hit fetch, and instantly explore which asteroids are passing closest to Earth — their sizes, velocities, and approach distances — all in one dashboard.
 
> Built for space nerds, data enthusiasts, and anyone who wants to know what's flying past us today.
 
---
 
## Features
 
| Feature | Description |
|---|---|
| **Live NASA API** | Fetches real asteroid data for any custom date range |
| **Size Comparison** | Bar chart of the largest asteroids in the selected window |
| **Velocity vs. Distance** | Scatter plot showing speed vs. miss distance for each object |
| **Daily Approach Count** | Line chart tracking how many asteroids pass Earth each day |
| **Interactive UI** | Date range picker and filters via Streamlit |
 
---


## Tech Stack
 
```
Frontend     →  Streamlit
Data Source  →  NASA NeoWs API
Charting     →  Plotly / Matplotlib
Data Layer   →  Pandas
Language     →  Python 3.10+
```
 
---
 
## Getting Started
 
```bash
# Clone the repo
git clone https://github.com/Ree2612/nasa-asteroid-dashboard.git
cd nasa-asteroid-dashboard
 
# Install dependencies
pip install -r requirements.txt
 
# Add your NASA API key
echo "NASA_API_KEY=your_key_here" > .env
 
# Run
streamlit run nasa_asteroid_dashboard.py
```
 
> Get a free NASA API key at [api.nasa.gov](https://api.nasa.gov)
 
---
 
## How It Works
 
1. User selects a start and end date
2. App calls NASA's NeoWs API for that date range
3. Response is parsed and cleaned with Pandas
4. Three charts are rendered — size, velocity/distance, and daily count
5. All data updates live on date change
 
---
   
## Outputs
[streamlit-nasa_asteroid_dashboard-2025-05-20-22-05-17.webm](https://github.com/user-attachments/assets/3cf911d8-64c7-4059-a30a-0119a6f3f932)
![dashboard op1](https://github.com/user-attachments/assets/5ba50db0-0e4e-4745-a77a-d599965be686)
![ip result1](https://github.com/user-attachments/assets/05b7b7ff-8945-4ec3-b51d-206d24c11a3c)

<div align="center">
  <sub>Data sourced from NASA's public NeoWs API · Built with Python & Streamlit</sub>
</div>


# F1-LapTime-Analysis

# F1 Lap Time Analysis with FastF1 

Hi! I'm Pía, an 18-year-old engineering student and a huge Formula 1 fan   
This is a simple and fun project I made using Python and [FastF1](https://theoehrly.github.io/Fast-F1/) to analyze lap data from a real F1 race.

In this case, I analyzed the 2024 Italian Grand Prix (Monza) and chose my favorite driver: **Yuki Tsunoda** 💙  
But you can totally change the driver and session to whatever you want — it works with anyone on the grid.

---

## What this code does

- Connects to the official F1 API using FastF1
- Loads the race session data (lap times, pit stops, etc.)
- Filters the data by a specific driver (in this case, 'TSU' = Yuki)
- Finds the **fastest lap**
- Detects all **pit stop laps**
- Creates a graph that shows:
  - Each lap time
  - A red dot for the fastest lap
  - Purple “x” markers where the driver did pit stops

---

## What I learned

- How to use Python libraries like `pandas`, `matplotlib`, and `FastF1`
- How F1 teams visualize and study lap data
- How to read performance shifts during a race

---

##  Output example

Here’s a preview of the chart it generates:  


---

##  How to run it

1. Make sure you have Python installed
2. Install FastF1 by opening your terminal and running: pip install -U fastf1

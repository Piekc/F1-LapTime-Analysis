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
https://github.com/Piekc/F1-LapTime-Analysis/blob/59f43c4115f279e159bfe60f3aa03560b9375441/Yuki2.png 


---

##  How to run it

1. Make sure you have Python installed
2. Install FastF1 by opening your terminal and running: pip install -U fastf1
3. Code example: https://github.com/Piekc/F1-LapTime-Analysis/blob/9422b9260bc106bfa254dec6e09a60c408d4f5bb/Yuki_analisis2.py 
4. After writing the code open your terminal and run: python Name_of_your_file.py
5. The Graph appears on screen

If everything works, you'll see a graph with lap-by-lap performance.

---

## My thoughts

This was my first F1 data project ever and I loved it.  
I want to keep learning more about motorsport engineering and simulation.  
Feel free to use this code as a base for your own analysis — and if you improve it or build something cool with it, I’d love to see it!

---

## Change the driver

To analyze a different driver, just change this line:

```python
driver = 'TSU'  # Yuki Tsunoda

Use the 3-letter code for any F1 driver (like 'VER' for Verstappen, 'HAM' for Hamilton, etc.)

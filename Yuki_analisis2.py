import fastf1
from fastf1.plotting import setup_mpl
import matplotlib.pyplot as plt
import pandas as pd
import os

# Activamos caché
fastf1.Cache.enable_cache('f1_cache')

# Cargamos la sesión
session = fastf1.get_session(2024, 'Monza', 'Race')
session.load()

# Seleccionamos piloto
driver = 'TSU'  # Yuki Tsunoda

# Obtenemos las vueltas
laps = session.laps.pick_drivers(driver).reset_index(drop=True)

# Buscamos la vuelta más rápida
fastest_lap = laps.loc[laps['LapTime'] == laps['LapTime'].min()]
fastest_lap_number = int(fastest_lap['LapNumber'])

# Detectamos vueltas con pit stop
pit_laps = laps[laps['PitInTime'].notnull()]

# Configuramos estilo visual
setup_mpl()
plt.figure(figsize=(10, 5))

# Graficamos los tiempos de vuelta
plt.plot(laps['LapNumber'], laps['LapTime'].dt.total_seconds(), label=f'{driver} - Ritmo')

# Marcamos la vuelta más rápida (punto rojo)
plt.scatter(fastest_lap['LapNumber'], fastest_lap['LapTime'].dt.total_seconds(), color='red', label='Vuelta más rápida')

# Marcamos los pit stops (puntos morados)
plt.scatter(pit_laps['LapNumber'], pit_laps['LapTime'].dt.total_seconds(), color='purple', marker='x', label='Pit stop')

# Estética
plt.xlabel("Número de vuelta")
plt.ylabel("Tiempo de vuelta (segundos)")
plt.title(f"Tiempos de vuelta de {driver} en Monza 2024")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

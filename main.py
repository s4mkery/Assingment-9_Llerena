import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#Part 1
exercise_df = pd.read_csv('Exercise_Data.csv')

pulse_df = exercise_df.select_dtypes(include=['number']).drop(columns=['id'], errors='ignore').dropna()

#Heatmap

ax_heat = sns.heatmap(pulse_df, cmap= 'inferno')

ax_heat.set_title("Título Personalizado", fontsize=14, pad=12)
ax_heat.set_xlabel("Pulse", fontsize=11)
ax_heat.set_ylabel("Index", fontsize=11)

plt.show()

#Categorical Data

gym_df = pd.melt(exercise_df,id_vars=['diet', 'kind'],value_vars=['1 min', '15 min', '30 min'],var_name='time',value_name='pulse')

sns.catplot(data=gym_df,x='time',y='pulse', hue='diet', col='kind', kind='box', palette='Set3')
plt.show()

#Part 2

planets = sns.load_dataset('planets')

#Relational Plots

sns.scatterplot(data=planets,x='orbital_period',y='mass',alpha=0.6)

plt.xscale('log')
plt.yscale('log')

plt.title("Correlation: Orbital Period vs. Mass (Log-Log Scale)")
plt.xlabel("Orbital Period (Days - Log Scale)")
plt.ylabel("Mass (Jupiter Mass - Log Scale)")
plt.grid(True, which="both", ls=":", alpha=0.4)

plt.tight_layout()
plt.show()



sns.lineplot(data=planets,x='year',y='mass',hue='method',errorbar=None)

plt.yscale('log')
plt.title("Evolution of Discovered Planet Mass Over Years")
plt.xlabel("Discovery Year")
plt.ylabel("Average Mass (Jupiter Mass - Log Scale)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

#Distributional
clean_period = planets.dropna(subset=['orbital_period'])

sns.histplot(
    data=clean_period,
    x='orbital_period',
    log_scale=True,                 
    color='teal',
    bins=30              
)

plt.title("Distribution of Orbital Periods  (Log Scale)", fontsize=13)
plt.xlabel("Orbital Period (Days - Log10 Scale)")
plt.ylabel("Number of Planets")
plt.grid(axis='y', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()


sns.kdeplot(data=planets.dropna(subset=['orbital_period', 'mass']), x='orbital_period',y='mass', log_scale=(True,True), fill=True, cmap='rocket')

plt.title("Density Estimation: Orbital Period vs. Planetary Mass", fontsize=12, pad=12)
plt.xlabel("Orbital Period (Days - Log Scale)", fontsize=10)
plt.ylabel("Mass (Jupiter Mass - Log Scale)", fontsize=10)
plt.grid(True, which="both", ls=":", alpha=0.3)

plt.tight_layout()
plt.show()


#Categorical

top_methods = planets['method'].value_counts().head(5).index
filtered = planets[planets['method'].isin(top_methods)].copy()

sns.boxplot(data=filtered, x='method', y='distance', palette='Set3')

plt.yscale('log')
plt.title("Detection Range: Distance by Method (Log Scale)", fontsize=11, pad=10)
plt.xlabel("Detection Method", fontsize=10)
plt.ylabel("Distance to Earth (Parsecs - Log Scale)", fontsize=10)
plt.tick_params(axis='x', rotation=25)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.show()


sns.boxplot(data=filtered, x='method', y='year', palette='Set2')
plt.title("Historical Timeline: Discovery Year by Method", fontsize=11, pad=10)
plt.xlabel("Detection Method", fontsize=10)
plt.ylabel("Discovery Year", fontsize=10)
plt.tick_params(axis='x', rotation=25)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.show()
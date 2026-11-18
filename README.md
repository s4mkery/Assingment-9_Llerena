# Assingment-9_Llerena

This project conducts an in-depth exploratory data analysis (EDA) on NASA's exoplanet discovery catalog using the Seaborn `planets` dataset. The primary objective is to evaluate detection methodology biases, physical planetary attributes, and observational limits across multiple dimensions—specifically examining correlations, probability densities, and categorical distributions across orbital periods, masses, and distances.

By leveraging modern data visualization principles, this report deconstructs the multi-scale nature of astronomical observations and illustrates how different detection instruments systematically favor specific planetary sub-populations.

---

**Environment & Tech Stack**

The analysis is implemented in Python within a Jupyter Notebook environment, utilizing the following core libraries:

**Pandas (`pandas`)**:
  * Serves as the primary data manipulation and structuring layer.
  * Handles DataFrame transformations, subset filtering, null-value management (`dropna`), and categorical aggregations required for high-level statistical plotting.

**Seaborn (`seaborn`)**:
  * Operates as the high-level statistical visualization engine.
  * Native integration with Pandas DataFrames allows direct visual encoding of semantic variables (`x`, `y`, `hue`, `col`).
  * Utilized across three core visualization families:
    **Relational**: `scatterplot` and `lineplot` for multi-variable dependency and historical discovery trends.
    **Distributional**: `histplot` and bivariate `kdeplot` for probability mass and kernel density estimations.
    **Categorical**: `boxplot` for comparative quartile summaries, dispersion, and outlier detection.

**Matplotlib (`matplotlib.pyplot`)**:
  * Provides granular, low-level control over the figure anatomy and canvas layout.
  * Used explicitly to customize fine-grained chart elements that Seaborn abstracts away:
    **Axis Transformations**: Applying logarithmic scaling (`plt.xscale('log')`, `plt.yscale('log')`) to resolve extreme skewness and multi-decade orders of                               magnitude.
     **Typography & Metadata**: Fine-tuning chart titles (`plt.title`), axes labels (`plt.xlabel`, `plt.ylabel`), and tick adjustments.

---

**Visualization Taxonomy Implemented**

The analysis fulfills a balanced 6-figure taxonomy structured as follows:

1. **Relational Analysis**:
   * *Scatterplot*: Assessing the correlation between `orbital_period` and planetary `mass`.
   * *Temporal Lineplot*: Tracking the historical trajectory of discovered planet mass over discovery years (`year`).
2. **Distributional Analysis**:
   * *Histogram *: Identifying bimodal frequency clustering across `orbital_period` under logarithmic binning.
   * *kdplot*: Mapping joint continuous probability contours of `orbital_period` vs. `mass` to reveal distinct physical clustering regimes (Hot Jupiters vs. Cold Gas Giants).
3. **Categorical Analysis**:
   * *Spatial Range Boxplot*: Evaluating observational distance reach (`distance`) grouped by primary discovery `method`.
   * *Historical Timeline Boxplot*: Comparing detection era maturation and operational peaks (`year`) across discovery techniques.
---

**Findings**
 * *Explanation for elementary school students (Analogy)*
   
Imagine our heart is the rocket booster of a spaceship. When we are resting, the rocket is sitting peacefully on the launchpad with its engines idling     quietly (around 80 to 90 beats per minute). Walking is like taxiing along the runway: the thrusters are gently purring. But running is full blast-off!     To push the rocket through the sky, the main engines must fire at maximum power, sending the energy gauge skyrocketing up to 140 and 150 beats per minute    after 15 and 30 minutes.   Our food is the rocket fuel. The astronauts on the no-fat fuel (no fat, yellow boxes) had to rev their rocket boosters            significantly harder than those on the regular fuel (low fat, green boxes) just to fly at the very same speed

Figure A (2D KDE: Orbital Period vs. Planetary Mass): The density contours reveal that exoplanets naturally separate into two distinct physical populations rather than a single continuous gradient: the primary core clusters massive, cold gas giants orbiting over hundreds of days, while the lower secondary lobe  captures Hot Jupiters revolving tightly around their host stars in just a matter of days. Implementing bilateral logarithmic scaling was essential to prevent extreme values across multiple orders of magnitude from collapsing into an unreadable cluster at the origin.

Figure B (Boxplot: Detection Range by Method): The distribution of distances highlights the clear instrumental selection bias of modern astrophysics: traditional techniques such as Radial Velocity and Imaging are largely confined to our local stellar neighborhood (median distances around 40 to 50 parsecs), whereas space-borne Transit missions and Microlensing events successfully reach deep-field targets hundreds to thousands of parsecs away across the galaxy.

<img width="400" height="350" alt="image" src="https://github.com/user-attachments/assets/d2928432-778a-48f4-b133-848362049331" />  <img width="400" height="375" alt="image" src="https://github.com/user-attachments/assets/cab9de98-54f9-4795-8df2-80d72b64921d" />



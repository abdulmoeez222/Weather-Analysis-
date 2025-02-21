# Weather-Analysis-
A Python-based weather data analysis project using pandas to explore, filter, and summarize weather conditions.

# Weather Data Analysis

## Overview
This project analyzes weather data using **pandas** to extract useful insights from a dataset named `Weather_Dataset.csv`. The script performs various operations such as inspecting data, handling missing values, and grouping data for better understanding.

## Requirements
Ensure you have Python installed along with the following dependencies:

```bash
pip install pandas
```

## Dataset
The dataset used is `Weather_Dataset.csv`, which contains weather-related parameters such as temperature, humidity, wind speed, and weather conditions.

## Commands Used

### Basic Data Exploration
```python
import pandas as pd
data = pd.read_csv("Weather_Dataset.csv")

print(data.head())  # Displays first 5 rows
print(data.shape)  # Shows dataset dimensions
print(data.index)  # Displays index details
print(data.columns)  # Lists column names
print(data.dtypes)  # Displays data types of each column
print(data["weather"].unique())  # Unique values in 'weather' column
print(data.nunique())  # Number of unique values in each column
print(data.count())  # Non-null values in each column
print(data["Weather"].value_counts())  # Frequency of each weather type
print(data.info())  # General dataset information
```

### Unique Values & Filtering
```python
print(data["Wind_Speed_km/h"].nunique())  # Unique wind speed values
print(data["Wind_Speed_km/h"].unique())  # Displays all unique wind speeds

print(data.Weather.value_counts())  # Count occurrences of weather types
print(data.groupby("Weather").get_group('Clear'))  # Filters data where weather is 'Clear'

print(data[data["Wind_Speed_km/h"] == 4])  # Filters wind speed of 4 km/h
```

### Handling Missing Values
```python
print(data.isnull().sum())  # Count missing values in each column
```

### Renaming Columns
```python
data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
```

### Statistical Analysis
```python
print(data['Visibility_km'].mean())  # Average visibility
print(data['Press_kPa'].std())  # Standard deviation of pressure
print(data['Rel_Hum_%'].var())  # Variance of relative humidity
```

### Weather Condition Analysis
```python
print(data['Weather Condition'].value_counts())  # Count of each weather condition
print(data['Weather Condition'].str.contains('Snow').sum())  # Number of times Snow appears
print(data[data['Weather Condition'] == 'Fog'])  # Filter data where weather is 'Fog'
```

### Grouping Data
```python
print(data.groupby('Weather Condition').mean())  # Mean of each column per weather condition
print(data.groupby('Weather Condition').min())  # Minimum values per weather condition
print(data.groupby('Weather Condition').max())  # Maximum values per weather condition
```

### Complex Filtering
```python
print(data[(data['Wind_Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])  # Filters wind speed > 24 km/h and visibility = 25 km
```

## How to Run
1. Clone this repository:
```bash
git clone https://github.com/your-username/weather-data-analysis.git
```
2. Navigate to the project folder:
```bash
cd weather-data-analysis
```
3. Run the Python script:
```bash
python weather_analysis.py
```

## Contribution
Feel free to contribute by submitting issues or pull requests. Any suggestions and improvements are welcome!

## License
This project is open-source and available under the [MIT License](LICENSE).



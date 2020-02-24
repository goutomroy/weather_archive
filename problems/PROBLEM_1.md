# Problem 1 - Parsing an Archive File
Write a python function that takes a Weather Archive file and parses it into a list of dictionaries.

Weather Archive files are CSV files that contain the following fields:
- date (datetime) - represents the weather observation date and time)
- temperature (float) - average temperature in °F
- rainfall (float) - total rainfall during observation period in Inches
- barometricPressure (float) - atmospheric pressure in Inches Hg
- humidity (int) - relative humidity as a percentage
- windSpeed (int) - average wind speed in Mph
- windDirection (string) - direction label of prevailing wind, such as N, NE, NNE, etc

The Archive File [data/weather_archive.csv](../data/weather_archive.csv) contains 100 weather observations that you can use to test your function with.

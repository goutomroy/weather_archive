# Problem 2 - Weather Observations API
Create a python-based web service based on the following API Blueprint defined in [Appendix A](#appendix-a---api-blueprint-weather-observations). The API should only provide the following functionality:
 - view a single Observation (e.g. Detail View)
 - view a list of Observations (e.g. List View). The list view should include a 'Limit' parameter that limits the number of Observations returned (Default: 20).

Functionality for adding Weather Observations will be handled in [Problem 4](PROBLEM_4.md#problem-4---asynchronous-archive-file-processing).


## Appendix A - API Blueprint: Weather Observations

(API Blueprint based on https://apiblueprint.org)


```yaml
FORMAT: 1A

# Weather Observations API
A simple API for displaying weather observations. Readonly.

## Observation [/observation/{id}]
An Observation has the following attributes:

+ id - A unique integer id
+ date - An ISO8601 date when the weather observation was collected.
+ temperature - Average Temperature in °F.
+ rainfall - Total Rainfall since the last observation in Inches.
+ barometricPressure - Average Atmospheric Pressure in Inches Hg.
+ humidity - Average Relative Humidity as a percentage.
+ windSpeed - Average Wind Speed in Mph.
+ windDirection - Prevailing Wind Direction label (N, NNW, NW, ..., NNE).

+ Parameters
    + id: 1 (required, number) - An unique identifier of the observation.

### View an Observation Detail [GET]

+ Response 200 (application/json)

    + Body

            {
              "id": 1,
              "date": "2016-03-23T18:50:00Z",
              "temperature": 32.3,
              "rainfall": 0.0,
              "barometricPressure": 29.979,
              "humidity": 78,
              "windSpeed": 2,
              "windDirection": "SSW"
            }

## Observation Collection [/observation{?limit}]

+ Parameters
    + limit (number, optional) - The maximum number of observations to return.
        + Default: `20`

### List All Observations [GET]

+ Response 200 (application/json)

    + Body

            [
              {
                "id": 1,
                "date": "2016-03-23T18:50:00Z",
                "temperature": 32.3,
                "rainfall": 0.0,
                "barometricPressure": 29.979,
                "humidity": 78,
                "windSpeed": 2,
                "windDirection": "SSW"
              },
              {
                "id": 2,
                "date": "2016-03-23T18:55:00Z",
                "temperature": 32.4,
                "rainfall": 0.0,
                "barometricPressure": 29.977,
                "humidity": 78,
                "windSpeed": 2,
                "windDirection": "SSW"
              },
              {
                "id": 3,
                "date": "2016-03-23T19:00:00Z",
                "temperature": 32.5,
                "rainfall": 0.0,
                "barometricPressure": 29.972,
                "humidity": 78,
                "windSpeed": 3,
                "windDirection": "SSW"
              }
            ]
```

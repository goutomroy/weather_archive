# Problem 5 - Parsing a Binary Archive File

In an effort to reduce the payload size being transmitted from the weather station, a change was made to send the data encoded in a binary format instead of ASCII.

Make the following changes to your API:

- Add a new field to the Archive resource called `version` that tracks the Archive File version. CSV files should be marked as version 1. Binary files should be marked as version 2. Refer to [Appendix C](#appendix-c---api-blueprint-weather-archives-complete) for the complete Weather Archives API blueprint.
- Write a new binary file parser. The binary Archive file contains the same fields as the CSV Archive file. The format of the binary file is explained in [Appendix D](#appendix-d---binary-weather-archive-file-format).
- Update the Weather Archive API to allow a user to POST binary Archive File content to the API. The binary Archive file will need to get parsed by a [celery](https://github.com/celery/celery) task that creates individual Weather Observation resource objects.

The binary file [data/weather_archive.bin](../data/weather_archive.bin) contains 100 Weather Observations that you can use to test your function with. The Weather Observations in this binary file should be identical to the Weather Observations parsed by the [CSV Archive File](../data/weather_archive.csv).

## cURL Example
The following curl statement can be used to test your API:
```shell
$ curl -i -H 'content-type:application/octet-stream' --data-binary @data/weather_archive.bin localhost:8000/archive/
```

## Appendix C - API Blueprint: Weather Archives (Complete)
```yaml
FORMAT: 1A

# Weather Archives API
A simple API for viewing Weather Archive data.

## Archive [/archive/{id}]
An Archive object has the following attributes:

+ id - A unique integer id
+ created - An ISO8601 date when the Archive object was created.
+ archive_file - Relative path to the location of the Archive file.
+ status - Status of the Archive file. One of ["Pending", "Running", "Complete", "Failure"].
+ version - Version of the Archive file. Version 1 is CSV format. Version 2 is binary format.

+ Parameters
    + id: 1 (required, number) - An unique identifier of the message.

### View an Archive Detail [GET]

+ Response 200 (application/json)

    + Body

            {
              "id": 1,
              "created": "2019-09-23T16:21:27Z",
              "archive_file": "archive/2019/09/23/0ae02dd3-6212-46c2-9068-7fdcc74fff00.csv",
              "status": "Complete",
              "version": 1
            }

## Archive Collection [/archive{?limit}]

+ Parameters
    + limit (number, optional) - The maximum number of results to return.
        + Default: `20`

### List All Archives [GET]

+ Response 200 (application/json)

    + Body

            [
              {
                "id": 1,
                "created": "2019-09-23T16:21:27Z",
                "archive_file": "archive/2019/09/23/0ae02dd3-6212-46c2-9068-7fdcc74fff00.csv",
                "status": "Complete",
                "version": 1
              },
              {
                "id": 2,
                "created": "2019-09-23T16:27:16Z",
                "archive_file": "archive/2019/09/23/42f74e19-bfe5-47ae-8cde-a03853fbb18c.csv",
                "status": "Running",
                "version": 1
              },
              {
                "id": 3,
                "created": "2019-09-23T16:32:49Z",
                "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
                "status": "Pending",
                "version": 1
              },
              {
                "id": 4,
                "created": "2019-09-23T16:34:08Z",
                "archive_file": "archive/2019/09/23/8f4ca522-9fa4-4cd8-98fc-ac8f857782f4.bin",
                "status": "Pending",
                "version": 2
              }
            ]

### Create a New Archive [POST]

The body of the request is expected to be the weather archive content in CSV format.

+ Request CSV Archive

    + Headers

            Content-Type: text/csv

+ Response 201 (application/json)

    + Body

            {
              "id": 3,
              "created": "2019-09-23T16:32:49Z",
              "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
              "status": "Pending",
              "version": 1
            }

+ Request Binary Archive

    + Headers

            Content-Type: application/octet-stream

+ Response 201 (application/json)

    + Body

            {
              "id": 4,
              "created": "2019-09-23T16:34:08Z",
              "archive_file": "archive/2019/09/23/8f4ca522-9fa4-4cd8-98fc-ac8f857782f4.bin",
              "status": "Pending",
              "version": 2
            }
```


## Appendix D - Binary Weather Archive File Format

A Weather Archive file consists of a set of Weather Observation records. Data is recorded in the file in **Little-Endian** ordering (most significant byte last). Each Weather Observation record is 13 bytes long. The following table describes the format of a Weather Observation record:

|Field              |Offset|Byte|Units          |Description|
|-------------------|------|----|---------------|-----------|
|Date               |0     |2   |See Description|Observation Date: ((Year - 2000) * 512 + Month * 32 + Day). See [Date Field](#date-field) for more info.|
|Time               |2     |2   |See Description|Observation Time: (Hour * 64 + Minute). See [Time Field](#time-field) for more info.|
|Temperature        |4     |2   |°F / 10        |Average Outside Temperature over the archive period.|
|Rainfall           |6     |2   |Inch / 100     |Rainfall over the archive period.|
|Barometric Pressure|8     |2   |Hg / 1000      |Barometer reading at the end of the archive period.|
|Humidity           |10    |1   |%              |Outside Humidity at the end of the archive period.|
|Wind Speed         |11    |1   |Mph            |Average Wind Speed over the archive interval.|
|Wind Direction     |12    |1   |               |Prevailing or Dominant Wind Direction code. See [Wind Direction Codes](#wind-direction-codes) for more info.|

### Date Field
The Date field is a 2-byte value.
- The 7 most significant bits represent the number of years after 2000 (0 to 127)
- The next 4 most significant bits represent the month (1 to 12)
- The 5 least significant bits represent the day (1 to 31)

You can convert a date into the integer value stored in the date field with the following formula:
date_value = (Year - 2000) * 512 + Month * 32 + Day

### Time Field
The Time field is a 2-byte value.
- The 5 most significant bits are unused
- The next 5 most significant bits represent the hour (0 to 24)
- The 6 least significant bits represent the minute (0 to 59)

You can convert a timestamp into the integer value stored in the time field with the following formula:
time_value = Hour * 64 + Minute

### Wind Direction Codes

|Code|Direction Label|
|----|---------------|
|0   |N              |
|1   |NNE            |
|2   |NE             |
|3   |ENE            |
|4   |E              |
|5   |ESE            |
|6   |SE             |
|7   |SSE            |
|8   |S              |
|9   |SSW            |
|10  |SW             |
|11  |WSW            |
|12  |W              |
|13  |WNW            |
|14  |NW             |
|15  |NNW            |

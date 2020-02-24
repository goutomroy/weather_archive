# Problem 4 - Asynchronous Archive File Processing
Add functionality to your endpoint to allow a user to POST a Weather Archive file to the API. You can use the CSV Weather Archive file [data/weather_archive.csv](../data/weather_archive.csv) to test your API. When POSTing a Weather Archive file to the API, the request body should be the CSV content of the Weather Archive file.

When an archive file gets POSTed to the API, the following things should happen:
  - The request body content should get written to a new file in local storage
  - A new Archive resource object should get created (persisted to a database), and then viewable through the API
  - A [celery](http://www.celeryproject.org/) task should get created that would parse the Weather Archive file, and create individual Weather Observation resource objects.

## cURL Example
The following curl statement can be used to test your API:
```shell
$ curl -i -H 'content-type:text/csv' --data-binary @data/weather_archive.csv localhost:8000/archive/
```

## Appendix C - API Blueprint: Create Weather Archives
```yaml
FORMAT: 1A

# Weather Archives API
A simple API for creating and viewing Weather Archive data.

## Archive Collection [/archive]

### Create a New Archive [POST]

The body of the request is expected to be the weather archive content in CSV format.

+ Request

    + Headers

            Content-Type: text/csv

+ Response 201 (application/json)

    + Body

            {
              "id": 3,
              "created": "2019-09-23T16:32:49Z",
              "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
              "status": "Pending"
            }
```

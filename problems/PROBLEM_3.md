# Problem 3 - Weather Archives API
Add a new resource to your web service based on the API Blueprint defined in [Appendix B](#appendix-b---api-blueprint-weather-archives). The API should add the following functionality:
 - view a single Archive (e.g. Detail View)
 - view a list of Archives (e.g. List View). The list view should include a 'Limit' parameter that limits the number of Archives returned (Default: 20). 


## Appendix B - API Blueprint: Weather Archives

(API Blueprint based on https://apiblueprint.org)


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

+ Parameters
    + id: 1 (required, number) - An unique identifier of the message.

### View an Archive Detail [GET]

+ Response 200 (application/json)

    + Body

            {
              "id": 1,
              "created": "2019-09-23T16:21:27Z",
              "archive_file": "archive/2019/09/23/0ae02dd3-6212-46c2-9068-7fdcc74fff00.csv",
              "status": "Complete"
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
                "status": "Complete"
              },
              {
                "id": 2,
                "created": "2019-09-23T16:27:16Z",
                "archive_file": "archive/2019/09/23/42f74e19-bfe5-47ae-8cde-a03853fbb18c.csv",
                "status": "Running"
              },
              {
                "id": 3,
                "created": "2019-09-23T16:32:49Z",
                "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
                "status": "Pending"
              }
            ]
```

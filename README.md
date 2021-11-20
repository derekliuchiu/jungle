## Jungle API documentation

Base Url: `api.jungleapi.org`  

### Routes
`POST /insert`
Tracks Amazon product if not tracked already, expects JSON format input

| JSON Key | Description | Example |  
| ----------- | ----------- | ----------- |
| `ASIN` | Amazon product identifier | `B000YDDF6O` | 

Response
| JSON Key | Description | Example |  
| ----------- | ----------- | ----------- |
| `success` | Whether insert was successful or not | `true` or `false` |
| `message` | Description of whether insertion was successful | `successfully inserted ASIN` or `invalid ASIN` |

```json
{
  "success": true, 
  "message": "successfully inserted ASIN"
}
```

`GET /get/:ASIN`
Gets the prices of a product with the given ASIN since the product has been tracked

| Parameters | Description | Example |  
| ----------- | ----------- | ----------- |
| `date` | Date of when price was scraped (`MM/DD/YYYY`) can be optional | `12/22/2001` |
| `when` | specifies dates `before`, `after`, or `exact`-ly on, the given `date`, by default `exact` | `before` |

Response
| JSON Key | Description | Example |  
| ----------- | ----------- | ----------- |
| `success` | Whether get was successful or not | `true` or `false` |
| `error` | error message if there was one | `invalid date` |
| `prices` | list of prices with associated dates | see below |

```json
{
  "success": true, 
  "prices": [
    {
      "time": "2021-11-17 06:07:08",
      "price": 39.99
    },
    {
      "time": "2021-11-17 06:09:08",
      "price": 20.99
    }
  ]
}
```

### TODO
- amazon\_domain param
- 


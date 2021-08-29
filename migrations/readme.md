## sql migrations
these "migrations" are sql queries that should be run once to set up the database or add new fields/etc to an existing database

| Filename    | Description |
| ----------- | ----------- |
| create\_prices\_db.py | creates a database called `Prices` |
| create\_product\_prices\_table.py | creates a table in the `Prices` database called `ProductPrices` with 2 fields, a primary string id and a double price |

### TimeTracker
This is a simple DRF app to allow for the creation and viewing of timesheets and subsequent entries to the same.

#### Setup
You will first need to `git clone` the project. Once that is complete, you can simply run a `docker-compose up` from the project root to setup a local instance.

There is already a superuser configured within the system (user_id=1) for you to create timesheets against.

##### Testing
There are four endpoints which have been configured:
1) create timesheet: POST - localhost:8000/timesheets
2) crate lineitem: POST - localhost:8000/entries
3) view timesheets: GET - localhost:8000/timesheets
4) view lineitem: GET - localhost:8000/entries

Each endpoint accepts a method body (not ideal for the GET endpoints but I spent more time debugging connection issues than I anticipated). The bodies are as follows:
1) POST - localhost:8000/timesheets
```{ "user_id": 1, description: "", rate: 74.99 }```
2) POST - localhost:8000/entries 
```{ "timesheet_id": 1, date: "2025-09-07", minutes: 50 }```
3) GET - localhost:8000/timesheets
```{ "user_id": 1 }```
4) GET - localhost:8000/entries
```{ "timesheet_id": 1 }```

##### Future Enhancements
Unfortunately, as I said, time got away from me with debugging the postgres image configuration, connecting the django image to the db, and configuring the docker endpoints to accept the proper values. That coupled with minor interruptions from my kids, I'd say I spent about two and half hours of actual time working on getting everything properly functioning. My very ambitious goal was, ultimately, to code a simple react SPA with a tabular view of the timesheets and lineitems as well as feature a login page with user authentication. That would be at the top of my list to complete with additional time followed closely by unit tests of the endpoints and subsequently the UI navigations.

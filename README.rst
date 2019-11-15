tickets
=======

This is a code challenge project: it allows anonymous users to
imitate cinema tickets selling flow.

Settings
--------

It has very modest set of setting, to start-up the app you
basically need to install dependencies from pipfile (I used pipenv here), makemigrations and migrate.
I used sqlite here for the sake of simplicity.



Versions
********
- django = "2.2.7"
- django rest framework = "3.10.3"
- factory-boy = "2.12.0"

For api get and post requests I used mostly Curl.

Basic Api Reference
-------------------

Get List of 'Active' Movies or Create A New One:
`/api/movie`

Get List of all Available Rooms and Their Capacity:
`/api/rooms`

Get List of Current Showings or Create A New One:
`/api/showings`


Format for creating a new Showing (you have to know movie Id and room id beforehand), example:

- "price_per_ticket": "10"
- "movie": movie.id
- "showing_room": room.id
- "remaining_seats": "20"
- "start": "2019-10-25 14:30"
- "end": "2019-10-25 15:30"

GET request will return all the actual Showings (Movie + Room + Time Scheduled)







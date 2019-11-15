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

Basic Api Reference
-------------------

Get List of 'Active' Movies or Create A New One:
`/api/movie`

Get List of all Available Rooms and Their Capacity:
`/api/rooms`





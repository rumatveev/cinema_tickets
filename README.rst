tickets
=======

This is a code challenge project: it allows anonymous users to
imitate cinema tickets selling/buying flow. This is an API-only implementation,
as requested. Post requests should contain valid json.

Settings
--------

It has very modest set of setting, to start-up the app you
basically need to install dependencies from pipfile (I used pipenv here), makemigrations and migrate.
I used sqlite here for the sake of simplicity.

Flow
****
**Seller:**

(1) 'Create' a Movie -> (2) 'Create' a Room -> (3) Create Showing

**Customer:**

(1) Get all Showings Available -> (2) Place an Order


Versions
********
- django = "2.2.7"
- django rest framework = "3.10.3"
- factory-boy = "2.12.0"

For api get and post requests testing I used mostly Curl.

Basic Api Reference
*******************

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

The main API endpoint to interact with customers and management,
to list orders or place a new one:
`/api/order`

Format for placing a new Order (buying a ticket/tickets), example:

- "email": "test@test.com"
- "showing": showing.id
- "quantity": '1'





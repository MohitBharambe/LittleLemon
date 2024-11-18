Little Lemon API Restaurant  Project

API Endpoints to test:

To add/register or display users: Request Type: POST & GET 
http://localhost:8000/auth/users/ - params = username, email & password

To get a Token for a user: Request Type: POST
http://localhost:8000/auth/token/login/ - params = password & username

To Logout a user: Request Type: POST
http://localhost:8000/auth/token/logout/ - params = username & passsword

To Book a Table: Request Type: POST
http://localhost:8000/restaurant/booking/tables/
- params = name, guests & booking_date

To View or Update Menu Items: Request Type: GET, POST, PUT
http://localhost:8000/restaurant/menu-items/
& http://localhost:8000/restaurant/menu-items/1
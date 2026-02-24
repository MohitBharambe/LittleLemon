## Little Lemon API Restaurant Project - [Meta Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer)

### This repository includes the Capstone Project in the [Meta Back-End Developer Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer) offered by Meta through Coursera. 
---
### About the Capstone Project:
#### The Capstone project enables you to demonstrate multiple skills by solving an authentic real-world problem. You’ll test your abilities in full-stack back-end development in a real-life scenario by composing a Django web app. 
---
### Some Instructions For Peer Reviewers:

## API Endpoints to test:

### To add/register or display users: 
Request Type: `POST` | `GET`
```
http://localhost:8000/auth/users/  
```
params = `username`, `email` & `password`

---
### To get a Token for a user: 
Request Type: `POST`
```
http://localhost:8000/auth/token/login/ 
```
params = `password` & `username`

---
### To Logout a user:
Request Type: `POST`
```
http://localhost:8000/auth/token/logout/ 
```
params = `username` & `passsword`

---
### To Book a Table: 
Request Type: `POST`
```
http://localhost:8000/restaurant/booking/tables/
```
params = `name`, `guests` & `booking_date`

---
### To View or Update Menu Items:
Request Type: `GET` | `POST` | `PUT`
```
http://localhost:8000/restaurant/menu-items/
```
& 
```
http://localhost:8000/restaurant/menu-items/1
```
params = `name`, `price` & `quantity`

---

---
New Line added by Uttkarsh
# Authentication

**Note**:- For endpoints which require the authentication, provide `Authorization` header as `Bearer "FakeAcessToken"`

### Login

```
POST /api/v1/auth/login
```

**Parameters**

Name              | Data Type | Required | Default Value  | Description
------------------|-----------|----------|----------------|--------------------
email             | text      | true     | null           | email of the user.
password          | text      | true     | null           | password of the user.

__NOTE__ 

- Error out in case of invalid email/password.
- Error out in case of missing **required** attributes.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
Status: 200 OK
```json
{
    "id": "171956bd-717f-4021-a901-c5be80fd469b",
    "first_name": "John",
    "last_name": "Howley",
    "email": "hello@example.com",
    "phone_number": "",
    "is_active": true,
    "is_staff": false,
    "is_superuser": false,
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4ODI0MTU2NSwianRpIjoiYTA1OTUzZTE2OTNiNGU0M2IxMTllMjYwMzM5M2NhNWYiLCJ1c2VyX2lkIjoiYjgxY2FkNmQtMGQ1Ni00ODQxLTg1ZWUtODJjNDQ2ZGEzOGI5In0.t_P43_QiNFk2zhNdHRvJGD68jZWWcGrBtZd6G0obINw",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg4MTU1NDY1LCJqdGkiOiIyMmNhNTNkMjgyZDQ0NTc3YjdjMTA4ZDA4M2I2MjMxYyIsInVzZXJfaWQiOiJiODFjYWQ2ZC0wZDU2LTQ4NDEtODVlZS04MmM0NDZkYTM4YjkifQ.qWzd1WVmOpB5GCeCBLnjcnafZuudwPWWUPhSiCpUp9Q"
    }
}
```

### Register

```
POST /api/v1/auth/register
```

**Parameters**

Name              | Data Type | Required | Default Value  | Description
------------------|-----------|----------|----------------|--------------------
email             | text      | true     | null           | email of the user.
password          | text      | true     | null           | password of the user.
first_name        | text      | false    | ""             | first name of the user.
last_name         | text      | false    | ""             | last name of the user.
phone_number      | text      | false    | ""             | mobile number of the user.

__NOTE__
- Error out if email is already registered.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909",
    "first_name": "John",
    "last_name": "Howley",
    "phone_number": "+911234567890"
}
```

**Response**
Status: 201 Created
```json
{
    "id": "1f19560d-f1ff-4021-a901-c50e80fd4690",
    "first_name": "John",
    "last_name": "Howley",
    "email": "hello@example.com",
    "phone_number": "+911234567890",
    "is_active": true,
    "is_staff": false,
    "is_superuser": false,
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4ODI0MTU2NSwianRpIjoiYTA1OTUzZTE2OTNiNGU0M2IxMTllMjYwMzM5M2NhNWYiLCJ1c2VyX2lkIjoiYjgxY2FkNmQtMGQ1Ni00ODQxLTg1ZWUtODJjNDQ2ZGEzOGI5In0.t_P43_QiNFk2zhNdHRvJGD68jZWWcGrBtZd6G0obINw",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg4MTU1NDY1LCJqdGkiOiIyMmNhNTNkMjgyZDQ0NTc3YjdjMTA4ZDA4M2I2MjMxYyIsInVzZXJfaWQiOiJiODFjYWQ2ZC0wZDU2LTQ4NDEtODVlZS04MmM0NDZkYTM4YjkifQ.qWzd1WVmOpB5GCeCBLnjcnafZuudwPWWUPhSiCpUp9Q"
    }
}
```
### Logout

```
POST /api/v1/auth/logout (requires authentication)
```

**Parameters**

Name              | Data Type | Required | Default Value  | Description
------------------|-----------|----------|----------------|--------------------
refresh           | text      | true     | null           | The refresh token of the current session.

**Request**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4ODI0MTU2NSwianRpIjoiYTA1OTUzZTE2OTNiNGU0M2IxMTllMjYwMzM5M2NhNWYiLCJ1c2VyX2lkIjoiYjgxY2FkNmQtMGQ1Ni00ODQxLTg1ZWUtODJjNDQ2ZGEzOGI5In0.t_P43_QiNFk2zhNdHRvJGD68jZWWcGrBtZd6G0obINw"
}
```

**Response**
Status: 204 No-Content


### Refresh access token

```
POST /api/v1/auth/refresh
```

**Parameters**

Name              | Data Type | Required | Default Value  | Description
------------------|-----------|----------|----------------|--------------------
refresh           | text      | true     | null           | The refresh token of the current session.

**Request**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4ODM1Mzg2OCwianRpIjoiNDQ4MDE2OTk3ZDJmNGM1YThiNGI3ODRlNTNmNzc2ZDgiLCJ1c2VyX2lkIjoiYjgxY2FkNmQtMGQ1Ni00ODQxLTg1ZWUtODJjNDQ2ZGEzOGI5In0.WyRZ_5rByRH9pZojHc5tmB9s95DPDDWHzFMj2lpTVkw"
}
```

**Response**
Status: 200 OK

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg4ODc2MjgwLCJqdGkiOiI1MTYxM2QzOTliMGM0OTVlOGM1MDM5YmI0NzA5ZTZhMCIsInVzZXJfaWQiOiJmYmNmYTczZC0xNDdjLTQyOTUtYTM2Ny0xNmI0YmZlODQxODUifQ.-rsxySyJ04qBYQi7BQSgzp3Djh5OxQXZzGrMx29xy_U",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4OTA0ODE4MCwianRpIjoiOWM5NzE4ODM2OWEwNDFkZGEzMjdjMmIzMzI4ZmRjNjAiLCJ1c2VyX2lkIjoiZmJjZmE3M2QtMTQ3Yy00Mjk1LWEzNjctMTZiNGJmZTg0MTg1In0.PvzT-P0Swtgi1jUm2iNTKo84A9kF9n1DY2R21CFI_l4"
}
```

### Change password

```
POST /api/v1/auth/password_change (requires authentication)
```

**Parameters**

Name             | Description
-----------------|-------------------------------------
current_password | Current password of the user.
new_password     | New password of the user.

**Request**
```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

**Response**
Status: 204 No-Content

### Request password for reset

Send an email to user if the email exist.

```
POST /api/v1/auth/password_reset
```

**Parameters**

Name  | Description
------|-------------------------------------
email | (required) valid email of an existing user.

**Request**
```json
{
    "email": "hello@example.com"
}
```

**Response**
Status: 200 OK
```json
{
    "message": "Further instructions will be sent to the email if it exists"
}
```


### Confirm password reset

Confirm password reset for the user using the token sent in email.

```
POST /api/v1/auth/password_reset_confirm
```

**Parameters**

Name          | Description
--------------|-------------------------------------
new_password  | New password of the user
token         | Token decoded from the url (verification link)

**Request**
```json
{
    "new_password": "new_pass",
    "token" : "IgotTHISfromTHEverificationLINKinEmail"
}
```

**Response**
Status: 204 No-Content

# Users

### Get User Detail

```
GET /api/v1/users/:id (requires authentication)
```

Retrieves the detail of specific user corresponding to the ID provided

**Response**
Status: 200 OK
```json
{
  "id": "b81cad6d-0d56-4841-85ee-82c446da38b9",
  "email": "hello@example.com",
  "first_name": "John",
  "last_name": "Howley",
  "phone_number": "+911236547890",
  "is_staff": true,
  "is_active": true
}
```

### Update User Detail

```
PATCH /api/v1/users/:id (requires authentication)
```

Updates the detail of specific user corresponding to the ID provided

**Request**
```json
{
    "first_name": "Chris",
    "last_name": "Hemsworth"
}
```

**Response**
Status: 200 OK
```json
{
  "id": "b81cad6d-0d56-4841-85ee-82c446da38b9",
  "email": "hello@example.com",
  "first_name": "Chris",
  "last_name": "Hemsworth",
  "phone_number": "+911236547890",
  "is_staff": true,
  "is_active": true
}
```

### Delete User

```
DELETE /api/v1/users/:id (requires authentication)
```

**Response**
Status: 204 NO CONTENT

# Events

### Create Event

Creates an event

```
POST /api/v1/events/ (requires authentication)
```

**Parameters**


Name          | Data Type | Required | Default Value| Description
--------------|-----------|----------|--------------|--------------------
name          | text      | true     | null         | Title of the event.
description   | text      | true     | null         | Description of the event.
scheduled_time| text      | true     | null         | The date and time of event.
set_reminder  | boolean   | false    | True         | If reminder should be sent to the user for the event.


**Request**
```json
{
  "name": "Sample event",
  "description": "sample description",
  "scheduled_time": "2020-12-03T04:00:00Z",
  "set_reminder": false
}
```

**Response**
Status: 201 CREATED
```json
{
  "url": "http://localhost:8000/api/v1/events/fb5272fb-b34b-4d02-9275-e9a5785b6199",
  "id": "fb5272fb-b34b-4d02-9275-e9a5785b6199",
  "name": "Sample event",
  "owner": "http://localhost:8000/api/v1/users/a78b4e1f-cda7-4521-a3e9-5e687675840b",
  "created_at": "2020-05-12T17:32:53.217026+05:30",
  "modified_at": "2020-05-12T17:32:53.217127+05:30",
  "description": "sample description",
  "scheduled_time": "2020-12-03T09:30:00+05:30",
  "set_reminder": false,
  "has_reminder_sent": false
}
```

### Get Event List 

```
GET /api/v1/events/ (requires authentication)
```

This retrieves the list of events related with the authenticated user

**Response**
Status: 200 OK
```json
[
  {
    "url": "http://localhost:8000/api/v1/events/fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "id": "fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "name": "Sample event",
    "owner": "http://localhost:8000/api/v1/users/a78b4e1f-cda7-4521-a3e9-5e687675840b",
    "created_at": "2020-05-12T17:32:53.217026+05:30",
    "modified_at": "2020-05-12T17:32:53.217127+05:30",
    "description": "sample description",
    "scheduled_time": "2020-12-03T09:30:00+05:30",
    "set_reminder": false,
    "has_reminder_sent": false
  }
]
```

### Retrieve Event

```
GET /api/v1/events/:id (requires authentication)
```

Retrieves the detail of specific event corresponding to the ID provided

**Response**
Status: 200 OK
```json
{
    "url": "http://localhost:8000/api/v1/events/fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "id": "fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "name": "Sample event",
    "owner": "http://localhost:8000/api/v1/users/a78b4e1f-cda7-4521-a3e9-5e687675840b",
    "created_at": "2020-05-12T17:32:53.217026+05:30",
    "modified_at": "2020-05-12T17:32:53.217127+05:30",
    "description": "sample description",
    "scheduled_time": "2020-12-03T09:30:00+05:30",
    "set_reminder": false,
    "has_reminder_sent": false
}
```

### Update Event

```
PATCH /api/v1/events/:id (requires authentication)
```

Updates the specific event corresponding to the ID provided

**Request**
```json
{
    "name": "Updated Event Name"
}
```

**Response**
Status: 200 OK
```json
{
    "url": "http://localhost:8000/api/v1/events/fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "id": "fb5272fb-b34b-4d02-9275-e9a5785b6199",
    "name": "Updated Event Name",
    "owner": "http://localhost:8000/api/v1/users/a78b4e1f-cda7-4521-a3e9-5e687675840b",
    "created_at": "2020-05-12T17:32:53.217026+05:30",
    "modified_at": "2020-05-12T17:32:53.217127+05:30",
    "description": "sample description",
    "scheduled_time": "2020-12-03T09:30:00+05:30",
    "set_reminder": false,
    "has_reminder_sent": false
}
```

### Delete Event

```
DELETE /api/v1/events/:id (requires authentication)
```

Deletes the event corresponding to the given ID

**Response**
Status: 204 NO CONTENT

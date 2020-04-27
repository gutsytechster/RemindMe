# Authentication

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
    "auth_token": "Aebdbe703ccd50376ed3a7cf9fc7ae9614e0ac130"
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
    "auth_token": "ebdbe703ccd50376ed3a7cf9fc7ae9614e0ac130"
}
```
### Logout

```
POST /api/v1/auth/logout (requires authentication)
```

**Response**
Status: 204 No-Content

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
alert_date    | text      | true     | null         | The date at which the alert should be sent.
alert_interval| text      | true     | null         | The interval at which the alert should be resent.


**Request**
```json
{
    "name": "Sample Event Name",
    "alert_date": "2020-12-03T04:00:00Z",
    "alert_interval": "02:00"
}
```

**Response**
Status: 201 CREATED
```json
{
  "url": "http://localhost:8000/api/v1/events/6c402748-bb6f-406b-a3b7-a550617bcda2",
  "id": "6c402748-bb6f-406b-a3b7-a550617bcda2",
  "name": "Sample Event Name",
  "owner": "http://localhost:8000/api/v1/users/b81cad6d-0d56-4841-85ee-82c446da38b9",
  "created_at": "2020-04-26T21:48:14.541739+05:30",
  "modified_at": "2020-04-26T21:48:14.541782+05:30",
  "alert_date": "2020-12-03T09:30:00+05:30",
  "alert_interval": "00:02:00"
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
    "url": "http://localhost:8000/api/v1/events/6c402748-bb6f-406b-a3b7-a550617bcda2",
    "id": "6c402748-bb6f-406b-a3b7-a550617bcda2",
    "name": "Sample Event Name",
    "owner": "http://localhost:8000/api/v1/users/b81cad6d-0d56-4841-85ee-82c446da38b9",
    "created_at": "2020-04-26T21:48:14.541739+05:30",
    "modified_at": "2020-04-26T21:48:14.541782+05:30",
    "alert_date": "2020-12-03T09:30:00+05:30",
    "alert_interval": "00:02:00"
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
  "url": "http://localhost:8000/api/v1/events/6c402748-bb6f-406b-a3b7-a550617bcda2",
  "id": "6c402748-bb6f-406b-a3b7-a550617bcda2",
  "name": "Sample Event Name",
  "owner": "http://localhost:8000/api/v1/users/b81cad6d-0d56-4841-85ee-82c446da38b9",
  "created_at": "2020-04-26T21:48:14.541739+05:30",
  "modified_at": "2020-04-26T21:48:14.541782+05:30",
  "alert_date": "2020-12-03T09:30:00+05:30",
  "alert_interval": "00:02:00"
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
  "url": "http://localhost:8000/api/v1/events/6c402748-bb6f-406b-a3b7-a550617bcda2",
  "id": "6c402748-bb6f-406b-a3b7-a550617bcda2",
  "name": "Updated Event Name",
  "owner": "http://localhost:8000/api/v1/users/b81cad6d-0d56-4841-85ee-82c446da38b9",
  "created_at": "2020-04-26T21:48:14.541739+05:30",
  "modified_at": "2020-04-26T21:53:32.404905+05:30",
  "alert_date": "2020-12-03T09:30:00+05:30",
  "alert_interval": "00:02:00"
}
```

### Delete Event

```
DELETE /api/v1/events/:id (requires authentication)
```

Deletes the event corresponding to the given ID

**Response**
Status: 204 NO CONTENT

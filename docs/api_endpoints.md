# Authentication

## Login

```
POST /api/auth/login
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
    "auth_token": "AkJ0b.Ai0iJEv1EiLCJhbGciOiJIUeI1NiJ9.eyJ1c2VyX2F1dGhlbnRpY2F0eW9uX2lEIjoiMTcxOTU2YmEtNe3Ai00MDIxLWe5MDetYeViATgwemE0NjliIn0.loCdI3te2sICj8e5c6ip5TW_eFNn5RTj4HU-e2q0m"
}
```

## Register

```
POST /api/auth/register
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
    "auth_token": "eyJ0aXAiOiJqV1QiLCJhbGciOiJIUaI1NiJ9.ayJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lqIjoiMTcxOTU2YmQtNa3ai00MDIxLWa5MDatYaViaTgwamQ0NjliIn0.loCdI3tAa2sICj8a5c6ip5TW_aFnn5RTj4HU-D6zq3c"
}
```

## Change password

```
POST /api/auth/password_change (requires authentication)
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


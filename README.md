
# FIN_MANAGER_BACKEND

This is a simple backend application made in Django do handle user authentication alongside income and expenses transactions.

The projects runs on the default Django database 'SQlite' in order to facilitate for the user to run it locally.

#### Original language description
Decidi o tema desse mini projeto como algo da area financeira pois acredito ser de interesse da urbe.me. O projeto possui dois apps, um para usuários e um para transações. É bem simples, feito para adicionar as suas rendas pessoais e contas/gastos e ter uma melhor visão geral.


## Run Locally

Clone the project

```bash
  git clone git@github.com:FelipeBulhoes/fin_manager_backend.git
```

Go to the project directory

```bash
  cd fin_manager_backend
```

Create a virtual environment (Optional but recommended)

```bash
  python -m venv ./.venv  |  python3 -m venv ./.venv
```

Activate the virtual environment

```bash
  UNIX: source .venv/bin/activate
```
```bash
  WIN: .venv\Scripts\activate.bat  | .venv\Scripts\Activate.ps1
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Execute migrations

```bash
  python manage.py migrate  |  python3 manage.py migrate
```

Start the server

```bash
  python manage.py runserver  |  python3 manage.py runserver
```

The server is now running on http://localhost:8000


## API Reference

### Users

#### Create a new user

```http
  POST /users/create/
```
Body:
```json
{
  "username": "example",
  "email": "example@gmail.com",
  "password": "12345"
}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | None | Token not required |

###
#### Login

```http
  POST /users/login/
```
Body:
```json
{
  "email": "example@gmail.com",
  "password": "12345"
}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| None      | None | Token not required |

###
#### List

```http
  POST /users/list/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| None      | None | Token required |

### Transactions

#### Create a new transaction
```http
  POST /transactions/create/
```
Body:
```json
{
	"title": "Salary",
	"type": "income",
	"amount": 4000,
	"description": "My main source of income",
	"periodicity": "monthly"
}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | None | Token required |

###
#### List your transactions
```http
  GET /transactions/list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | None | Token required |

###
#### Edit one of your transactions
*You need be the owner of the desired transaction
```http
  PATCH /transactions/update/${id}/
```
Include in the body only the fields you want to update
```json
{
	"title": "Salary",
	"amount": 4000,
}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | Token required |

###
#### Delete one of your transactions
*You need be the owner of the desired transaction
```http
  DELETE /transactions/delete/${id}/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | Token required |

###
#### Get insights about your monthly and yearly balance
```http
  GET /transactions/balance/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | None | Token required |


## Running Tests

To run tests, run the following command

```bash
  python manage.py test  |  python3 manage.py test
```


# ✈️ Airline Management System

This is a Django-based API backend for managing airplanes, flights, and reservations in an airline system. The project is built with Django REST Framework and supports filtering, validation, and email notifications for reservations.

---

## 🚀 Features

- CRUD operations for Airplanes, Flights, and Reservations
- Airplane flight conflict validation
- Capacity check before accepting reservations
- Sends email confirmation when a reservation is made
- Filter/search support on list endpoints

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/airline-management.git
cd airline-management
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

---

## 📬 Email Setup

To enable reservation email notifications:

1. Use a Gmail account.
2. Enable 2FA and create an App Password.
3. Add the following to `backend/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

---

## 📡 API Endpoints

### Airplane API

| Method | Endpoint                        | Description                          |
|--------|----------------------------------|--------------------------------------|
| GET    | `/api/airplanes/`               | List all airplanes                   |
| GET    | `/api/airplanes/{id}/`          | Get airplane details                 |
| GET    | `/api/airplanes/{id}/flights/`  | List flights for an airplane         |
| POST   | `/api/airplanes/`               | Create a new airplane                |
| PATCH  | `/api/airplanes/{id}/`          | Update an airplane                   |
| DELETE | `/api/airplanes/{id}/`          | Delete an airplane                   |

---

### Flight API

| Method | Endpoint                         | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/api/flights/`                 | List all flights                     |
| GET    | `/api/flights/{id}/`            | Get flight details                   |
| GET    | `/api/flights/{id}/reservations/`| List reservations for a flight       |
| POST   | `/api/flights/`                 | Create a new flight                  |
| PATCH  | `/api/flights/{id}/`            | Update a flight                      |
| DELETE | `/api/flights/{id}/`            | Delete a flight                      |

---

### Reservation API

| Method | Endpoint                      | Description                          |
|--------|--------------------------------|--------------------------------------|
| GET    | `/api/reservations/`         | List all reservations                |
| GET    | `/api/reservations/{id}/`    | Get reservation details              |
| POST   | `/api/reservations/`         | Create a new reservation             |
| PATCH  | `/api/reservations/{id}/`    | Update a reservation                 |

---

## ✅ Tests

You can run tests using the exported POSTMAN collection.

https://api.postman.com/collections/32469330-63cd2750-503a-4218-ab8e-fd7683a5fd95

---

## Author

Ege SEFERTAŞ
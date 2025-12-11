
# 🚀 Nexus POS Backend – Week 3 (Products & Auth API)

A backend API developed using **FastAPI** and **PostgreSQL** to serve products by business type (Pharmacy/Grocery) and return a dummy JWT token for login purposes.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

---

## 📖 Overview

This backend project supports:

- 📦 GET `/products?module=Pharmacy` – Fetches product list by business type
- 🔐 POST `/login` – Dummy login returns a JWT token
- 🗃️ Products stored in PostgreSQL with categories (Antibiotics, Snacks, etc.)
- 💾 Dummy users handled via hardcoded credentials

---

## ✨ Features

- ✅ Fetch products by business type (Pharmacy / Grocery)
- ✅ Dummy login with hardcoded user
- ✅ JWT token response on successful login
- ✅ Error response for invalid login credentials
- ✅ Product fields: name, image, price, category, stock
- ✅ PostgreSQL integration using SQLAlchemy ORM
- ✅ Swagger UI auto-generated docs

---

## 📁 Folder Structure

```
nexus_backend_week3/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── product.py
│   │   └── auth.py
│   ├── models/
│   │   ├── product_model.py
│   │   └── user_model.py
│   ├── schemas/
│   │   ├── product_schema.py
│   │   └── user_schema.py
│   └── database.py
├── requirements.txt
├── api_docs.md
├── README.md
```

---

## 📦 Setup Instructions

1. Clone the repo or download the folder
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Access Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 API Testing

| Route                   | Method | Description                        |
|------------------------|--------|------------------------------------|
| `/products?module=`    | GET    | Get products for Pharmacy/Grocery |
| `/login`               | POST   | Login with dummy credentials       |

### 🔐 Login Payload

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### ✅ Successful Login Response

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

---

## 🧾 Postman Collection

You can import the provided `.postman_collection.json` file to test all routes.

---

## 👤 Author

**Syed Shujaa Hussain**

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:web.shujaa10@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shujaa396)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-shujaa-hussain-69113b289)

---

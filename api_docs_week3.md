
# 📦 Nexus POS – Week 3 API Documentation

## ✅ POST `/login`
Dummy login route

### 🔐 Request:
```json
{
  "username": "admin",
  "password": "admin123"
}
```

### ✅ Response:
```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

If credentials are invalid:
```json
{
  "detail": "Invalid credentials"
}
```

---

## ✅ GET `/products?module=`

### 🔍 Description:
Fetch products for either `"Pharmacy"` or `"Grocery"` module

### 🔗 Example URLs:
```
/products?module=Pharmacy
/products?module=Grocery
```

### ✅ Response:
```json
[
  {
    "id": 1,
    "name": "Amoxicillin 500mg",
    "image": "https://via.placeholder.com/150",
    "price": 12.5,
    "category": "Antibiotics",
    "stock": 100,
    "module": "Pharmacy"
  },
  ...
]
```

---

## 🧪 Testing Tools
- Swagger UI: http://127.0.0.1:8000/docs
- Postman/Insomnia: Optional

---

## 📌 Notes
- Token returned from `/login` should be stored in `localStorage`
- Authorization header format:
  ```
  Authorization: Bearer <access_token>
  ```

---

## 🛠️ Tech Stack
- FastAPI + PostgreSQL + JWT

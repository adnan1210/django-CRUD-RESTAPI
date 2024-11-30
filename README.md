# 🛠️ Django REST API - CRUD Operations  

This project is a **REST API** built with Django and Django REST Framework (DRF). It supports **CRUD (Create, Read, Update, Delete)** operations for managing `USER` 

---

## ✨ Features  

- **RESTful API Endpoints**: Easily interact with the API using standard HTTP methods.  
- **Django and DRF**: Built for scalability and maintainability.  
- **Input Validation**: Serializers ensure clean and structured data.  
- **Easy Integration**: Compatible with frontend frameworks and tools.  

---

## 🧰 Requirements  

- **Python**: 3.8+  
- **Django**: 4.x  
- **Django REST Framework**: Latest  

---

## 🏗️ Installation  

Follow these steps to set up the project locally:  

```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

---
## 🔗 API Endpoints  

| **Method** | **Endpoint**        | **Description**            |  
|------------|---------------------|----------------------------|  
| **GET**    | `/api/user/all`      | List all users          |  
| **POST**   | `/api/user/create`      | Create a new user        |  
| **GET**    | `/api/user/:id/`  | Retrieve an user by ID   |  
| **PUT**    | `/api/user/:id/`  | Update an user by ID     |  
| **DELETE** | `/api/user/:id/`  | Delete an user by ID     |  



---




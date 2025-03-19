### 📏 Event Management System (Backend)
🚀 **A powerful, API-driven event management system built with Django**  

![Django REST API](https://img.shields.io/badge/Django-REST%20Framework-green)  
![Python](https://img.shields.io/badge/Python-3.x-blue)  
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-orange)  
![JWT Auth](https://img.shields.io/badge/Auth-JWT-red)  

---

## **📌 Features**
✅ **Event Management** – Create, update, delete, and list events  
✅ **User Authentication** – Secure login & registration with JWT  
✅ **Event Registration** – Users can register for events  
✅ **Event Reminders** – Send automated email reminders before events *(optional: Celery + Redis)*  
✅ **Secure & Scalable** – Built with Django REST Framework + PostgreSQL  

---

## **📦 Tech Stack**
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL *(or SQLite for development)*  
- **Authentication:** JWT (JSON Web Tokens)  
- **Task Queue (Optional):** Celery + Redis for background tasks  
- **Deployment:** Gunicorn + Nginx *(for production setup)*  

---

## **🚀 Getting Started**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/event-management-system.git
cd event-management-system
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the Database**
```sh
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### **5️⃣ Run the Server**
```sh
python manage.py runserver
```
➡️ **API is now live at** `http://127.0.0.1:8000/`

---

## **🔗 API Endpoints**
| Endpoint             | Method | Description                      | Auth Required |
|----------------------|--------|----------------------------------|--------------|
| `/api/events/`       | GET    | List all events                 | ❌ No |
| `/api/events/`       | POST   | Create a new event              | ✅ Yes |
| `/api/events/<id>/`  | PUT    | Update an event                 | ✅ Yes |
| `/api/events/<id>/`  | DELETE | Delete an event                 | ✅ Yes |
| `/api/register/`     | POST   | User registration               | ❌ No |
| `/api/login/`        | POST   | User login (JWT token)          | ❌ No |

---

## **💌 Optional: Enable Event Reminders**
To enable email reminders, install **Celery & Redis**:  
```sh
pip install celery redis
```
Start Redis and Celery workers:
```sh
redis-server &
celery -A event_management worker --loglevel=info
```

---

## **🚀 Deployment Guide**
For production, set up **Gunicorn + Nginx**:  
```sh
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 event_management.wsgi
```

---

## **🛠 Future Enhancements**
✅ Add payment integration (MPesa, Stripe, PayPal)  
✅ Implement role-based access control (RBAC)  
✅ Build a front-end client (React/Vue) to interact with the API  

---

## **💡 Contributing**
Feel free to fork this repo, raise issues, or submit pull requests! 🚀  

---

## **📝 License**
MIT License © 2025 **Isaack Mogaka**  

---

🔥 **Happy Coding!**

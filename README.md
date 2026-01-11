# Smart-Rescue
# 🚑 Smart-Rescue

**Smart-Rescue** is a full-stack emergency response web application built with **Django and Python**, designed to help users quickly communicate with authorities during accidents or critical situations.

The platform allows users to send **text messages, images, and voice recordings** in real time, ensuring that critical information reaches the right responders without delay.

---

## ✨ Features

- 🆘 Emergency alert creation
- 📝 Real-time text communication
- 🎤 Voice message upload
- 🖼️ Image sharing for incident clarity
- ⚡ Fast and reliable request handling
- 🔐 Secure data management
- 📱 Responsive and user-friendly interface

---

## 🛠️ Tech Stack

**Backend**
- Python
- Django
- Django REST Framework

**Frontend**
- HTML5
- CSS3 / Bootstrap or Tailwind CSS
- JavaScript

**Database**
- PostgreSQL / SQLite
- Django ORM

**Other Tools**
- Git & GitHub
- RESTful APIs

---

## 📌 Project Purpose

Smart-Rescue addresses a real-world challenge:  
**enabling faster emergency response through efficient digital communication**.

By allowing users to instantly share accurate information, the application helps emergency services respond more effectively when every second counts.

---

## 🚀 How It Works

1. User initiates an emergency request
2. User submits text, image, or voice data
3. Django backend processes and stores the request
4. Emergency data is made available to responders in real time

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Christine-Abuqubou/MyProjects.git

# Navigate to project folder
cd Smart-Rescue

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

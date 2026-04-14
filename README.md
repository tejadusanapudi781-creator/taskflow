# TaskFlow — Full Stack Task Manager

A fully functional task management web application built with Django, featuring real user authentication, PostgreSQL database, and live deployment.

## 🚀 Live Demo
[Deployed on Render] — (Add your link here after deployment)

## ✨ Features
- **User Authentication** — Signup, Login, Logout with Django's built-in auth system
- **Task Management** — Create, Read, Update, Delete (CRUD) tasks
- **Priority Levels** — High, Medium, Low with color-coded indicators
- **Status Tracking** — Pending, In Progress, Completed
- **Due Dates** — Set and track task deadlines (overdue highlighting)
- **Search & Filter** — Filter by status, priority, or search keywords
- **Dashboard Stats** — Overview of all task counts by status
- **Responsive Design** — Works on mobile and desktop

## 🛠️ Tech Stack
- **Backend:** Python 3.x, Django 4.2
- **Database:** PostgreSQL (production) / SQLite (local dev)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Render.com
- **Static Files:** WhiteNoise

## 📦 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/tejadusanapudi781-creator/taskflow.git
cd taskflow

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Visit http://127.0.0.1:8000

## 🌐 Deployment (Render.com)
This project includes a `render.yaml` for one-click deployment on Render.com.

1. Push code to GitHub
2. Go to https://render.com → New → Blueprint
3. Connect your GitHub repo
4. Render auto-configures everything from `render.yaml`

## 📁 Project Structure
```
taskflow/
├── taskmanager/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/              # Main app
│   ├── models.py       # Task model
│   ├── views.py        # All views
│   ├── forms.py        # Django forms
│   ├── urls.py         # App URLs
│   └── admin.py
├── templates/          # HTML templates
│   ├── base.html
│   ├── registration/
│   └── tasks/
├── static/             # CSS & JS
├── requirements.txt
├── Procfile
└── render.yaml
```

## 👨‍💻 Author
Teja Dusanapudi — Full Stack Developer Internship Assignment
 
 

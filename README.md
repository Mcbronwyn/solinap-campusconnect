# CSIT327 - First Django Lab Challenge

**Student Name:** Karl Cyrus P. Solinap  
**Section:** CSIT327-G1  
**Project Name:** CampusConnect  
**Repository Name:** CSIT327-G1-Solinap-KarlCyrus-FirstDjango  

---

## Project Overview
**CampusConnect** is a web portal built with Django and styled with Bootstrap 5 loaded exclusively via CDN. The application includes a secure authentication lifecycle, feedback alerts powered by Django's messages framework, and a personalized profile management dashboard inspired by the classic 2013 Facebook desktop interface.

---

## Lab Challenge Implementations & Rubric Compliance

### 1. Profile Page (Class-Based `UpdateView`)
- **View Implementation:** Created `ProfileUpdateView` inheriting from `LoginRequiredMixin`, `SuccessMessageMixin`, and Django's generic `UpdateView`.
- **Security & Authorization:** Overrode `get_object(self)` to strictly return `self.request.user`. The profile endpoint does not accept primary keys or query arguments in the URL, preventing unauthorized users from accessing or editing other profiles (Insecure Direct Object Reference / IDOR protection).
- **Access Control:** Unauthenticated users attempting to navigate to `/accounts/profile/` are automatically redirected to `/accounts/login/`.

### 2. Feedback (Messages Framework)
- **Sign-Up Success Alert:** Integrated `SuccessMessageMixin` into `SignUpView` and `ProfileUpdateView`.
- **Bootstrap Alert Integration:** Configured `MESSAGE_TAGS` in `settings.py` to map Django message levels (`messages.ERROR` to `danger`, `messages.SUCCESS` to `success`, etc.).
- **Template Display:** Rendered messages inside `templates/base.html` using responsive, dismissible Bootstrap 5 alert components.

### 3. Bootstrap 5 CDN & UI Polish
- **CDN Loading:** Bootstrap 5.3.3 CSS and JavaScript bundle are loaded directly from the jsDelivr CDN inside `templates/base.html`. No local vendor files are used.
- **Form Controls:** Form widgets in `accounts/forms.py` dynamically inject the `form-control` class during initialization to eliminate unstyled HTML inputs.
- **2013 Facebook Theme:** Restyled navigation, forms, and the dashboard with the signature `#3b5998` top navbar, profile cover banner, square avatar box, and metadata feed layout.

---

## How to Run the Server on Your Local Machine

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/CSIT327-G1-Solinap-KarlCyrus-FirstDjango.git
cd CSIT327-G1-Solinap-KarlCyrus-FirstDjango
```

### 2. Set Up Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Migrations
Run `makemigrations` to register model changes (such as the custom user model), followed by `migrate` to apply them to the local SQLite database:
```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### 5. Create an Administrative Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🧭Application Routes

| Endpoint | Description | Access Level |
| :--- | :--- | :--- |
| `/` | Main dashboard / home page | Authenticated Users |
| `/accounts/signup/` | Student registration page with success alert dispatch | Public |
| `/accounts/login/` | Authentication form | Public |
| `/accounts/logout/` | Terminates user session | Authenticated Users |
| `/accounts/profile/` | Edit user profile (`UpdateView`) | Authenticated Users |
| `/admin/` | Django administrative interface | Superuser / Staff |

---

## Git Commit & Push Instructions

Before pushing, verify that your `.gitignore` file includes `venv/`, `__pycache__/`, and `db.sqlite3`.

Run the following commands in your project root terminal:

```bash
# Check modified files
git status

# Stage all project files
git add .

# Commit your changes
git commit -m "Complete Lab Challenge: Add Profile UpdateView, Bootstrap 5 CDN styling, and README"

# Ensure default branch is main
git branch -M main

# Push to your repository
git push -u origin main
```
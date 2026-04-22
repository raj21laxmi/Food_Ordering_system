<div align="center">

# Foodies Hub — Online Restaurant Ordering System

### A web-based food ordering platform built with Python and Django

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/raj21laxmi/Food_Ordering_system)

> Foodies Hub is an online restaurant ordering system that lets customers browse menus, add items to cart, and place orders — while restaurant admins manage everything from a central dashboard.

</div>

---

## Table of Contents

- [About the Project](#about-the-project)
- [Screenshots](#screenshots)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## About the Project

Foodies Hub is a full-stack web application that digitizes the restaurant ordering experience. Built on the Django web framework and powered by SQLite, it connects customers and restaurant management through a clean, intuitive interface.

The project was developed to demonstrate real-world web application development using Python and Django, covering user authentication, menu management, order handling, and an admin control panel.

---

## Screenshots


---
### Login Page

<img width="1515" height="725" alt="image" src="https://github.com/user-attachments/assets/8a4b6dcf-0ad5-40d7-af97-239caf66bec1" />


Secure login and registration forms for customer accounts.

---
### Menu Page


<img width="1704" height="760" alt="image" src="https://github.com/user-attachments/assets/a0d8a68d-0fb3-4d9e-99be-c2f6269abce1" />

Customers browse all available food items with photos, names, prices, and an Add to Cart button.
---

## Features

**Customer Side**

- User registration and login with secure authentication
- Browse the full food menu with item images, names, and prices
- Add items to cart and adjust quantities
- Place orders and confirm checkout
- View order history and current order status

**Restaurant / Admin Side**

- Centralized admin dashboard with key metrics
- Add, update, and remove menu items with photos
- View and process all incoming customer orders
- Update order status (Pending / Processing / Delivered)
- Manage registered customers

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Django Framework |
| Frontend | HTML5, CSS3, Bootstrap |
| Database | SQLite3 |
| Media Storage | Django Media Files (media/menu_images/) |
| Admin Panel | Django Built-in Admin |

**Language Breakdown**

```
Python   60%
HTML     40%
```

---

## Project Structure

```
Food_Ordering_system/
|
|-- manage.py                   # Django project management script
|-- db.sqlite3                  # SQLite database
|
|-- restaurant/                 # Core app — settings and configuration
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|
|-- orders/                     # Orders app — models, views, and URLs
|   |-- models.py               # Order and MenuItem models
|   |-- views.py                # Business logic
|   |-- urls.py                 # Route definitions
|   |-- admin.py                # Admin panel configuration
|   `-- templates/              # HTML templates
|
|-- media/
|   `-- menu_images/            # Uploaded food item images
|
`-- __pycache__/
```

---

## Getting Started

### Prerequisites

- Python 3.x — [Download](https://www.python.org/downloads/)
- pip (Python package manager)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/raj21laxmi/Food_Ordering_system.git
cd Food_Ordering_system
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install django
pip install Pillow
```

**4. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser for admin access**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

**7. Open in your browser**
```
http://127.0.0.1:8000/         Customer interface
http://127.0.0.1:8000/admin/   Admin panel
```

---

## Usage

**As a Customer**

1. Register a new account or log in with existing credentials
2. Browse the food menu and view item details
3. Add items to cart and review your selection
4. Confirm and place the order
5. Track order status from your order history

**As an Admin**

1. Go to `http://127.0.0.1:8000/admin/` and log in with superuser credentials
2. Add menu items with names, descriptions, prices, and images
3. View all incoming customer orders
4. Update order status as orders are prepared and delivered

---

## Roadmap

- [x] User authentication (register and login)
- [x] Menu browsing with images
- [x] Cart management and order placement
- [x] Django admin panel for restaurant management
- [ ] Real-time order status tracking
- [ ] Payment gateway integration (Razorpay / Stripe)
- [ ] Email confirmation on order placement
- [ ] Customer reviews and ratings
- [ ] Mobile-responsive UI improvements
- [ ] REST API using Django REST Framework

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## Author

**Raj Laxmi**
- GitHub: [raj21laxmi](https://github.com/raj21laxmi)
- Repository: [Food_Ordering_system](https://github.com/raj21laxmi/Food_Ordering_system)

---

<div align="center">

Foodies Hub — Order. Eat. Enjoy.

If you found this project helpful, please consider giving it a star on GitHub.

</div>

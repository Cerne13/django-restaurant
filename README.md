# Django Restaurant
### Little app to track cooks and dishes

---
[Project deployed to render.com](https://the-django-kitchen.onrender.com/)
---

Maybe will apply additional functionality later

### Important notes

**Superuser**:\
*nick*: admin\
*pass*: asd111poi


Pages listed in the sidebar are available to everyone. Ability to add/update/delete items - only
to logged in users.

---
## Features

* Authentication for users
* Dishes, dish types, cooks management (available only for logged in users)
* Powerful admin panel for advanced contents management


---

## Installation

Python 3 must be installed

- git clone https://github.com/Cerne13/django-restaurant
- in the project directory set up and activate virtual environment (depends on your system)
- usually it's:
- - python3 -m venv venv
- - source venv/bin/activate
- ===
- then:
- -  pip install -r requirements.txt
- - python manage.py migrate
- - python manage.py runserver

# TODO List for Django Portfolio Website

## 1. Project Setup
- [x] Create Django project structure using `django-admin startproject suresh_portfolio .`
- [x] Configure settings.py (static, templates, email, installed apps)
- [x] Create requirements.txt

## 2. Create Django Apps
- [x] Create home app: `python manage.py startapp home`
- [x] Create about app: `python manage.py startapp about`
- [x] Create services app: `python manage.py startapp services`
- [x] Create portfolio app: `python manage.py startapp portfolio`
- [x] Create blog app: `python manage.py startapp blog`
- [x] Create contact app: `python manage.py startapp contact`
- [x] Create testimonials app: `python manage.py startapp testimonials`
- [x] Create faq app: `python manage.py startapp faq`

## 3. Models and Database
- [x] Define models for each app (e.g., Service, Project, BlogPost, etc.)
- [x] Run migrations: `python manage.py makemigrations` and `python manage.py migrate`

## 4. Views and URLs
- [x] Implement views for each app
- [x] Configure URLs for each app and main project

## 5. Templates and Frontend
- [x] Create base templates (base.html with nav, footer, theme toggle)
- [x] Implement templates for home, about, services, portfolio, blog, contact, testimonials, faq pages
- [x] Add Tailwind CSS or Bootstrap
- [x] Add animations (AOS, preloader)
- [x] Add static files (CSS, JS, images)

## 6. Functionality
- [x] Contact form with email sending
- [x] Dark/Light mode toggle
- [x] Testimonials carousel
- [x] FAQ accordion
- [ ] Portfolio filters
- [ ] Blog pagination and search

## 7. SEO and Extras
- [ ] Add SEO meta tags
- [ ] Generate sitemap and robots.txt
- [ ] Custom 404 page
- [x] Admin setup and demo data

## 8. Testing and Deployment
- [ ] Test responsiveness and functionality
- [x] Create README with setup instructions
- [x] Add Procfile for deployment

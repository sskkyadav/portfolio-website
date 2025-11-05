# Suresh Kumar Yadav - Django Portfolio Website

A modern, responsive portfolio website for Suresh Kumar Yadav, an IT Trainer & Web Developer, built with Django, Tailwind CSS, and AOS animations.

## 🚀 Features

- **Modern Design**: Clean, professional design with dark/light mode toggle
- **Responsive**: Mobile-first design that works on all devices
- **Animated**: Smooth animations using AOS (Animate On Scroll)
- **SEO Optimized**: Meta tags, sitemap, and robots.txt included
- **Contact Form**: Working contact form with email integration
- **Admin Panel**: Django admin for easy content management
- **Portfolio Gallery**: Filterable portfolio with categories
- **Blog System**: Full blog with pagination and search
- **Testimonials**: Client and student testimonials carousel
- **FAQ Section**: Accordion-style frequently asked questions
- **WhatsApp Integration**: Live chat button
- **Resume Download**: Direct download link for CV

## 🛠️ Tech Stack

- **Backend**: Python Django 5.2
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (default)
- **Animations**: AOS (Animate On Scroll)
- **Icons**: Font Awesome
- **Deployment**: Ready for Render/PythonAnywhere/Railway

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd suresh_portfolio
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
suresh_portfolio/
├── manage.py
├── suresh_portfolio/          # Main settings folder
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/                      # Home app
├── about/                     # About page
├── services/                  # Services page
├── portfolio/                 # Portfolio gallery
├── blog/                      # Blog system
├── contact/                   # Contact form
├── testimonials/              # Testimonials
├── faq/                       # FAQ section
├── static/                    # Static files (CSS, JS, Images)
├── templates/                 # HTML templates
├── media/                     # User uploaded files
├── staticfiles/               # Collected static files
├── db.sqlite3                 # Database
└── requirements.txt
```

## 🔧 Configuration

### Email Settings
Update `suresh_portfolio/settings.py` with your email credentials:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Admin Access
- URL: `http://127.0.0.1:8000/admin/`
- Use the superuser credentials created during setup

## 📝 Content Management

### Adding Portfolio Projects
1. Go to Django Admin
2. Navigate to Portfolio > Projects
3. Add new project with title, description, image, category, and tags

### Managing Blog Posts
1. Go to Django Admin
2. Navigate to Blog > Posts
3. Create new blog posts with rich content

### Testimonials
1. Go to Django Admin
2. Navigate to Testimonials > Testimonials
3. Add client/student feedback

## 🎨 Customization

### Colors and Styling
- Edit `static/css/custom.css` for custom styles
- Modify Tailwind config in base template for theme colors

### Adding New Pages
1. Create new Django app: `python manage.py startapp newpage`
2. Add to `INSTALLED_APPS` in settings.py
3. Create models, views, templates, and URLs
4. Update navigation in `templates/base.html`

## 🚀 Deployment

### Environment Variables
Create a `.env` file for production settings:

```
DEBUG=False
SECRET_KEY=your-production-secret-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
ALLOWED_HOSTS=your-domain.com
```

### Static Files for Production
Make sure `DEBUG=False` and run:
```bash
python manage.py collectstatic
```

### Deployment Platforms
- **Render**: Add `build.sh` and `render.yaml`
- **PythonAnywhere**: Upload files and configure WSGI
- **Railway**: Connect GitHub repo for automatic deployment

## 📊 SEO Features

- Meta tags for all pages
- Open Graph tags for social sharing
- Twitter Card support
- Sitemap generation
- Robots.txt file

## 🔒 Security

- CSRF protection enabled
- Secure password hashing
- XSS protection
- Clickjacking protection
- SSL/HTTPS ready

## 📱 Responsive Design

- Mobile-first approach
- Tablet and desktop optimized
- Touch-friendly interactions
- Fast loading on all devices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support or questions:
- Email: suresh@example.com
- WhatsApp: +91-9352471227
- LinkedIn: [Suresh Kumar Yadav](https://www.linkedin.com/in/suresh-kumar-yadav-5b61092a6)

## 🙏 Acknowledgments

- Django Framework
- Tailwind CSS
- AOS Animation Library
- Font Awesome Icons
- Unsplash/Pexels for images

---

**Built with ❤️ by Suresh Kumar Yadav**

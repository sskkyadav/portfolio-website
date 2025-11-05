// Main JavaScript file for Suresh Portfolio

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }

    // Preloader
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                preloader.classList.add('fade-out');
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 500);
            }, 1000);
        });
    }

    // Dark/Light mode toggle
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;

    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    html.classList.toggle('dark', currentTheme === 'dark');

    if (themeToggle) {
        // Update toggle button icon
        updateThemeIcon(currentTheme);

        themeToggle.addEventListener('click', function() {
            const isDark = html.classList.toggle('dark');
            const theme = isDark ? 'dark' : 'light';
            localStorage.setItem('theme', theme);
            updateThemeIcon(theme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeToggle) return;

        const icon = themeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
            themeToggle.setAttribute('aria-label', 'Switch to light mode');
        } else {
            icon.className = 'fas fa-moon';
            themeToggle.setAttribute('aria-label', 'Switch to dark mode');
        }
    }

    // Mobile menu toggle
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            const isOpen = !mobileMenu.classList.contains('hidden');
            mobileMenuToggle.setAttribute('aria-expanded', isOpen);

            // Update hamburger icon
            const icon = mobileMenuToggle.querySelector('i');
            icon.className = isOpen ? 'fas fa-times' : 'fas fa-bars';
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenuToggle.contains(event.target) && !mobileMenu.contains(event.target)) {
                mobileMenu.classList.add('hidden');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
                const icon = mobileMenuToggle.querySelector('i');
                icon.className = 'fas fa-bars';
            }
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Portfolio filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter items
            portfolioItems.forEach(item => {
                if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'scale(1)';
                    }, 100);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // FAQ accordion
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const answer = this.nextElementSibling;
            const icon = this.querySelector('.faq-icon');

            // Close other answers
            document.querySelectorAll('.faq-answer').forEach(ans => {
                if (ans !== answer) {
                    ans.classList.remove('show');
                    ans.previousElementSibling.querySelector('.faq-icon').classList.remove('rotate-180');
                }
            });

            // Toggle current answer
            answer.classList.toggle('show');
            if (icon) {
                icon.classList.toggle('rotate-180');
            }
        });
    });

    // Progress bars animation
    const progressBars = document.querySelectorAll('.progress-bar');

    function animateProgressBars() {
        progressBars.forEach(bar => {
            const width = bar.getAttribute('data-width');
            if (width) {
                bar.style.setProperty('--progress-width', width);
                bar.classList.add('animate');
            }
        });
    }

    // Trigger progress bar animation when skills section is in view
    const skillsSection = document.querySelector('#skills');
    if (skillsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateProgressBars();
                    observer.unobserve(entry.target);
                }
            });
        });
        observer.observe(skillsSection);
    }

    // Testimonial carousel
    const testimonialSlides = document.querySelectorAll('.testimonial-slide');
    const testimonialIndicators = document.querySelectorAll('.testimonial-indicator');
    let currentTestimonial = 0;

    function showTestimonial(index) {
        testimonialSlides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        testimonialIndicators.forEach((indicator, i) => {
            indicator.classList.toggle('active', i === index);
        });
        currentTestimonial = index;
    }

    if (testimonialIndicators.length > 0) {
        testimonialIndicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => showTestimonial(index));
        });

        // Auto-rotate testimonials
        setInterval(() => {
            currentTestimonial = (currentTestimonial + 1) % testimonialSlides.length;
            showTestimonial(currentTestimonial);
        }, 5000);
    }

    // Contact form validation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Basic validation
            const name = document.getElementById('id_name').value.trim();
            const email = document.getElementById('id_email').value.trim();
            const message = document.getElementById('id_message').value.trim();

            if (!name || !email || !message) {
                alert('Please fill in all required fields.');
                return;
            }

            if (!isValidEmail(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            // Submit form (you would typically send this via AJAX)
            alert('Thank you for your message! I will get back to you soon.');
            contactForm.reset();
        });
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Newsletter signup
    const newsletterForms = document.querySelectorAll('form[action*="newsletter"]');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = form.querySelector('input[type="email"]').value.trim();

            if (!email) {
                alert('Please enter your email address.');
                return;
            }

            if (!isValidEmail(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            alert('Thank you for subscribing! You will receive updates at ' + email);
            form.reset();
        });
    });

    // Back to top button
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.remove('hidden');
            } else {
                backToTopBtn.classList.add('hidden');
            }
        });

        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Lazy loading for images
    const lazyImages = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for browsers without IntersectionObserver
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
        });
    }

    // Typing effect for hero text
    const typingElement = document.querySelector('.typing-effect');
    if (typingElement) {
        const text = typingElement.textContent;
        typingElement.textContent = '';
        let i = 0;

        function typeWriter() {
            if (i < text.length) {
                typingElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }

        setTimeout(typeWriter, 1000);
    }

    // Parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            heroSection.style.transform = `translateY(${rate}px)`;
        });
    }

    // Modal functionality
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const modals = document.querySelectorAll('.modal');

    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
        });
    });

    modals.forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        });

        const closeBtn = modal.querySelector('.modal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            });
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        // Escape key closes modals
        if (e.key === 'Escape') {
            modals.forEach(modal => {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            });
        }
    });

    // Service worker registration (for PWA features)
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js')
                .then(function(registration) {
                    console.log('ServiceWorker registration successful');
                })
                .catch(function(err) {
                    console.log('ServiceWorker registration failed: ', err);
                });
        });
    }

    // Performance monitoring
    if ('performance' in window && 'PerformanceObserver' in window) {
        // Monitor Largest Contentful Paint (LCP)
        try {
            const observer = new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (entry.entryType === 'largest-contentful-paint') {
                        console.log('LCP:', entry.startTime);
                    }
                }
            });
            observer.observe({ entryTypes: ['largest-contentful-paint'] });
        } catch (e) {
            console.log('LCP observation not supported');
        }
    }

    // Error handling
    window.addEventListener('error', function(e) {
        console.error('JavaScript error:', e.error);
        // You could send this to an error reporting service
    });

    window.addEventListener('unhandledrejection', function(e) {
        console.error('Unhandled promise rejection:', e.reason);
        // You could send this to an error reporting service
    });
});

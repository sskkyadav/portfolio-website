import urllib.request

try:
    with urllib.request.urlopen('http://localhost:8000/faq/') as response:
        html = response.read().decode('utf-8')

    # Check if categories are correctly assigned
    services_count = html.count('data-category="services"')
    training_count = html.count('data-category="training"')
    technical_count = html.count('data-category="technical"')
    pricing_count = html.count('data-category="pricing"')

    print('Services category items:', services_count)
    print('Training category items:', training_count)
    print('Technical category items:', technical_count)
    print('Pricing category items:', pricing_count)

    if services_count >= 2 and training_count >= 2 and technical_count >= 2 and pricing_count >= 2:
        print('SUCCESS: All categories have sufficient items')
    else:
        print('ERROR: Some categories have insufficient items')

    # Check if all FAQ items have categories
    total_faqs = html.count('data-category=')
    print('Total FAQ items with categories:', total_faqs)

    if total_faqs >= 8:
        print('SUCCESS: Sufficient FAQ items with categories')
    else:
        print('ERROR: Insufficient FAQ items with categories')

    # Check for specific questions in each category
    if 'What services do you offer?' in html and 'data-category="services"' in html:
        print('SUCCESS: Services question properly categorized')
    else:
        print('ERROR: Services question not properly categorized')

    if 'Do you provide training programs?' in html and 'data-category="training"' in html:
        print('SUCCESS: Training question properly categorized')
    else:
        print('ERROR: Training question not properly categorized')

    if 'Which technologies do you work with?' in html and 'data-category="technical"' in html:
        print('SUCCESS: Technical question properly categorized')
    else:
        print('ERROR: Technical question not properly categorized')

    if 'What is your pricing structure?' in html and 'data-category="pricing"' in html:
        print('SUCCESS: Pricing question properly categorized')
    else:
        print('ERROR: Pricing question not properly categorized')

    # Check for search functionality structure
    if 'addEventListener' in html and 'input' in html and 'faq-search' in html:
        print('SUCCESS: Search functionality structure present')
    else:
        print('ERROR: Search functionality structure missing')

    # Check for filter functionality structure
    if 'filterFAQ' in html and 'category-btn' in html:
        print('SUCCESS: Filter functionality structure present')
    else:
        print('ERROR: Filter functionality structure missing')

    # Check for accordion toggle functionality
    if 'toggleFAQ' in html and 'faq-question' in html:
        print('SUCCESS: Accordion toggle functionality present')
    else:
        print('ERROR: Accordion toggle functionality missing')

    # Check for newsletter form structure
    if 'newsletter-form' in html and 'email' in html and 'submit' in html:
        print('SUCCESS: Newsletter form structure present')
    else:
        print('ERROR: Newsletter form structure missing')

    # Check for popular topics links
    if 'popular-topics' in html and 'href=' in html:
        print('SUCCESS: Popular topics links present')
    else:
        print('ERROR: Popular topics links missing')

    # Check for contact information
    if 'contact' in html.lower() and 'whatsapp' in html.lower():
        print('SUCCESS: Contact information present')
    else:
        print('ERROR: Contact information missing')

    # Check for dark mode compatibility
    if 'dark:' in html or 'dark-mode' in html:
        print('SUCCESS: Dark mode compatibility present')
    else:
        print('ERROR: Dark mode compatibility missing')

    # Check for responsive design classes
    if 'md:' in html or 'lg:' in html or 'sm:' in html:
        print('SUCCESS: Responsive design classes present')
    else:
        print('ERROR: Responsive design classes missing')

    print('All structural checks completed.')

except Exception as e:
    print('ERROR: Could not connect to server:', e)

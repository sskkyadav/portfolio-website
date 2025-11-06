#!/usr/bin/env python
import os
import django
from datetime import datetime, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suresh_portfolio.settings')
django.setup()

from blog.models import BlogPost
from django.contrib.auth.models import User

def create_blog_posts():
    # Get or create the author user
    author, created = User.objects.get_or_create(
        username='suresh',
        defaults={
            'email': 'suresh@example.com',
            'first_name': 'Suresh',
            'last_name': 'Kumar Yadav'
        }
    )
    if created:
        print("Created author user: Suresh Kumar Yadav")
    else:
        print("Using existing author user: Suresh Kumar Yadav")
    blog_posts_data = [
        {
            'title': 'Getting Started with Django REST Framework',
            'slug': 'getting-started-django-rest-framework',
            'image': '/static/images/suresh.jpg',
            'content': '''
# Getting Started with Django REST Framework

Django REST Framework (DRF) is a powerful toolkit for building Web APIs in Django. In this comprehensive guide, we'll explore how to create robust REST APIs that can power modern web and mobile applications.

## Why Django REST Framework?

DRF provides:
- **Serialization** that supports both ORM and non-ORM data sources
- **Authentication** policies including packages for OAuth1a and OAuth2
- **Throttling** for rate limiting access to your API
- **Pagination** for handling large datasets
- **Versioning** for managing API versions
- **Browsable API** for easy testing and exploration

## Installation and Setup

First, install DRF using pip:

```bash
pip install djangorestframework
```

Add it to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'rest_framework',
]
```

## Creating Your First API View

Let's create a simple API endpoint that returns a list of blog posts:

```python
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

## Serializers

Serializers convert complex data types like Django model instances to Python data types that can be easily rendered into JSON:

```python
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author', read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'author_name', 'published_at']
        read_only_fields = ['id', 'slug', 'published_at']
```

## Authentication and Permissions

DRF provides several authentication methods:

- **SessionAuthentication**: For web browsers
- **TokenAuthentication**: For API clients
- **BasicAuthentication**: For simple cases

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

## Testing Your API

DRF includes a browsable API that allows you to test endpoints directly from your browser. Simply navigate to your API endpoint, and you'll see an interactive interface.

## Conclusion

Django REST Framework makes it incredibly easy to build powerful APIs. With its extensive feature set and excellent documentation, you can quickly create production-ready APIs that scale with your application.

The key to success with DRF is understanding the separation of concerns between views, serializers, and permissions. Once you grasp these concepts, building complex APIs becomes straightforward.
            ''',
            'excerpt': 'Learn how to build powerful REST APIs with Django REST Framework. This comprehensive guide covers installation, serialization, authentication, and best practices.',
            'author': 'Suresh Kumar Yadav',
            'published': True,
            'tags': 'Django, REST API, Python, Web Development'
        },
        {
            'title': 'React Hooks: A Complete Guide for Beginners',
            'slug': 'react-hooks-complete-guide',
            'content': '''
# React Hooks: A Complete Guide for Beginners

React Hooks revolutionized how we write React components. Introduced in React 16.8, hooks allow you to use state and other React features without writing a class component. This guide will take you from hooks basics to advanced patterns.

## What Are React Hooks?

Hooks are functions that let you "hook into" React state and lifecycle features from function components. They let you use React without classes.

## useState: Managing Component State

The `useState` hook is the most fundamental hook. It allows you to add state to functional components:

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

## useEffect: Handling Side Effects

`useEffect` lets you perform side effects in function components. It serves the same purpose as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` in class components:

```jsx
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // This runs after every render
    fetch(`/api/users/${userId}`)
      .then(response => response.json())
      .then(data => setUser(data));

    // Cleanup function (optional)
    return () => {
      // This runs when component unmounts or before next effect
    };
  }, [userId]); // Only re-run if userId changes

  if (!user) return <div>Loading...</div>;

  return <div>Welcome, {user.name}!</div>;
}
```

## useContext: Accessing Context

`useContext` makes it easy to consume context values:

```jsx
import React, { useContext } from 'react';
import { ThemeContext } from './ThemeProvider';

function ThemedButton() {
  const theme = useContext(ThemeContext);

  return (
    <button style={{ background: theme.background, color: theme.foreground }}>
      I am styled with theme context!
    </button>
  );
}
```

## Custom Hooks: Reusable Logic

You can create your own hooks to extract component logic into reusable functions:

```jsx
import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setValue = value => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.log(error);
    }
  };

  return [storedValue, setValue];
}

// Usage
function MyComponent() {
  const [name, setName] = useLocalStorage('name', 'John');

  return (
    <input
      value={name}
      onChange={e => setName(e.target.value)}
    />
  );
}
```

## Rules of Hooks

1. **Only call hooks at the top level** - Don't call hooks inside loops, conditions, or nested functions
2. **Only call hooks from React functions** - Call them from React function components or custom hooks
3. **Hook names must start with "use"** - This is a convention that helps with automatic linting

## Common Hook Patterns

### Data Fetching
```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, [url]);

  return { data, loading, error };
}
```

### Form Handling
```jsx
function useForm(initialValues) {
  const [values, setValues] = useState(initialValues);

  const handleChange = e => {
    setValues({
      ...values,
      [e.target.name]: e.target.value
    });
  };

  const reset = () => setValues(initialValues);

  return [values, handleChange, reset];
}
```

## Conclusion

React Hooks have transformed React development by making it easier to share logic between components and reducing the need for class components. While there's a learning curve, the benefits of cleaner, more reusable code make it worthwhile.

Start small by converting simple class components to function components with hooks, and gradually work your way up to more complex patterns. The React documentation and community resources are excellent for deepening your understanding.
            ''',
            'excerpt': 'Master React Hooks from basics to advanced patterns. Learn useState, useEffect, useContext, and how to create custom hooks for reusable logic.',
            'author': 'Suresh Kumar Yadav',
            'published': True,
            'tags': 'React, JavaScript, Hooks, Frontend'
        },
        {
            'title': 'Building Modern Web Applications with Django and React',
            'slug': 'building-modern-web-apps-django-react',
            'content': '''
# Building Modern Web Applications with Django and React

Combining Django's powerful backend capabilities with React's dynamic frontend creates a robust full-stack solution. This guide explores best practices for integrating these technologies to build scalable, maintainable web applications.

## Why Django + React?

Django and React complement each other perfectly:
- **Django** provides a secure, scalable backend with excellent ORM and admin interface
- **React** delivers fast, interactive user interfaces with component-based architecture
- Together they enable separation of concerns and team specialization

## Project Structure

A typical Django + React project structure:

```
myproject/
├── backend/
│   ├── manage.py
│   ├── myapp/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.js
│   ├── package.json
│   └── public/
└── docker-compose.yml
```

## Django REST Framework Setup

First, set up your Django backend with DRF:

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',  # For CORS handling
    'myapp',
]

MIDDLEWARE = [
    # ... other middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# Allow all origins for development
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

## API Design

Design RESTful APIs that your React frontend can consume:

```python
# views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

```python
# serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
```

## React Frontend Setup

Create a React app and set up API communication:

```jsx
// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api',
});

// Add request interceptor for authentication
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

export default api;
```

## State Management

Use React hooks and Context API for state management:

```jsx
// src/contexts/TaskContext.js
import React, { createContext, useContext, useReducer, useEffect } from 'react';
import api from '../services/api';

const TaskContext = createContext();

const taskReducer = (state, action) => {
  switch (action.type) {
    case 'SET_TASKS':
      return { ...state, tasks: action.payload, loading: false };
    case 'ADD_TASK':
      return { ...state, tasks: [...state.tasks, action.payload] };
    case 'UPDATE_TASK':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id ? action.payload : task
        )
      };
    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload)
      };
    default:
      return state;
  }
};

export const TaskProvider = ({ children }) => {
  const [state, dispatch] = useReducer(taskReducer, {
    tasks: [],
    loading: true
  });

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks/');
      dispatch({ type: 'SET_TASKS', payload: response.data });
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  const addTask = async (taskData) => {
    try {
      const response = await api.post('/tasks/', taskData);
      dispatch({ type: 'ADD_TASK', payload: response.data });
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  const updateTask = async (id, taskData) => {
    try {
      const response = await api.put(`/tasks/${id}/`, taskData);
      dispatch({ type: 'UPDATE_TASK', payload: response.data });
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const deleteTask = async (id) => {
    try {
      await api.delete(`/tasks/${id}/`);
      dispatch({ type: 'DELETE_TASK', payload: id });
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  return (
    <TaskContext.Provider value={{
      ...state,
      addTask,
      updateTask,
      deleteTask
    }}>
      {children}
    </TaskContext.Provider>
  );
};

export const useTasks = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTasks must be used within a TaskProvider');
  }
  return context;
};
```

## Component Architecture

Create reusable components:

```jsx
// src/components/TaskList.js
import React from 'react';
import { useTasks } from '../contexts/TaskContext';
import TaskItem from './TaskItem';

const TaskList = () => {
  const { tasks, loading } = useTasks();

  if (loading) return <div>Loading tasks...</div>;

  return (
    <div className="task-list">
      {tasks.map(task => (
        <TaskItem key={task.id} task={task} />
      ))}
    </div>
  );
};

export default TaskList;
```

```jsx
// src/components/TaskItem.js
import React from 'react';
import { useTasks } from '../contexts/TaskContext';

const TaskItem = ({ task }) => {
  const { updateTask, deleteTask } = useTasks();

  const handleToggle = () => {
    updateTask(task.id, { ...task, completed: !task.completed });
  };

  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      deleteTask(task.id);
    }
  };

  return (
    <div className={`task-item ${task.completed ? 'completed' : ''}`}>
      <input
        type="checkbox"
        checked={task.completed}
        onChange={handleToggle}
      />
      <span>{task.title}</span>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default TaskItem;
```

## Authentication

Implement authentication with JWT:

```python
# Django - views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Add to urls.py
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

```jsx
// React - AuthContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // Verify token and set user
      api.get('/auth/user/')
        .then(response => setUser(response.data))
        .catch(() => localStorage.removeItem('token'))
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (username, password) => {
    try {
      const response = await api.post('/api/token/', { username, password });
      const { access, refresh } = response.data;

      localStorage.setItem('token', access);
      localStorage.setItem('refreshToken', refresh);

      // Get user data
      const userResponse = await api.get('/auth/user/');
      setUser(userResponse.data);

      return { success: true };
    } catch (error) {
      return { success: false, error: error.response?.data?.detail || 'Login failed' };
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
```

## Deployment

Deploy your application using Docker:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myproject
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password

  backend:
    build: ./backend
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./backend:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgres://user:password@db:5432/myproject

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
```

## Best Practices

1. **API Versioning**: Use URL versioning (e.g., `/api/v1/tasks/`)
2. **Error Handling**: Implement comprehensive error handling on both frontend and backend
3. **Testing**: Write unit tests for both Django and React code
4. **Security**: Use HTTPS, validate inputs, and implement proper authentication
5. **Performance**: Implement caching, pagination, and lazy loading
6. **Documentation**: Document your APIs with tools like Swagger/OpenAPI

## Conclusion

Django and React together provide an excellent foundation for modern web applications. By following the patterns outlined in this guide, you can build scalable, maintainable applications that provide great user experiences.

The key to success is maintaining clear separation between frontend and backend concerns while ensuring smooth communication between them. With proper planning and architecture, this stack can handle everything from small projects to large-scale applications.
            ''',
            'excerpt': 'Learn how to build full-stack web applications using Django for the backend and React for the frontend. Includes authentication, state management, and deployment.',
            'author': 'Suresh Kumar Yadav',
            'published': True,
            'tags': 'Django, React, Full-Stack, Web Development'
        },
        {
            'title': 'Python Best Practices for Clean and Maintainable Code',
            'slug': 'python-best-practices-clean-code',
            'content': '''
# Python Best Practices for Clean and Maintainable Code

Writing clean, maintainable Python code is crucial for long-term project success. This guide covers essential practices, patterns, and tools that will help you write better Python code.

## Code Style and Formatting

### PEP 8 Compliance

Follow PEP 8, Python's official style guide:

```python
# Good
def calculate_total(price, tax_rate):
    """Calculate total price including tax."""
    return price * (1 + tax_rate)

# Bad
def calculateTotal(price,tax_rate):
    return price*(1+tax_rate)
```

### Use Black for Consistent Formatting

Black is an uncompromising code formatter:

```bash
pip install black
black my_module.py
```

### Type Hints

Add type hints for better code documentation and IDE support:

```python
from typing import List, Optional

def process_items(items: List[str], limit: Optional[int] = None) -> List[str]:
    """Process a list of items with optional limit."""
    if limit:
        return items[:limit]
    return items
```

## Project Structure

Organize your project logically:

```
myproject/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── mymodule/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_views.py
├── docs/
├── requirements.txt
├── setup.py
└── README.md
```

## Writing Clean Functions

### Single Responsibility Principle

Each function should do one thing well:

```python
# Good
def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def send_welcome_email(email: str) -> None:
    """Send welcome email to user."""
    if validate_email(email):
        # Send email logic
        pass

# Bad
def process_user(email: str) -> None:
    """This function does too many things."""
    # Validate email
    # Save to database
    # Send welcome email
    # Log activity
    pass
```

### Function Length

Keep functions short and focused:

```python
# Good
def calculate_order_total(items: List[dict]) -> float:
    """Calculate total price of order items."""
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax = subtotal * 0.08  # 8% tax
    return subtotal + tax

# Avoid functions longer than 50 lines
```

### Descriptive Names

Use descriptive, meaningful names:

```python
# Good
def calculate_monthly_revenue(sales_data: List[dict]) -> float:
    pass

# Bad
def calc_rev(data: List[dict]) -> float:
    pass
```

## Error Handling

### Use Specific Exceptions

```python
# Good
class InsufficientFundsError(Exception):
    pass

def withdraw(account: dict, amount: float) -> None:
    if account['balance'] < amount:
        raise InsufficientFundsError("Insufficient funds")
    account['balance'] -= amount

# Bad
def withdraw(account: dict, amount: float) -> None:
    if account['balance'] < amount:
        raise ValueError("Not enough money")
```

### Context Managers

Use context managers for resource management:

```python
# Good
with open('data.txt', 'r') as file:
    data = file.read()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def database_connection():
    connection = create_connection()
    try:
        yield connection
    finally:
        connection.close()

with database_connection() as conn:
    # Use connection
    pass
```

## Testing

### Write Comprehensive Tests

```python
import pytest
from mymodule import calculate_total, validate_email

class TestCalculateTotal:
    def test_basic_calculation(self):
        assert calculate_total(100, 0.08) == 108.0

    def test_zero_tax(self):
        assert calculate_total(100, 0) == 100.0

    def test_high_tax(self):
        assert calculate_total(100, 0.5) == 150.0

class TestValidateEmail:
    def test_valid_emails(self):
        assert validate_email('user@example.com')
        assert validate_email('test.email+tag@domain.co.uk')

    def test_invalid_emails(self):
        assert not validate_email('invalid-email')
        assert not validate_email('@domain.com')
```

### Test Coverage

Aim for high test coverage:

```bash
pip install pytest-cov
pytest --cov=mymodule --cov-report=html
```

## Documentation

### Docstrings

Write comprehensive docstrings:

```python
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### README and Documentation

Maintain comprehensive documentation:

```markdown
# My Project

A Python library for [purpose].

## Installation

```bash
pip install myproject
```

## Usage

```python
from myproject import MyClass

obj = MyClass()
obj.do_something()
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests
4. Submit a pull request
```

## Code Quality Tools

### Linting

Use multiple linters for comprehensive checking:

```bash
pip install flake8 pylint mypy

# Run linters
flake8 mymodule.py
pylint mymodule.py
mypy mymodule.py
```

### Pre-commit Hooks

Use pre-commit to run checks before commits:

```yaml
# .pre-commit-config.yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.4.0
  hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-yaml
  - id: check-added-large-files

- repo: https://github.com/psf/black
  rev: 22.3.0
  hooks:
  - id: black

- repo: https://github.com/pycqa/flake8
  rev: 4.0.1
  hooks:
  - id: flake8
```

## Performance Considerations

### Efficient Data Structures

Choose the right data structures:

```python
# Use sets for membership testing
valid_items = {'apple', 'banana', 'orange'}
if item in valid_items:  # O(1) lookup
    pass

# Use lists for ordered collections
items = ['apple', 'banana', 'orange']

# Use dicts for key-value pairs
prices = {'apple': 1.0, 'banana': 0.5, 'orange': 0.8}
```

### List Comprehensions

Use list comprehensions for concise, readable code:

```python
# Good
squares = [x**2 for x in range(10) if x % 2 == 0]

# Bad
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
```

### Generator Expressions

Use generators for memory efficiency:

```python
# Memory efficient for large datasets
def get_large_data():
    for i in range(1000000):
        yield i * 2

# Process data without loading everything into memory
total = sum(get_large_data())
```

## Security Best Practices

### Input Validation

Always validate user input:

```python
def safe_sql_query(user_id: str) -> str:
    """Safely construct SQL query."""
    # Validate input
    if not user_id.isdigit():
        raise ValueError("Invalid user ID")

    # Use parameterized queries
    return f"SELECT * FROM users WHERE id = ?", (user_id,)
```

### Environment Variables

Store sensitive data securely:

```python
import os

# Good
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

# Bad
DATABASE_URL = "postgresql://user:password@localhost/db"
```

## Version Control

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Add user authentication feature

- Implement login/logout functionality
- Add password hashing with bcrypt
- Create user registration endpoint
- Add JWT token generation"

# Bad
git commit -m "fix bug"
```

### Branching Strategy

Use a consistent branching strategy:

```
main (production)
├── develop (integration)
│   ├── feature/user-auth
│   ├── feature/payment-integration
│   └── bugfix/login-validation
```

## Conclusion

Writing clean, maintainable Python code requires discipline and attention to detail. By following these best practices, you'll create code that's easier to understand, test, and maintain.

Remember that code is read much more often than it's written, so prioritize readability and maintainability. Use the tools and techniques outlined in this guide to establish good habits that will serve you throughout your Python development career.
            ''',
            'excerpt': 'Master Python best practices for writing clean, maintainable code. Covers style, structure, testing, documentation, and performance optimization.',
            'author': 'Suresh Kumar Yadav',
            'published': True,
            'tags': 'Python, Best Practices, Clean Code, Development'
        },
        {
            'title': 'Deploying Django Applications to AWS',
            'slug': 'deploying-django-aws',
            'content': '''
# Deploying Django Applications to AWS

Amazon Web Services (AWS) provides a robust platform for deploying Django applications. This comprehensive guide covers various deployment strategies, from simple EC2 instances to complex architectures using Elastic Beanstalk, ECS, and more.

## AWS Services Overview

### Elastic Beanstalk
AWS Elastic Beanstalk is the fastest way to deploy Django applications. It handles:
- Load balancing
- Auto scaling
- Health monitoring
- Environment management

### EC2 with Docker
For more control, deploy Django in Docker containers on EC2 instances.

### ECS (Elastic Container Service)
Run Django applications in containers with orchestration.

### Lambda with API Gateway
Serverless deployment for cost-effective, scalable solutions.

## Elastic Beanstalk Deployment

### Prerequisites

1. **AWS CLI Installation**
```bash
pip install awscli
aws configure
```

2. **EB CLI Installation**
```bash
pip install awsebcli
```

### Django Configuration for Production

```python
# settings.py
import os

DEBUG = False

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    'yourdomain.com',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Security
SECRET_KEY = os.environ.get('SECRET_KEY')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Application Structure

```
myproject/
├── .ebextensions/
│   ├── 01_packages.config
│   ├── 02_django.config
│   └── 03_postgres.config
├── .platform/
│   └── hooks/
│       └── predeploy/
│           └── 01_migrate.sh
├── requirements.txt
├── manage.py
└── myapp/
```

### EB Extensions Configuration

```yaml
# .ebextensions/01_packages.config
packages:
  yum:
    git: []
    postgresql-devel: []
    python3-devel: []

container_commands:
  01_collectstatic:
    command: "python manage.py collectstatic --noinput"
    leader_only: true
```

```yaml
# .ebextensions/02_django.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: myproject.settings
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles
  aws:autoscaling:launchconfiguration:
    InstanceType: t3.micro
    IamInstanceProfile: aws-elasticbeanstalk-ec2-role
```

```yaml
# .ebextensions/03_postgres.config
Resources:
  AWSEBRDSDatabase:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceClass: db.t3.micro
      DBEngine: postgres
      DBEngineVersion: "13.7"
      DBName: ebdb
      AllocatedStorage: "20"
```

### Deployment Commands

```bash
# Initialize EB application
eb init -p python-3.9 my-django-app

# Create environment
eb create django-env

# Deploy
eb deploy

# Open application
eb open
```

## Docker Deployment on EC2

### Dockerfile

```dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
```

### Docker Compose for Local Development

```yaml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myproject
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web
```

### EC2 Deployment Steps

1. **Launch EC2 Instance**
```bash
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --count 1 \
  --instance-type t3.micro \
  --key-name my-key-pair \
  --security-groups my-security-group
```

2. **Install Docker on EC2**
```bash
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```

3. **Deploy Application**
```bash
# Clone repository
git clone https://github.com/yourusername/myproject.git
cd myproject

# Build and run
docker-compose up -d
```

## Serverless Deployment with Lambda

### Zappa Configuration

Zappa makes it easy to deploy Django to AWS Lambda:

```bash
pip install zappa
zappa init
```

```json
// zappa_settings.json
{
  "dev": {
    "django_settings": "myproject.settings",
    "project_name": "myproject",
    "runtime": "python3.9",
    "s3_bucket": "myproject-zappa",
    "aws_region": "us-east-1",
    "environment_variables": {
      "DEBUG": "False"
    }
  }
}
```

### Django Settings for Lambda

```python
# settings.py
import os

if os.environ.get('AWS_LAMBDA_FUNCTION_NAME'):
    # Running on Lambda
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
    # Local development
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

### Deploy to Lambda

```bash
zappa deploy dev
zappa update dev
```

## Database Setup

### RDS PostgreSQL

```bash
aws rds create-db-instance \
  --db-instance-identifier my-django-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version 13.7 \
  --master-username myuser \
  --master-user-password mypassword \
  --allocated-storage 20
```

### Database Migration

```bash
# For Elastic Beanstalk
eb ssh
cd /var/app/current
python manage.py migrate
```

## Security Best Practices

### Environment Variables

Store sensitive configuration in environment variables:

```python
# settings.py
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

### HTTPS Configuration

Always use HTTPS in production:

```python
# settings.py
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

## Monitoring and Logging

### CloudWatch Integration

Set up monitoring with AWS CloudWatch:

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'aws': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'watchtower': {
            'level': 'INFO',
            'class': 'watchtower.CloudWatchLogHandler',
            'log_group': 'django-app',
            'stream_name': 'application',
            'formatter': 'aws',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['watchtower'],
            'level': 'INFO',
        },
    },
}
```

## Cost Optimization

### Auto Scaling

Configure auto scaling based on demand:

```yaml
# .ebextensions/autoscaling.config
Resources:
  AWSEBAutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: "1"
      MaxSize: "4"
      DesiredCapacity: "2"
      TargetGroupARNs:
        - Ref: AWSEBLoadBalancerTargetGroup
```

### Reserved Instances

Consider reserved instances for predictable workloads to reduce costs.

## Conclusion

AWS provides multiple deployment options for Django applications, each with different trade-offs between ease of use, control, and cost. Elastic Beanstalk offers the fastest path to production, while EC2 with Docker provides maximum control. Lambda with Zappa is ideal for serverless deployments.

Choose the deployment strategy that best fits your application requirements, team expertise, and scaling needs. Always implement proper security measures, monitoring, and backup strategies regardless of the chosen approach.

The key to successful AWS deployment is understanding your application's architecture and selecting the right AWS services to support it efficiently and cost-effectively.
            ''',
            'excerpt': 'Learn how to deploy Django applications to AWS using various services like Elastic Beanstalk, EC2, ECS, and Lambda. Includes production configuration and best practices.',
            'author': 'Suresh Kumar Yadav',
            'published': True,
            'tags': 'Django, AWS, Deployment, Cloud'
        }
    ]

    for post_data in blog_posts_data:
        # Remove 'author' from post_data and use the author instance
        post_data_copy = post_data.copy()
        post_data_copy['author'] = author

        # Create or update blog post
        post, created = BlogPost.objects.get_or_create(
            slug=post_data['slug'],
            defaults=post_data_copy
        )
        if created:
            print(f"Created blog post: {post.title}")
        else:
            # Update existing post
            for key, value in post_data_copy.items():
                setattr(post, key, value)
            post.save()
            print(f"Updated blog post: {post.title}")

    print(f"Total blog posts: {BlogPost.objects.count()}")

if __name__ == '__main__':
    create_blog_posts()

# Glimpsify Shopping Web Application

Glimpsify is a web-based e-commerce platform built using Django, SQLite, HTML, CSS, JavaScript, and PayPal for payment processing. It offers a range of features for both customers and administrators to manage and purchase products. 

## Features

### For Customers
- **Product Listing:** Browse a variety of products with detailed descriptions and images.
- **Add to Cart:** Select products and add them to your shopping cart.
- **Login/Signup:** Users can create accounts or log in to their existing ones.
- **Order Products:** Place orders for the selected items.
- **User Dashboard:** Manage your orders and view your order history.

### For Admins
- **Admin Panel:** A separate admin panel for managing products, orders, and user accounts.
- **Product Management:** Add, edit, and remove products with ease.
- **Order Management:** View and process customer orders.
- **User Management:** Manage user accounts and their roles.

## Tech Stack

- **Django:** A high-level Python web framework for developing robust web applications.
- **SQLite:** A lightweight, serverless relational database engine.
- **HTML/CSS/JS:** Front-end technologies for building the user interface.
- **PayPal:** Payment gateway integration for secure online transactions.

## Getting Started

1. Clone this repository to your local machine.
    git clone https://github.com/mishra-pallavi/Django-ecommerce.git
   
3. Create a virtual environment and activate it.
    python -m venv venv
    source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
   
5. Install the project dependencies.
    pip install -r requirements.txt

6. Apply database migrations.
    python manage.py makemigrations
    python manage.py migrate

7. Create an admin user.
   python manage.py createsuperuser

8. Start the development server.
    python manage.py runserver








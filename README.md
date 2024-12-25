 E-commerce Product API

This project is an E-commerce Product API developed using Django and Django REST Framework (DRF). The API is designed to manage products on an e-commerce platform, including CRUD operations, user authentication, product search, and filtering. Below is a detailed explanation of how the project was implemented.


 1. Project Setup

1. Create the Django Project:
   bash
   django-admin startproject ecommerce_api
   cd ecommerce_api
   

2. Create the Apps:
    For `Products`:
     bash
     python manage.py startapp products
    
    For `Users`:
     bash
     python manage.py startapp users
    

3. Install Dependencies:
    Install Django and Django REST Framework:
    bash
     pip install django djangorestframework
     
   Add the apps to `INSTALLED_APPS` in `settings.py`.

4. Set Up Database:
    Configure MySQL as the database backend in `settings.py`.
    Run migrations:
     bash
     python manage.py migrate
     


 2. Models

1. Product Model:
   - Fields: `name`, `description`, `price`, `category`, `stock_quantity`, `image_url`, `created_date`.
   - Category is implemented as a `CharField` with predefined choices.

2. User Model:
   - Extended Django’s default User model to include additional fields where necessary.
   - Used Django’s built-in authentication.



 3. Endpoints

 Product Management (CRUD):
- Create a Product:
  - Endpoint: `POST /api/products/`
  - Used DRF’s `ModelSerializer` to handle product creation and validation.
- Read Products:
  - Endpoint: `GET /api/products/`
  - Pagination and filtering implemented.
- Update a Product:
  - Endpoint: `PUT /api/products/<id>/`
- Delete a Product:
  - Endpoint: `DELETE /api/products/<id>/`

 User Management (CRUD):
-Register a User:
  - Endpoint: `POST /api/users/register/`
  - Used DRF’s `UserSerializer` for user creation.
- Authentication:
  - Token-based authentication using `djangorestframework-simplejwt`.
  - Endpoint for login: `POST /api/token/`

 Product Search:
- Search Products by Name/Category:
  - Endpoint: `GET /api/products/search/?name=<name>&category=<category>`
  - Allowed partial matches using `icontains` lookup.

 Filtering and Pagination:
- Filtering by Price and Stock Availability:
  - Added filters for price range (`min_price`, `max_price`) and stock availability.
- Pagination:
  - Configured DRF’s `PageNumberPagination` for efficient listing.

---

4. Authentication

- Implemented using Django’s default `User` model and `djangorestframework-simplejwt` for JWT-based authentication.
- Middleware added to ensure authenticated access for product management endpoints.

---

 5. Deployment

  -Set up a PythonAnywhere web app and choose manual configuration.

  -Install dependencies using pip install -r requirements.txt.

  -Update the WSGI file to point to wsgi.py.

  -Set up static and media files in PythonAnywhere settings.

  -Run python manage.py migrate.

  -Restart the web app.

---

 6. Challenges and Solutions

1. Challenge: Implementing efficient filtering and pagination for large datasets.
   - Solution: Used Django ORM’s query optimization techniques and DRF’s pagination classes.

2. Challenge: Securing endpoints.
   - Solution: Implemented JWT-based authentication and thoroughly tested access controls.

---

 7. Future Enhancements

- Add advanced category management and product reviews.
- Implement stock reduction on order placement.
- Allow multiple images per product.
- Develop a wishlist and discount/promotion system.




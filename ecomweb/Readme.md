# EZEE CLOTHING -Ecommerce Website

EZEE CLOTHING is an e-commerce website designed to provide a seamless online shopping experience. This project leverages Django, HTML, CSS, JavaScript, and Bootstrap to create a responsive and user-friendly platform.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Setup](#project-setup)
  - [Pre-requisites](#pre-requisites)
  - [Installation](#installation)
  - [Database Migration](#database-migration)
  - [Create Superuser](#create-superuser)
  - [Running the Server](#running-the-server)
- [Django Overview](#django-overview)
- [Contributors](#contributors)

## Introduction
EZEE CLOTHING is developed to cater to the growing needs of the e-commerce market, particularly focusing on the Nepalese market. The website includes features such as a diverse product catalog, secure payment options, and efficient delivery systems.

## Features

- **Diverse Product Range**: Extensive catalog of clothing items for men, women, and children.
- **User-Friendly Interface**: Intuitive design with easy navigation, filters, and search options.
- **Secure Payment Options**: Multiple payment methods including cash on delivery (COD) and mobile wallets.
- **Efficient Delivery System**: Reliable logistics network with order tracking and notifications.
- **Customer Support**: Responsive customer service via chat, email, and phone.
- **Trust-Building Measures**: Customer reviews, quality assurance, and authenticity guarantees.



## Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Database**: SQLite (default), can be configured to use other databases


## Project Setup

### Pre-requisites
- Python 3.x
- Django
- SQLite (default database for Django)
- HTML & CSS (Bootstrap)
- Git (for version control)


### Installation
1. **Clone the repository:**
    ```bash
     git clone https://github.com/San123desh/Ecommerce_Proj.git

    ```

2. **Create a virtual environment:**
    ```bash
    conda create -n envname python=3.x 
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      conda activate envname
      ```
4. **Activate the virtual environment:**
    - On Windows:
      ```bash
      conda deactivate
      ```



### Database Migration
1. **Make migrations:**
    ```bash
    python manage.py makemigrations
    ```

2. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

### Create Superuser
To access the Django admin panel, you need to create a superuser.
```bash
python manage.py createsuperuser
```

### Running the Server
```bash
python manage.py runserver
```

## Contributors

- Kriteeka Shrestha
- Leo Lepcha
- Ritiz Man Thaiba
- Sandesh Shrestha
# Medical Info. Website

## Requirements Met
1. Sign-up page for users
2. A page where users can fill in their medical information with relevant questions depending on the developer's discretion.
3. A sign-up page for medical practitioners
4. A page that displays the statistical details of the medical records gotten from the users (all users can view this page) e.g. A chart that shows the count for users with Ebola.
5. A table that displays all users and their relevant medical records (only users registered as medical practitioners can view this page).
6. A drop-down filter to show users with specified medical records of your own discretion e.g show only users with Malaria.

## Setup Procedure

> **Note**: If you do not already have it installed, kindly download the latest version of Python 3 [here](https://www.python.org/downloads/). This project will only work for Python >3.
- Clone the project into your machine using the following terminal command
  
        git clone https://github.com/tobeyOguney/medical_info_website.git

- Enter the root project directory via the following terminal command

        cd medical_info_website/

- Install the Pipenv python package via the following terminal command 

        pip install pipenv

- Setup a virtual environment using the Pipenv package via the following command
  
        pipenv shell

- Install the project dependencies via the following command

        pipenv install

- Make sqlite database migrations via the following commands

        python manage.py makemigrations
        python manage.py migrate

- Setup and run the Django development server via the following command

        python manage.py runserver

- Visit the displayed url in your favourite web browser.

> **Note**: You can populate the local database relatively quickly via creating a superuser and using the admin panel at the `BASE_URL/admin` route.
> ```
> python manage.py createsuperuser
> ```

## Snapshots

![ScreenShot](/static/images/screenshot_4.PNG?raw=true "Sign Up Page")
![ScreenShot](/static/images/screenshot_3.PNG?raw=true "Log In Page")
![ScreenShot](/static/images/screenshot_1.PNG?raw=true "Biodata Page")
![ScreenShot](/static/images/screenshot_2.PNG?raw=true "Statistics Page")
![ScreenShot](/static/images/screenshot_5.PNG?raw=true "User Records Page")

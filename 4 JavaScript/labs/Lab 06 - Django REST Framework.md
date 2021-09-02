# Lab 06 - Django REST Framework

Let's build a full API using Django REST Framework!

## Part 1

Start a new Django project and create an app named `students`. Create a `Student` model with:

- First Name (CharField)
- Last Name (CharField)
- Cohort (CharField)
- Favorite Topic (CharField)
- Favorite Teacher (CharField)
- Capstone (URLField)

Use the admin panel to add several students to your database.

## Part 2

Use the [WSVincent DRF tutorial](https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api) and the in-class examples as references to build your API. Once you have the API built, use the built in API documentation website provided by DRF to explore your API and get a sense for the API calls you'll need to make from the frontend.

Your API needs to have the ability to create students, retrieve either a list of students or any specific student, edit a student, and delete students. Make sure you use the browsable API to test all these features out.

## Make Javascript request to API
- install django-cors-headers & add "corsheaders" to app list in settings.py
- add "'corsheaders.middleware.CorsMiddleware'" to MIDDLEWARE on settings.py
- add CORS_ORIGIN_ALLOW_ALL = True on settings.py
- add ALLOWED_HOSTS = ['*' ] on settings.py
- add CSRF_COOKIE_NAME = "csrftoken" on settings.py





## Part 3 (Optional)

Add the ability to search or filter students using URL parameters. Consult the DRF documentation here: https://www.django-rest-framework.org/api-guide/filtering/

## Part 4 (Optional)

Use the following tutorial to dive deeper into the components of Django Rest Framework:

[Official Django REST Framework Tutorial - A Beginners Guide](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)

create virtual environment
- virtualenv <environmentname>

activate virtual environment
- source myenv/Scripts/activate

to start the project

- django-admin startproject <projectname>

to run server

- python manage.py runserver
- to stop: ctrl + c

migrate (Create DB)

- python manage.py migrate
- python manage.py makemigrations

create superuser

- python manage.py createsuperuser

to access admin panel

- ip:port/admin

# create app

- python manage.py startapp <appname>
- Don't forget to register app in settings.py - installed_apps = [ ..., '<appname>',]

# create file 'urls.py' in <appname> folder
write following code
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.index, name='index')
    ]

# Goto views.py
- Create function for each page or route.
for eg:
    def index(request):
        return render(request, 'index.html')

# Create folder name 'templates'
- inside this folder keep the html files for eg. named 'index.html'
- Change path code of urls.py of <appname> folder to
    path('', views.index, name='index')

# Goto <projectname> folder's "urls.py" file and rewrite the code to
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls'))
    ]


PRVO IDE INSTALACIJA VIRTUAL ENVIROMENTA
ZATIM NAPRAVI INSTALACIJE
ONDA PREBACI ENVIROMENT U FOLDER OD DJANGA JER CE BACATI ERROR

py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate    (deactivate)

pip install django                    (django)
pip install pillow                     (pictures)
pip install django-cors-headers        (allow who can on your page)
pip install django-rest-framework      (api)
pip install djoser                     ( provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model)
pip install stripe                     (automatically syncs your Stripe Data to your local database as pre-implemented Django Models allowing you to use the Django ORM, in your code, to work with the data making it easier and faster)
pip install bulma-toast	


django-admin startproject (name of folder)
python manage.py startapp (name of app)

python manage.py createsuperuser         (da bi ju napravio prvo moras makemigrations i migrate napraviti )
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

--------------------------------------

U FOLDER E-COMMERCE DJANGO-VUE 

npm install -g @vue/cli
vue create (name of project)  (babel,vuex,preprocessor,router; 3.x; history mode for youter yes; css preprocessor-saas/scss(with dart-sass); placing in dedicated config files
npm install axios    -library to talk with backend
npm install bulma    -css framework(nesto kao bootstrap)
npm run serve

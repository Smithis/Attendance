pip install --upgrade pip
pip install -r requirements.txt
python manage.py createsuperuser --no-input
python manage.py makemigrations studentattendance
python manage.py migrate studentattendance
pythono manage.py runserver collectstatic


reference link : https://www.w3schools.com/django/index.php

cd django
python3 -m venv myworld
source myworld/bin/activate

python3 -m pip install Django
django-admin --version
cd myworld
django-admin startproject my_tennis_club

cd my_tennis_club
python3 manage.py runserver

cd my_tennis_club
python3 manage.py startapp members

python3 manage.py migrate

http://127.0.0.1:8000/members/

python3 manage.py makemigrations members

python3 manage.py migrate

python3 manage.py sqlmigrate members 0001

python3 manage.py shell

#add record

from members.models import Member
Member.objects.all()
member = Member(firstname='Emil', lastname='Refsnes')
Member.objects.all().values()

#update data
from members.models import Member
x = Member.objects.all()[2]
x.firstname
x.firstname = "Stalikken"
x.save()


#delete record

from members.models import Member
x = Member.objects.all()[2]
x.firstname

#update table
python3 manage.py makemigrations members
python3 manage.py migrate
python3 manage.py shell
from members.models import Member
x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()
Member.objects.all().values()
exit()


To run server 
reach upto django folder  , then activate venv ,then go upto my_tennis_club folder  then runserver 
cd ..
cd ..
source myworld/bin/activate
cd myworld
cd my_tennis_club
python3 manage.py runserver

http://127.0.0.1:8000/
http://127.0.0.1:8000/members/
http://127.0.0.1:8000/members/details/1
http://127.0.0.1:8000/testing/
http://127.0.0.1:8000/admin/


python3 manage.py createsuperuser
username: superadmin
email: superadmin@gmail.com
password: 123

http://127.0.0.1:8000/admin/

Debug = False
pip3 install whitenoise
python3 manage.py collectstatic

http://127.0.0.1:8000/testing/


pip3 install psycopg2-binary


# pasona_test_assisment


# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/assiduus
~~~
# installation
~~~
cd Library_project
pip install -r requairments.txt
~~~~
# Setup DB migration
~~~
create a Student, Books and Borrow Tables

run commands
python manage.py makemigrations
python manage.py migrate
~~~
# Runserver
~~~
python manage.py runserver
~~~
# Rest api for add student 
~~~
http://127.0.0.1:8000/add_student/

Request Body :
  {"name":"Rahul","contact":12349675}
Response Body :
  {
    "success": true
  }
  
  
~~~
 # Rest api for add student 
~~~

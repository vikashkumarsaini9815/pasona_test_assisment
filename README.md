# pasona_test_assisment


# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/pasona_test_assisment.git
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
# Rest api for GET Books 
~~~
http://127.0.0.1:8000/get_books/

Request Body :-

Response Body :
  [
    {
        "book_name": "English",
        "add_time": "2022-12-21T16:41:55.130467"
    }
  ]

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
 # Rest api for add Books 
~~~
http://127.0.0.1:8000/add_book/

  Request Body :
  {"book_name":"English"}
  
  Response Body :
  {
    "success": true
  }
  
  
~~~
 # Rest api for Borrow Book Student 
~~~
http://127.0.0.1:8000/borrow_book/

  Request Body :
  {"student_id":1,"book_id":1}
  
  Response Body :
  {
    "success": true
  }
  
  
~~~
 # Rest api for Borrow Book return Time 
~~~
http://127.0.0.1:8000/return_book_time/

  Request Body :
  {"book_id":1}
  
  Response Body :
  {
    "success": true,
    "message": "return time Update Successfully"
  }
  
  
~~~
 # Rest api for Borrow Book Renew 
~~~
http://127.0.0.1:8000/borrow_book_renew/

  Request Body :
  {"book_id":1}
  
  Response Body :
  {
    "success": true,
    "message": "Renew your book  Update Successfully"
  }
  
  
~~~
# Rest api for GET borrow books 
~~~
http://127.0.0.1:8000/get_borrow_books/pk/

Request Body :-

Response Body :
  [
    {
        "borrow_time": "2022-12-21T17:38:01.164828",
        "return_time": "2022-12-21T16:54:51.212650",
        "book": 1,
        "student": 1
    }
  ]

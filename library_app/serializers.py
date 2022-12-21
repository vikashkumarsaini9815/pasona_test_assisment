from rest_framework import serializers
from library_app.models import Student, Books, Borrow_book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','contact']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['book_name','add_time']


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_book
        fields = ['borrow_time','return_time','book','student']
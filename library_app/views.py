from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from library_app.models import Student, Books, Borrow_book
from library_app.serializers import StudentSerializer,BooksSerializer, BorrowSerializer
import datetime
# Create your views here.





class StudentAPIView(APIView):
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Books_get_APIView(APIView):
    def get (self, request, format = None):
        L1 = Books.objects.all( )
        serializer = BooksSerializer(L1, many = True)
        return Response(serializer.data)



class Book_post_APIView(APIView):
    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Borrow_post_APIView(APIView):
    def post(self, request, format=None):
        data = request.data
        try:
            student_id = data["student_id"]
            book_id = data["book_id"]
            try:
                S1 = Student.objects.get(pk = student_id)
                B2 = Books.objects.get(pk = book_id)
                Bo1 = Borrow_book(student = S1,book = B2)
                Bo1.save()
                return Response({"success":True}, status=status.HTTP_201_CREATED)
            except:
                return Response({"success":False})

        except KeyError:
            message = {"success":"False","message":"KeyError"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)



class Borrow_update2_APIView(APIView):
    def put(self, request, format=None):
        data = request.data
        try:
            book_id = data["book_id"]
            try:
                borrow_time = datetime.datetime.now()
                borrow = Borrow_book.objects.get(book = book_id)
                borrow.borrow_time = borrow_time
                borrow.save()
                return Response({"success":True,"message":"Renew your book  Update Successfully"}, status=status.HTTP_201_CREATED)
            except:
                return Response({"success":False})

        except KeyError:
            message = {"success":"False","message":"KeyError"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)






class Borrow_update_APIView(APIView):
    def put(self, request, format=None):
        data = request.data
        try:
            book_id = data["book_id"]
            try:
                return_time = datetime.datetime.now()
                borrow = Borrow_book.objects.get(book = book_id)
                borrow.return_time = return_time
                borrow.save()
                return Response({"success":True,"message":"return time Update Successfully"}, status=status.HTTP_201_CREATED)
            except:
                return Response({"success":False})

        except KeyError:
            message = {"success":"False","message":"KeyError"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class Borrow_get_APIView(APIView):
    def get (self, request, pk, format = None):
        Boro = Borrow_book.objects.filter(book = 2)
        serializer = BorrowSerializer(Boro, many = True)
    
        return Response(serializer.data)
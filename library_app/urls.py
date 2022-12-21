from django.urls import path
from library_app.views import *




urlpatterns = [
    path("get_books/", Books_get_APIView.as_view(), name = "books" ),
    path("add_student/",StudentAPIView.as_view(),name = "student_add"),
    path("add_book/", Book_post_APIView.as_view(), name = "books" ),
    path("borrow_book/", Borrow_post_APIView.as_view(), name = "borrow" ),
    path("borrow_book_renew/", Borrow_update2_APIView.as_view(), name = "borrow_update" ),
    path("return_book_time/", Borrow_update_APIView.as_view(), name = "borrow_updates" ),
]
from django.contrib import admin
from library_app.models import Student, Books, Borrow_book
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact']

admin.site.register(Student,StudentAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','add_time']

admin.site.register(Books,BookAdmin)

class BorrowAdmin(admin.ModelAdmin):
    list_display = ["id",'borrow_time','return_time','book','student']

admin.site.register(Borrow_book,BorrowAdmin)
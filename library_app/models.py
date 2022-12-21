from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255,blank=True,null = True)
    contact = models.IntegerField(null = True, blank = True)
    

    def __str__(self):
        return f'{self.name},{self.contact}'


class Books(models.Model):
    book_name = models.CharField(max_length =255,null =True,blank = True)
    add_time = models.DateTimeField(auto_now_add=True, null = True, blank=True)
    

    def __str__(self):
        return f'{self.book_name},{self.join_time},{self.update_time}'


class Borrow_book(models.Model):
    borrow_time = models.DateTimeField(auto_now_add=True, null = True, blank=True)
    return_time = models.DateTimeField(default= None, null = True, blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='student')
    book = models.OneToOneField(Books,on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.borrow_time},{self.return_time}'



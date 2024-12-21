
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Student, Address

# Task 1
def task1(request):
    books = Book.objects.filter(price__lte=50)
    return render(request, 'books/lab8/task1.html', {'books': books})

# Task 2
def task2(request):
    books = Book.objects.filter(Q(editions__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'books/lab8/task2.html', {'books': books})

# Task 3
def task3(request):
    books = Book.objects.filter(~Q(editions__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'books/lab8/task3.html', {'books': books})

# Task 4
def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'books/lab8/task4.html', {'books': books})

# Task 5
def task5(request):
    aggregate_data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'books/lab8/task5.html', {'aggregate_data': aggregate_data})

# Task 7
def task7(request):
    city_student_count = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'books/lab8/task7.html', {'city_student_count': city_student_count})
    
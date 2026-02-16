from django.urls import path


from .views import BookCRUDView

urlpatterns=[
    path('book/',BookCRUDView.as_view()),
    path('books/<int:pk>/',BookCRUDView.as_view())
]
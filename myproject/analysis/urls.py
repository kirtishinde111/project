from django.urls import path
#from . import views
from .views import upload_file, process_file, visualize_data, file_list,delete_file



app_name = 'analysis'

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('process/<int:pk>/',process_file, name='process_file'),
    path('visualize/<int:pk>/', visualize_data, name='visualize_data'),
    path('files/', file_list, name='file_list'),
    path('delete/<int:pk>/', delete_file, name='delete_file'),

]


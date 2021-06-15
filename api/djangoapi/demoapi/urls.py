from .views import create_employee, getting_data, update_record, del_record, getting_delete_data, getting_current_data, \
    delete
from django.urls import path


urlpatterns =[
    path('create_employee/', create_employee),
    path('getting_data/', getting_data),
    path('update_record', update_record),
    path('del_record/', del_record),
    path('getting_delete_data/', getting_delete_data),
    path('getting_current_data/', getting_current_data),
    path('delete/', delete),
]
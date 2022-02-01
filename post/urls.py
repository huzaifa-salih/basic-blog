from django.urls import path
from post.views import (
    post_list,
    post_detail,
    create_post,
    post_edit
)


app_name='post'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>', post_detail, name='post_detail'),
    path('<int:id>/edit', post_edit, name='post_edit'),
    path('create/', create_post, name='create_post')
    

]

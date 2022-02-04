from django.urls import path
from post.views import (
    post_list,
    post_detail,
    create_post,
    post_edit,
    PostList,
    PostDetail,
    PostUpdate,
    PostCreate,
)


app_name='post'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>', post_detail, name='post_detail'),
    path('<int:id>/edit', post_edit, name='post_edit'),
    path('create/', create_post, name='create_post'),
    
    path("cbv", PostList.as_view(), name="post_list_cbv"),
    path("cbv/<int:pk>", PostDetail.as_view(), name="post_detail_cbv"),
    path("cbv/<int:pk>/edit", PostUpdate.as_view(), name="post_update_cbv"),
    path("cbv/create", PostCreate.as_view(), name="post_create_cbv"),
]

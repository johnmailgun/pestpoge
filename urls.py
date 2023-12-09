from django.urls import path
from django.views.generic import TemplateView
from .views import BlogCreate, BlogUpdate, BlogDelete, BlogList, BlogDetail

app_name = "pestpoge"

urlpatterns = [
    path('', TemplateView.as_view(template_name="pestpoge/index_2.html"), name="index_2"),
    path('post/create/', BlogCreate.as_view(), name="blog_create"),
    path('post/<int:pk>/update/', BlogUpdate.as_view(), name="blog_update"),
    path('post/<int:pk>/delete/', BlogDelete.as_view(), name="blog_delete"),
    path('post/', BlogList.as_view(), name='blog_list'),
    path('post/<int:pk>/', BlogDetail.as_view(), name="blog_detail"),
]
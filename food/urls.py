from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    # '' 代表http://localhost:8000/food/后面啥也没有
    # /food/
    # path('', views.index, name='index'), # 这个是原来的function view
    path('', views.IndexClassView.as_view(), name='index'), # 这个是class view
    # /food/item
    path('item/', views.item, name='item'),

    # /food/1
    # path('<int:item_id>/', views.detail, name='detail'),
    path('<int:pk>', views.ItemDetailView.as_view(), name='detail'),

    # 添加 items
    # path('add/', views.create_item, name='create_item'),
    path('add/', views.CreateItem.as_view(), name='create_item'),

    # edit
    path('update/<int:item_id>/', views.update_item, name='update_item'),

    # delete
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

]

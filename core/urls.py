"""
URL configuration for restframework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # urls for class generic view
    path('_products/', views.ProductListCreateAPIView.as_view()),
    # path('products/<int:pk>', views.ProductDetailsAPIView.as_view()),
    # ''' By default, the URL parameter is 'pk'. If it's changed, we need to specify the new name 
    #  in the 'lookup_url_kwarg' attribute within the class. '''
    path('_products/<int:product_id>', views.ProductDetailsAPIView.as_view()),
    path('_orders/', views.OrderListAPIView.as_view()),
    path('user_orders/', views.UserOrderListAPIView.as_view(), name='user_orders'),

    # urls for class generic view
    path('_products_info/', views.ProductInfoAPIView.as_view()),


    # urls for function based view
    path('products/', views.product_list),
    path('products_info/', views.product_info),
    path('products/<int:pk>', views.product_detail),
    path('orders/', views.order_list),
    path('silk/', include('silk.urls', namespace='silk'))
]

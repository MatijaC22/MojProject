from django.urls import path, include, re_path

from product import views

urlpatterns = [
    #path('latest-products/', views.LatestProductsList.as_view()),   ovadvoje radi, to je bilo za test
    re_path(r'^latest-products/$', views.LatestProductsList.as_view()), 
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
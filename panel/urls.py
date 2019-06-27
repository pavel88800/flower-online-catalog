from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name="index_admin_url"),

    path('category/list/', CategoryList.as_view(), name='category_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:category_id>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:category_id>/delete/', CategoryDelete.as_view(), name='category_delete_url'),

    path('category/<str:category_id>/sub_category/list/', SubCategoryList.as_view(), name="sub_category_list_url"),
    path('sub_category/create/', SubCategoriesCreate.as_view(), name='sub_category_create_url'),
    path('sub_category/<str:sub_category_id>/delete/', SubCategoryDelete.as_view(), name='sub_category_delete_url'),
    path('sub_category/<str:sub_category_id>/update/', SubCategoryUpdate.as_view(), name="sub_category_update_url"),

    path('catalog_item/create/', CatalogItemCreate.as_view(), name="catalog_item_create_url"),

    path('get_subcategory/', get_subcaegories, name="get_subcategory_url"),

]

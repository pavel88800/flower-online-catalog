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

    path('catalog_item/', CatalogItemAllList.as_view(), name="catalog_items_all_list_url"),
    path('catalog_item/<str:sub_category_id>/list/', CatalogItemList.as_view(), name="catalog_item_list_url"),
    path('catalog_item/create/', CatalogItemCreate.as_view(), name="catalog_item_create_url"),
    path('catalog_item/<str:item_id>/update/', CatalogItemUpdate.as_view(), name="catalog_item_update_url"),
    path('catalog_item/<str:item_id>/delete/', CatalogItemDelete.as_view(), name="catalog_item_delete_url"),

    path('static_page/all_list/', StaticPageAllList.as_view(), name="static_pages_all_list_url"),
    path('static_page/create/', StaticPageCreate.as_view(), name="static_pages_create_url"),
    path('static_page/<str:page_id>/update/', StaticPageUpdate.as_view(), name="static_pages_update_url"),
    path('static_page/<str:page_id>/delete/', StaticPageDelete.as_view(), name="static_pages_delete_url"),

    path('tags/list/', TagsList.as_view(), name="tags_list_url"),
    path('tags/create/', TagsCreate.as_view(), name='tag_create_url'),
    path('tags/<str:tag_id>/update/', TagsUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:tag_id>/delete/', TagsDelete.as_view(), name='tag_delete_url'),
    path('tags/<str:tag_id>/tag_items/', TagItemsList.as_view(), name='tag_items_url'),

    path('articles/list/', ArticleList.as_view(), name="articles_list_url"),
    path('articles/create/', ArticleCreate.as_view(), name="articles_create_url"),
    path('articles/<str:article_id>/update/', ArticleUpdate.as_view(), name="articles_update_url"),
    path('articles/<str:article_id>/delete/', ArticleDelete.as_view(), name="articles_delete_url"),

    path('reviews/list/', ReviewsList.as_view(), name="reviews_list_url"),
    path('reviews/create/', ReviewsCreate.as_view(), name="review_create_url"),
    path('reviews/<str:review_id>/update/', ReviewsUpdate.as_view(), name="review_update_url"),
    path('reviews/<str:review_id>/delete/', ReviewDelete.as_view(), name='review_delete_url'),

    path('get_subcategory/', get_subcaegories, name="get_subcategory_url"),
    path('logout/', logout_view, name="logout_panel_url"),
]

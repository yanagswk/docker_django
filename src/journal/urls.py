from django.urls import path
from . import views
from .views import comment_approve, comment_remove, reply_approve, reply_remove


app_name = 'journal'

urlpatterns = [
    path('', views.JournalListView.as_view(), name="journal_list"),
    path('journal-detail/<int:pk>/', views.JournalDetailView.as_view(), name="journal_detail"),
    path('journal-create/', views.JournalCreateView.as_view(), name='journal_create'),
    path('journal-update/<int:pk>/', views.JournalUpdateView.as_view(), name="journal_update"),
    path('journal-delete/<int:pk>/', views.JournalDeleteView.as_view(), name="journal_delete"),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/', views.CategoryJournalView.as_view(), name='category_journal'),
    path('tag/<str:tag_slug>/', views.TagJournalView.as_view(), name='tag_journal'),
    path('search/', views.SearchJournalView.as_view(), name='search_journal'),
    path('inquiry/', views.JournalInquiryView.as_view(), name="inquiry"),
    path('comment/<int:pk>/', views.CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', views.ReplyFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', views.reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', views.reply_remove, name='reply_remove'),
]

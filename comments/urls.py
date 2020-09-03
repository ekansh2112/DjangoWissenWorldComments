from . import views
from django.urls import path
urlpatterns = [
    path('delete/<int:pk>', 
        views.CommentDeleteView.as_view(), name='comment_delete'),
    path('page2',views.page2,name='page2'),
    path('',views.cmnts,name="mainpage"),
    path('comment/', 
        views.CommentCreateView.as_view(), name='comment_create'),
    
    # path('<str:url>/', 
    #     views.CommentDetailView.as_view(), name='comment_detail'),
    
]
      
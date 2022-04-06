from django.urls import path

from. import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),
    #제네릭 뷰
    #제네릭 뷰는 편리한 기능이지만 초심자에게는 혼란을 줄 수 있다
    #단점: 복잡한 문제를 해결할 때 오히려 개발 난이도가 높아진다
    #path('', views.IndexView.as_view()),
    #path('<int:pk>/', views.DetailView.as_view()),
]
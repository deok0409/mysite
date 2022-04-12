from django.urls import path

from. views import base_views, question_views, answer_views, comment_views

app_name = 'pybo'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # quesetion_views
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    # answer_views
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    # comment_views
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer,
         name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer,
         name='comment_delete_answer'),

    #제네릭 뷰
    #제네릭 뷰는 편리한 기능이지만 초심자에게는 혼란을 줄 수 있다
    #단점: 복잡한 문제를 해결할 때 오히려 개발 난이도가 높아진다
    #path('', views.IndexView.as_view()),
    #path('<int:pk>/', views.DetailView.as_view()),
]
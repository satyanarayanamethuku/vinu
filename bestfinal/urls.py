"""bestfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from best import views 
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('satya/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    path('application/',views.application),
    path('privacypolicy/',views.privacypolicy),
    path('terms/',views.terms),
    path('refund/',views.refund),
    path('six/', views.six),
    path('seven/',views.seven),
    path('eight/',views.eight),
    path('nine/',views.nine),
    path('ten/',views.ten),
    path('about/',views.about),
    path('update/', views.update),
    path('gallery/',views.gallery),
    path('brouchars/',views.brouchars),
    path('contact/',views.contact),
    path('student_login/',views.student_login),
    path('admin_login/',views.admin_login),
    path('pay/', views.payment),
    path('payment2/',views.payment2),
    path('bhimapp/',views.bhimapp),
    path('student_profile/',views.student_profile),
    path('student_notification/',views.student_notification),
    path('student_mocktest/',views.student_mocktest),
    path('student_test/',views.student_test),
    path('student_logout/',views.student_logout),
    path('student_profile_view/',views.student_profile_view),
    # path('mail_sent/',views.mail_sent),
    path('offline_register/',views.offline_register),
    url(r'^index/',views.index_view),
    url(r'^register/',views.register_view, name='register'),
    url(r'^login/',views.login_view, name='login'),
    url(r'^logout/',views.logout_view, name='logout'),
    url(r'^reset/$',auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    
    path('quiz/',views.quiz),
    path('student_profile_display/',views.student_profile_display, name='display_view'),
    # url(r'^studelete/(?P<id>\d+)/$',views.studelete),
    url(r'^mail_sent/(?P<id>\d+)/$',views.mail_sent),

    url(r'^stuedit/(?P<pk>\d+)/$',views.StudentView.as_view()),
    path('time/',views.time),
    path('admin_search_date/', views.admin_search_date),
    url(r'^delete/(?P<pk>\d+)/$', views.StudentDeleteView.as_view()),
   

]
    



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
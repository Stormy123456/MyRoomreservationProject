"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from store import Linemessage, views,Usingroom,Log,Linemessage
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import include,url
from django.urls import include, re_path as url

app_name = "tasks"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^create/$', views.product_create, name='product_create'),
    url(r'^products/(?P<pk>\w+)/update/$', views.product_update, name='product_update'),
    url(r'^employeeBoard/(?P<pk>\w+)/update/$', views.product_update, name='product_update'),
    url(r'^products/(?P<pk>\w+)/delete/$', views.product_delete, name='product_delete'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create$', views.book_create, name='book_create'),

    # url(r'^historyUsingroom/$',Usingroom.historyUsingroom,name='historyUsingroom'),
    url(r'^roomhistoryviews/(?P<pk>\w+)/update/$', views.roomhistoryviews, name='roomhistoryviews'),
    url(r'^historyUsingroomBoard/(?P<pk>\w+)/update/$', views.roomhistoryviews, name='roomhistoryviews'),

    path('historyUsingroom/',Usingroom.historyUsingroom,name='historyUsingroom'),
    path('ShowhistoryUsingroom/',Usingroom.ShowhistoryUsingroom,name='ShowhistoryUsingroom'),

    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('employeeAdd/',views.employeeAdd),
    path('employeeAddnewdata/',views.employeeAddnewdata,name='employeeAddnewdata'),
    path('employeeBoard/',views.employeeBoard),
    path('employeeEdit/',views.employeeEdit,name='employeeEdit'),
    path('employeeUpdate/',views.employeeUpdate,name='employeeUpdate'),
    path('employeeDelete/',views.employeeDelete,name='employeeDelete'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('requestdata/',views.requestdata,name='requestdata'),
    path('registerNewdata/',views.registerNewdata,name='registerNewdata'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('userindex/',views.userindex),
    # path('userconfirm/',views.userconfirm),
    path('userconfirmRoom/',views.userconfirmRoom,name='userconfirmRoom'),
    path('userconfirmRoomSelected/',views.userconfirmRoomSelected,name='userconfirmRoomSelected'),
    path('userconfirmRoomSelected2/',views.userconfirmRoomSelected2,name='userconfirmRoomSelected2'),
    path('userAddconfirm/',views.userAddconfirm,name='userAddconfirm'),
    path('userToken/',Linemessage.userToken,name='userToken'),
    path('userTokenAdd/',Linemessage.userTokenAdd,name='userTokenAdd'),
    path('logout/',views.logout,name='logout'),
    path('userEdit/',views.userEdit,name='userEdit'),
    path('userUpdate/',views.userUpdate,name='userUpdate'),
    path('userpicEdit/',views.userpicEdit,name='userpicEdit'),
    path('userpicUpdate/',views.userpicUpdate,name='userpicUpdate'),
    path('userBoard/',views.userBoard,name='userBoard'),
    path('userReservationBoard/',views.userReservationBoard,name='userReservationBoard'),
    path('userReservationDelete/',views.userReservationDelete,name='userReservationDelete'),
    path('userDelete/',views.userDelete,name='userDelete'),
    path('punishmentBoard/',views.punishmentBoard,name='punishmentBoard'),
    path('punishmentAdd/',views.punishmentAdd),
    path('punishmentAddnewdata/',views.punishmentAddnewdata,name='punishmentAddnewdata'),
    path('punishmentEdit/',views.punishmentEdit,name='punishmentEdit'),
    path('punishmentToggleOff/',views.punishmentToggleOff,name='punishmentToggleOff'),
    path('punishmentToggleOn/',views.punishmentToggleOn,name='punishmentToggleOn'),
    path('punishmentUpdate/',views.punishmentUpdate,name='punishmentUpdate'),
    path('punishmentDelete/',views.punishmentDelete,name='punishmentDelete'),
    path('banuserBoard/',views.banuserBoard,name='banuserBoard'),
    path('banuserAddnewdata/',views.banuserAddnewdata,name='banuserAddnewdata'),
    path('banuserDelete/',views.banuserDelete,name='banuserDelete'),
    path('adminconfirm/',views.adminconfirm,name='adminconfirm'),
    path('adminAddconfirm/',views.adminAddconfirm,name='adminAddconfirm'),
    path('userReservation/',views.userReservation,name='userReservation'),
    path('userReservationAdd/',views.userReservationAdd,name='userReservationAdd'),
    path('historyReservation/',views.historyReservation,name='historyReservation'),
    path('historyBoard/',views.historyBoard,name='historyBoard'),
    path('historySearch/',views.historySearch,name='historySearch'),
    path('historyLog/',Log.historyLog,name='historyLog'),
    path('roomBoard/',views.roomBoard,name='roomBoard'),
    path('roomAdd/',views.roomAdd,name='roomAdd'),
    path('roomAddnewdata/',views.roomAddnewdata,name='roomAddnewdata'),
    path('roomDelete/',views.roomDelete,name='roomDelete'),
    path('roomEdit/',views.roomEdit,name='roomEdit'),
    path('roomUpdate/',views.roomUpdate,name='roomUpdate'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# if settings.DEBUG :
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



from django.urls import path,include
from . import views
from . import maintainance
from django.conf import settings
from django.conf.urls.static import static

maintainance_check = False

if maintainance_check:
    urlpatterns = [
        path("", maintainance.home, name="home"),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

else:
    urlpatterns = [
        path("", views.home, name="home"),
        path("products/", views.products, name="products"),
        path("R-and-D/", views.r_d, name="r&d"),
        path("about-us/", views.about, name="about"),
        path("admin/inquiry/", views.admin_inquiry, name="admin-inquiry"),
        path("admin/logs/", views.site_log, name="site-log"),
        path("admin/terms-and-conditions/", views.terms, name="terms"),
        path("admin/privacy-policy/", views.privacy, name="privacy"),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
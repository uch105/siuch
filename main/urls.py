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
        path("terms-and-conditions/", views.terms, name="terms"),
        path("privacy-policy/", views.privacy, name="privacy"),
        path("checkout/", views.checkout, name="checkout"),
        path("checkout/success/", views.checkoutsuccess, name="checkoutsuccess"),
        path("checkout/fail/", views.checkoutfail, name="checkoutfail"),
        path("checkout/cancel/", views.checkoutcancel, name="checkoutcancel"),
        path("checkout/ipn_listener/", views.ipn_listener, name="ipn_listener"),
        path("checkout/payment/<str:pk>/<str:pk2>/", views.create_a_payment, name="payment"),
        path("api/check_tran_id/<str:pk>/", views.check_tran_id, name="check_tran_id"),
        #portfolio urls
        path("portfolio/tanvir-ahmed-monon/", views.portfolio_tanvirahmedmonon, name="tanvirahmedmonon"),
        path("portfolio/uch/", views.portfolio_uch, name="uch"),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
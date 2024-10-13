from django.contrib.sitemaps import Sitemap
from .models import *

'''
class YourModelSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return YourModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
'''
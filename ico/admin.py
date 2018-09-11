# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import NsUsers, NsBlog

admin.site.register(NsUsers)
admin.site.register(NsBlog)

# Register your models here.
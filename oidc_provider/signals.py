# -*- coding: utf-8 -*-
from django.dispatch import Signal


#  Provided Arguments ['user', 'client', 'scope']
user_accept_consent = Signal()
user_decline_consent = Signal()

# -*- coding: utf-8 -*-
from django.dispatch import Signal


# Signal provides the arguments 'user', 'client', 'scope'
user_accept_consent = Signal()

# Signal provides the arguments 'user', 'client', 'scope'
user_decline_consent = Signal()

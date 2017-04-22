#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
class VerifiedEmail(object):
    def __init__(self, *args, **kwargs):
        self.__email = ""
    def set_email(self, value):
        if '@' not in value:
            raise Exception("This doesn't look like an email address.")
        self.__email = value
    def get_email(self):
        return self.__email
    email = property(get_email, set_email)

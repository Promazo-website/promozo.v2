__author__ = 'marc'
from django.conf import settings
from hashids import Hashids
import datetime
from django.core.exceptions import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import random
User = get_user_model()

class NewUserReg():
    """
    This class contains methods needed to proccess a new user into the system
    and when needed to reset their password
    """

    def __init__(self):
        self.hasher = Hashids(salt=settings.HASH_SALT_KEY, min_length=15)
        self.BASE_URL=settings.BASE_URL

    def __generate_user_hash(self, user):
        """
        creates a hash code from the userid
        :param user:
        :return: user.id
        """
        return self.hasher.encode(user.id)

    def __generate_date_hash(self):
        """
        creates a hash code from todays date in ordinal
        :return:hash encoded date
        """
        return self.hasher.encode(datetime.date.today().toordinal())

    def __verify_date_hash(self, datehash):
        """
        Decodes the datehash and checks to see if the date is within
        7 days of it being created
        :param datehash:
        :return:Boolean
        """
        hash_date = self.hasher.decode(datehash)[0]
        if datetime.date.today().toordinal()-hash_date > settings.REGISTRATION_TIME:
            return False
        else:
            return True

    def __verify_user_hash(self, userhash):
        """
        decodes the hashed user id, checks to see if its a valid user and
        that the user is not active. If the user is already active it means
        they have already verified their user so the link is no longer
        valid
        :param userhash:
        :return:
        """
        try:
            user = User.objects.get(id=self.hasher.decode(userhash)[0])
            return user
        except ObjectDoesNotExist:
            return 'No User Found'


    def __verify_user_reset_hash(self, userhash):
        """
        decodes the hashed userid passed as an argument and
        checks the id refers to a valid user. This is used
        for password resets
        :param userhash:
        :return:
        """
        try:
            user = User.objects.get(id=self.hasher.decode(userhash)[0])
        except ObjectDoesNotExist:
            return 'No User Found'
        return user

    def __generate_url(self, user):
        """
        creates the url to be placed into emails for users to verify
        their user before activating it
        :param user:
        :return:
        """
        return '%s/register/validate/%s/%s/' % (self.BASE_URL, self.__generate_date_hash(),
                                                 self.__generate_user_hash(user))
    def __generate_reset_url(self, user):
        """
        cerates the url to be placed into emails for users to
        verify who they are so they can reset their password
        :param user:
        :return:
        """
        return '%s/password/reset/%s/%s/' % (self.BASE_URL, self.__generate_date_hash(),
                                                 self.__generate_user_hash(user))



    def Generate_url(self,user):
        """
        Wrapper to allow for testing the verify url
        :param user:
        :return:
        """
        return self.__generate_url(user)

    def Generate_reset_url(self,user):
        """
        Wrapper to allow for testing to verify the reset password url
        :param user:
        :return:
        """
        return self.__generate_reset_url(user)

    def Verify_url(self,userhash,datehash):
        """
        checks that the url is valid. if its vaild it will activate the user,
        create an account and return the user object
        :param userhash:
        :param datehash:
        :return:
        """
        user= self.__verify_user_hash(userhash)
        if isinstance(user,User):
            if self.__verify_date_hash(datehash):
                return user
            else:
                return 'Out of date'
        else:
            return 'Bad User'

    def Verify_Reset_url(self,userhash,datehash):
        """
        Verifies the url on password resets
        :param userhash:
        :param datehash:
        :return:
        """
        user= self.__verify_user_reset_hash(userhash)
        if isinstance(user,User):
            if self.__verify_date_hash(datehash):
                user.is_active=True
                user.save()
                return 'Done'
            else:
                return 'Out of date'
        else:
            return user

    def Get_user(self,userhash):
        """
        used for unit tests to obtain the user record for
        a given hash code
        :param userhash:
        :return:
        """
        user= self.__verify_user_reset_hash(userhash)
        return user.id

    def GenerateUserEmail(self,user):
        """
        main method for generating the user verification email
        :param user:
        :return:
        """
        html_email_body = render_to_string("register_email_template.html",
                                           { 'user': user,'type':'user',
                                             'register_url':self.__generate_url(user)})
        text_email_body = render_to_string("register_email_template.txt",
                                           { 'user': user,'type':'user',
                                             'register_url':self.__generate_url(user)})
        send_mail(subject='Validate Your email for Promozo',
                  message=text_email_body,
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[user.email,],
                  html_message=html_email_body)


    def GenerateResetEmail(self,user):
        """
        main method used to generate the password reset verification email
        :param user:
        :return:
        """
        html_email_body = render_to_string("reset_email_template.txt",
                                           { 'user': user,
                                             'reset_url':self.__generate_reset_url(user)})
        text_email_body = render_to_string("reset_email_template.txt",
                                           { 'user': user,
                                             'reset_url':self.__generate_reset_url(user)})
        try:
            send_mail(subject='Reset Password for Promozo',
                      message=text_email_body,
                      from_email=settings.DEFAULT_FROM_EMAIL,
                      recipient_list=[user.email,],
                      html_message=html_email_body)
            return True
        except:
            return False
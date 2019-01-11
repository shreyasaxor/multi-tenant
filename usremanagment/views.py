# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from tenantapp.models import Client
from usremanagment.models import User
from usremanagment.serializers import UserSerializers
from rest_framework import status


class GetUser(APIView):
    """ this api retrives all users and save users  """

    def get(self,request,*args,**kwargs):
        """get method reterive all users"""


        obj = User.objects.all()
        serializer = UserSerializers(obj, many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        """post methods saves the users  either self signup or referal signup"""
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            first_name=request.data['first_name']
            tenant = Client(domain_url=first_name + ".localhost",
                            schema_name=first_name,
                            name=first_name,
                            paid_until='2022-12-12',
                            on_trial=True)
            tenant.save()
            return Response({'referal_url': serializer.data}, status=status.HTTP_200_OK)
        else:
            print serializer.errors
            return Response({'referal_url': serializer.errors}, status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):

        first_name = request.data['first_name']
        client =Client.objects.get(schema_name=first_name)
        client.delete(force_drop=True)
        return Response({'referal_url': "done"}, status=status.HTTP_200_OK)

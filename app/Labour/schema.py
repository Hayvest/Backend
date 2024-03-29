import datetime

import graphene
from Buyer.models import Buyer
from Farm.models import Farm
from Labourers.models import Labourer
from Wards.models import Ward
from django.db.models import Q
from graphene_django import DjangoObjectType

from .models import LabourService, PayPeriod, LaboursRequest, LabourApplication


class LabourType(DjangoObjectType):
    class Meta:
        model = LabourService


class LabourRequestType(DjangoObjectType):
    class Meta:
        model = LaboursRequest


class PayPeriodsTypes(DjangoObjectType):
    class Meta:
        model = PayPeriod


class LabourApplicationType(DjangoObjectType):
    class Meta:
        model = LabourApplication


class Query(graphene.ObjectType):
    services = graphene.List(LabourType, name=graphene.String())
    labourRequests = graphene.List(LabourRequestType, ward=graphene.Int(), service=graphene.Int())
    payPeriod = graphene.List(PayPeriodsTypes)
    applications = graphene.List(LabourApplicationType, RequestId=graphene.Int(required=True))

    def resolve_services(self, info, name=None):
        srv = LabourService.objects.all()
        print(srv)
        if name:
            filters = (
                Q(title__icontains=name)
            )
            srv = srv.filter(filters)

        return srv

    def resolve_payPeriod(self, info):
        periods = PayPeriod.objects.all()
        return periods

    def resolve_labourRequests(self, info, ward=None, service=None):
        lrs = LaboursRequest.objects.filter(startDate__gt=datetime.datetime.now())
        if ward:
            w = Ward.objects.get(id=ward)
            lrs = LaboursRequest.objects.filter(ward=w)
        if service:
            s = LabourService.objects.get(id=service)
            lrs = LaboursRequest.objects.filter(service=s)

        if ward and service:
            w = Ward.objects.get(id=ward)
            s = LabourService.objects.get(id=service)
            lrs = LaboursRequest.objects.filter(service=s).filter(ward=w)

        return lrs

    def resolve_applications(self, info, RequestId):
        request = LaboursRequest.objects.get(id=RequestId)
        applications = LabourApplication.objects.filter(LaboursRequest=request)

        return applications



class createLabourReq(graphene.Mutation):
    request = graphene.Field(LabourRequestType)

    class Arguments:
        ward = graphene.Int(required=True)
        farm = graphene.Int(required=False)
        buyer = graphene.Int(required=False)
        service = graphene.Int(required=True)
        startDate = graphene.String(required=True)
        time = graphene.String(required=True)
        payPeriod = graphene.Int(required=True)
        pay = graphene.Int(required=True)
        workers = graphene.Int(required=True)
        periodLength = graphene.Int(required=True)

    def mutate(self, info, ward, service, startDate, time, payPeriod, pay,
               periodLength, workers, farm=None, buyer=None):
        request = LaboursRequest()
        w = Ward.objects.get(id=ward)
        if farm:
            f = Farm.objects.get(id=farm)
            request.farm = f
        else:
            b = Buyer.objects.get(id=buyer)
            request.buyer = b
        s = LabourService.objects.get(id=service)
        date_time = f"{startDate} {time}"
        start_date_time = datetime.datetime.strptime(date_time, '%d-%m-%Y %H:%M')
        request.ward = w
        request.service = s
        request.payPeriod = PayPeriod.objects.get(id=payPeriod)
        request.pay = pay
        request.periodNumber = periodLength
        request.startDate = start_date_time
        request.workers = workers
        request.save()

        return createLabourReq(request=request)


class makeApplication(graphene.Mutation):
    application = graphene.Field(LabourApplicationType)

    class Arguments:
        LabourRequest = graphene.Int(required=True)
        LabourerId = graphene.Int(required=True)

    def mutate(self, info, LabourRequest, LabourerId):
        LabourReq = LaboursRequest.objects.get(id=LabourRequest)
        labourer = Labourer.objects.get(id=LabourerId)

        application = LabourApplication()
        application.Labourer = labourer
        application.LaboursRequest = LabourReq
        application.hired = False

        application.save()

        return makeApplication(application=application)


class RespondApplication(graphene.Mutation):
    application = graphene.Field(LabourApplicationType)

    class Arguments:
        LabourApply = graphene.Int(required=True)
        hiring = graphene.Boolean(required=True)

    def mutate(self, info, LabourApply, hiring):
        application = LabourApplication.objects.get(id=LabourApply)
        application.hired = hiring
        application.responded = True

        application.save()

        return RespondApplication(application=application)


class Mutation(graphene.ObjectType):
    create_Labour_Req = createLabourReq.Field()
    make_Application = makeApplication.Field()
    respond_to_Application = RespondApplication.Field()

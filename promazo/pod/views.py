
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *

from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
# Create your views here.

#list of pod members

class PodViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = podSerializer
    queryset = pod.objects.all()
    @detail_route(methods=['GET'])
    def permission(self, request, pk):
        try:
            rec=podMembers.objects.get(pod=self.get_object(),member=request.user)
            return Response(rec.has_permission(request.GET['permission']))
        except:
            return Response(False)
    @list_route()
    def mypods(self, request):
        queryset = [x.pod for x in podMembers.objects.filter(member=request.user)]
        ser = podSerializer(queryset,many=True)
        return Response(ser.data)

    @detail_route(methods=['GET'])
    def available_users(self,request,pk):
        queryset =  User.objects.filter(is_active=True).exclude(id__in=[x.member.id for x in podMembers.objects.filter(pod__id=pk)])
        ser = userSerializer(queryset,many=True)
        return Response(ser.data)


class PodMembersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = podMembersSerializer
    queryset = podMembers.objects.all()
    @detail_route(methods=['GET'])
    def members(self,request, pk):
        queryset=podMembers.objects.filter(pod__id=pk)
        ser=podMembersSerializer(queryset,many=True)
        return Response(ser.data)



class PodRolesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = podRoleSerializer
    queryset = podRole.objects.all()

class PodPermissionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = podPermissionsSerializer
    queryset = podPermissions.objects.all()
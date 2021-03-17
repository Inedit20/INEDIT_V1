import django_filters
from classroom.models import Process, Activity
import django_filters.rest_framework




class ProcessFilter (django_filters.FilterSet):
    activity_process = django_filters.ModelChoiceFilter(queryset=Activity.objects.all())
    process_name = django_filters.ModelChoiceFilter(queryset=Process.objects.all())


    class Meta:
        model =Process
        fields = ['process_name','activity_process']




class ActivityFilter (django_filters.FilterSet):
    activity_name = django_filters.ModelChoiceFilter(queryset=Activity.objects.all())
   

    class Meta:
        model =Activity
        fields = ['activity_name']







class ProcessFilter_1 (django_filters.FilterSet):
    u__contains = django_filters.rest_framework.CharFilter(field_name='process_name', lookup_expr='icontains')


    class Meta:
        model =Process
        fields = ['u__contains',]


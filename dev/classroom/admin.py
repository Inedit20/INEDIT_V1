from django.contrib import admin
from .models import Process,Partner, FamilyProcess, Activity, Decision,Skill, Type_actors,Output,Task,Input, Actor, Technologie,Decision_act,Skill_act,Technologie_act,Actor_act,Input_act,Output_act


# Register your models here.

admin.site.register(Process)
admin.site.register(Activity)
admin.site.register(Type_actors)
admin.site.register(Decision)
admin.site.register(Output)
admin.site.register(Task)
admin.site.register(Input)
admin.site.register(Actor)
admin.site.register(Technologie)
admin.site.register(Skill)
admin.site.register(Partner)
admin.site.register(Decision_act)
admin.site.register(Output_act)
admin.site.register(Input_act)
admin.site.register(Actor_act)
admin.site.register(Technologie_act)
admin.site.register(Skill_act)
admin.site.register(FamilyProcess)
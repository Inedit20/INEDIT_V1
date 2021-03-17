
from django.db import models
from PIL import Image
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings 
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from translations.models import Translatable
from phone_field import PhoneField
from ckeditor.fields import RichTextField
from django.core.paginator import Paginator 









class  FamilyProcess(models.Model):
    process_name = models.CharField(max_length=270,verbose_name= u"Process title  ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    figure = models.ImageField(upload_to='media/', default='default.jpg', verbose_name=u"Figure associated", null=True)

    def __str__(self):
        return str(self.process_name)





class Process(models.Model):
    process_name = models.CharField(max_length=270,verbose_name= u"Process title  ",  null=True, blank=True)
    family_process = models.ManyToManyField(FamilyProcess, verbose_name= u"Family_proces  ", help_text=u" help text.", related_name='family_process', blank=True) 
    definition = RichTextField(blank=True, null=True)


    def __str__(self):
        return str(self.process_name)
     
    
class TypePartner(models.Model):
    type_name = models.CharField(max_length=270,verbose_name= u"Process title  ",  null=True, blank=True)
    


    def __str__(self):
        return str(self.type_name)
     







class Partner(models.Model):
    partner_name = models.CharField(max_length=270,verbose_name= u"Activity name   ",  null=True, blank=True)
    image = models.ImageField(upload_to='media/', default='default.jpg', verbose_name=u"Figure associated", null=True)
    

    def __str__(self):
        return str(self.partner_name)







class Session(models.Model):
    session_name = models.CharField(max_length=270,verbose_name= u"name  ",  null=True, blank=True)
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts',  blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    
    def __str__(self):
        return str(self.user.session_name)










class Activity(models.Model):
    activity_name = models.CharField(max_length=270,verbose_name= u"Activity name   ",  null=True, blank=True)
    definition = RichTextField(blank=True,verbose_name=u"Activity description ",  null=True)
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE, verbose_name=u"Select a Process :", related_name='activity_process',  blank=True)
  
  
  
  
  
  
  
  
  
    def __str__(self):
        return str(self.activity_name)






class Task(models.Model):
    name = models.CharField(max_length=270,verbose_name= u"Task title   ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    activety_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity Name  ", related_name='task_process',  blank=True)
   
    def __str__(self):
        return str(self.name)




class Decision(models.Model):
    decision_name = models.CharField(max_length=270,verbose_name= u"Decision title   ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Task Decision ", related_name='decision_process')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_dec')
    created_at = models.DateTimeField(auto_now_add=True, null= True)   
    def __str__(self):
        return str(self.decision_name)
    




class Output(models.Model):
    output_name = models.CharField(max_length=270,verbose_name= u"Output title ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Task Output ", related_name='output_process')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_out')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.output_name) 




class Type_actors(models.Model):
    type_name = models.CharField(max_length=270,verbose_name= u"Type actor title :  ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    def __str__(self):
        return str(self.type_name)





class Actor(models.Model):
    actor_name = models.CharField(max_length=270,verbose_name= u"Type or Name   ",help_text=u"User, ",  null=True, blank=True)
    prenom = models.CharField(max_length=270,verbose_name= u"Last Name  ",  null=True, blank=True)
    presentation = RichTextField(blank=True, null=True)
    adress = models.CharField(max_length=270,verbose_name= u"Adress  ",  null=True, blank=True)
    contact = PhoneField(help_text="Contact", null=True, blank=True)
    partenair_nam1= models.CharField(max_length=270,verbose_name= u"Partner ",  null=True, blank=True)
    partenair_nam2= models.CharField(max_length=270,verbose_name= u"Partner ",  null=True, blank=True)
    partenair_nam3= models.CharField(max_length=270,verbose_name= u"Partner  ",  null=True, blank=True)
    partenair_nam4= models.CharField(max_length=270,verbose_name= u"Partner  ",  null=True, blank=True)
    type_actor = models.CharField(max_length=270,verbose_name= u"Type of actor  ",help_text=u" help text.",  null=True, blank=True)
    task_id = models.ManyToManyField(Task, verbose_name= u"Actor_proces  ", help_text=u" help text.", related_name='actor_process', blank=True) 
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_act')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        if self.actor_name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.actor_name)



class Input(models.Model):
    input_name = models.CharField(max_length=270,verbose_name= u"Input   ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Task Input ", related_name='ressource_process')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_input')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return str(self.input_name) 




class Skill(models.Model):
    skills_name = models.CharField(max_length=270,verbose_name= u"Skill title:  ",  null=True, blank=True)
    skills_maturity = models.CharField(max_length=270,verbose_name= u"Skill maturity :  ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Task  ", related_name='skill_process')   
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_skill')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.skills_name) 

    
class Technologie(models.Model):
    technologie_name = models.CharField(max_length=270,verbose_name= u"Technoly :  ",  null=True, blank=True)
    definition = RichTextField(blank=True, null=True)
    technology_maturity = models.CharField(max_length=270,verbose_name= u"Technology's maturity :  ",  null=True, blank=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Task ", related_name='tech_process')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_tech')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.technologie_name)






class Decision_act(models.Model):
    decision_name = models.CharField(max_length=270,verbose_name= u"Decision title   ",  null=True, blank=True)
    task_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity Decision ", related_name='decision_act')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_dec_act')
    created_at = models.DateTimeField(auto_now_add=True, null= True)   
    def __str__(self):
        return str(self.decision_name)
    




class Output_act(models.Model):
    output_name = models.CharField(max_length=270,verbose_name= u"Output title ",  null=True, blank=True)
    task_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity Output ", related_name='output_act')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_out_act')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.output_name) 






class Actor_act(models.Model):
    actor_name = models.CharField(max_length=270,verbose_name= u"Type or Name   ",help_text=u"User, ",  null=True, blank=True)
    task_id = models.ManyToManyField(Activity, verbose_name= u"Actor_proces  ", help_text=u" help text.", related_name='actor_act', blank=True) 
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_act_act')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        if self.actor_name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.actor_name)



class Input_act(models.Model):
    input_name = models.CharField(max_length=270,verbose_name= u"Input   ",  null=True, blank=True)
    task_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity Input ", related_name='ressource_act')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_input_act')
    created_at = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return str(self.input_name) 




class Skill_act(models.Model):
    skills_name = models.CharField(max_length=270,verbose_name= u"Skill title:  ",  null=True, blank=True)
    skills_maturity = models.CharField(max_length=270,verbose_name= u"Skill maturity :  ",  null=True, blank=True)
    
    task_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity  ", related_name='skill_act')    
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_skill_act')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.skills_name) 

    
class Technologie_act(models.Model):
    technologie_name = models.CharField(max_length=270,verbose_name= u"Technoly :  ",  null=True, blank=True)
    technology_maturity = models.CharField(max_length=270,verbose_name= u"Technology's maturity :  ",  null=True, blank=True)
    task_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=u"Activity ", related_name='tech_act')
    part = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name= u"Select Your University  ", related_name='parts_tech_act')
    autre =  models.CharField(max_length=270,verbose_name= u"if other partner ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return str(self.technologie_name)
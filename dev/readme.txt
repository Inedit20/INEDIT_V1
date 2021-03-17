%systemdrive%%homepath%\my-venv\Scripts\activate.bat


pip install django-admin-autocomplete-filter
pip install django-richtextfield

pip install django-ckeditor

pip install django-translations

pip install django-widget_tweaks

pip install django-filter

pip install pillow
pip install django-crispy-forms

pip install django-admin-autocomplete-filter
nnovationStory/Inedit

compl messages


python manage.py makemessages -l 'en'
python manage.py compilemessages
Django filter:
1. pip install django-admin-list-filter-dropdown

2. django_admin_listfilter_dropdown



def Research(request):
    template_name = 'Home/SearchItems/search.html'
    process_list = Process.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(process_list, 10)
    process_filter = ProcessFilter(request.GET, queryset = process_list)

    try:
        process_list = paginator.page(page)
    except PageNotAnInteger:
        process_list = paginator.page(1)
    except EmptyPage:
        process_list = paginator.page(paginator.num_pages)
    return render(request, template_name, {'filter' : process_filter, 'process_list': process_list})








{% if users.has_other_pages %}
  <ul class="pagination">
    {% if users.has_previous %}
      <li><a href="?page={{ users.previous_page_number }}">&laquo;</a></li>
    {% else %}
      <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    {% for i in users.paginator.page_range %}
      {% if users.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
      {% else %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if users.has_next %}
      <li><a href="?page={{ users.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
  </ul>
{% endif %}


    'crispy_forms',
    'djrichtextfield',
    'widget_tweaks',
    'translations',
    'ckeditor',
    'phone_field', 
    'admin_auto_filters',
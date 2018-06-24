from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import EmployeeForm


# Create your views here.


def employee_list(request):
    employees = Employee.objects.all().order_by("pk")
    # from the url, we grab the the first page
    # here, page = 1
    page = request.GET.get('page', 1)

    # this query is for the search function
    # grab the query from the URL
    query = request.GET.get("query")
    # if it exists
    if query:
        # search for the employee by name or job title or department
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(job_title__icontains=query) |
            Q(department__icontains=query)
            ).distinct()
    # django's built in paginator, wich will paginate employees, in pages of 15 instances
    paginator = Paginator(employees, 15)
    # we try and return a page 1 of paginated results
    try:
        workers = paginator.page(page)
        # if the variable page isnt an integer, we force to be '1'
    except PageNotAnInteger:
        workers = paginator.page(1)
    except EmptyPage:
        # if the contains no results, return a page with the total number of pages
        workers = paginator.page(paginator.num_pages)

    return render(request, 'employees/employee_list.html', {'workers':workers})



def save_employee_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # form_is_valid will tell us whether there are errors, and display the rror message on the screen
            data['form_is_valid'] = True
            employees = Employee.objects.all()
            # render_to_string loads a template and allows you to inject a context dictionary into it
            data['html_employee_list'] = render_to_string('employees/partial_employee_list.html', {
                'employees': employees
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    # the data dictionary we are passing to out ajax request holds the template, info on whether the form is valid, and the form itself
    data['html_form'] = render_to_string(template_name, context, request=request)
    # we are passing the form and validation in the data dictionary, which we pass back into the ajax request as a JSON object
    return JsonResponse(data)

# employee_create and employee_update recieve the request and prepare an instance of the form and pass it to save_employee_form


# this function is only responsible for rendering the form
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
        # we are sending back the employee form to save_employee_form above to save it to the backend
    return save_employee_form(request, form, 'employees/partial_employee_create.html')

# this function is only responsible for rendering the form
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        # render the prepopulated form
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'employees/partial_employee_update.html')


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    # if user is submitting the form
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = Employee.objects.all()
        # we delete the employee, then return the updated list, and inject it into the template
        data['html_employee_list'] = render_to_string('employees/partial_employee_list.html', {
            'employees': employees
        })
    else:
        # if useer isnt trying to submit the form, simply return the tempalte
        context = {'employee': employee}
        data['html_form'] = render_to_string('employees/partial_employee_delete.html',
            context,
            request=request,
        )
    # return the data as a JSON reponse to the ajax
    return JsonResponse(data)

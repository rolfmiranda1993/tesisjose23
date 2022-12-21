from member.models import StaffProfileD
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from member.forms import SI2  

def all_staff(request):
    def recursion(data, staff_no):
        new_child_list = []
        ro = data.filter(reporting_officer=staff_no)
        for j in ro:
            temp = {'staff_no': j.staff_no, 'staff_name': j.staff_name, 'designation': j.designation}
            temp['children'] = recursion(data, temp['staff_no'])
            if len(temp['children']) == 0:
                del temp['children']
            new_child_list.append(temp)
        return new_child_list

    data_list = StaffProfileD.objects.all()
    final_json = {}
    cs = data_list.get(designation='CS')
    final_json['staff_no'] = cs.staff_no
    final_json['staff_name'] = cs.staff_name
    final_json['designation'] = cs.designation
    final_json['children'] = recursion(data_list, final_json['staff_no'])
    return render(request, 'orgch2.html', {'a_staff': final_json})


def show_ch2(request):
    if request.method == "GET":
        form = SI2()
        return render(request, 'enter_staff2.html', {'form': form})

    if request.method == "POST":
        def recursion(data, staff_no):
            new_child_list = []
            ro = data.filter(reporting_officer=staff_no)
            for j in ro:
                temp = {'staff_no': j.staff_no, 'staff_name': j.staff_name, 'designation': j.designation}
                temp['children'] = recursion(data, temp['staff_no'])
                if len(temp['children']) == 0:
                    del temp['children']
                new_child_list.append(temp)
            return new_child_list

        data_list = StaffProfileD.objects.all()
        final_json = {}
        cs = data_list.get(designation='CS')
        final_json['staff_no'] = cs.staff_no
        final_json['staff_name'] = cs.staff_name
        final_json['designation'] = cs.designation
        #final_json['departamento'] = cs.departamento
        final_json['children'] = recursion(data_list, final_json['staff_no'])

        new_staff = request.POST['input_staff']
        if new_staff:
            if StaffProfileD.objects.filter(staff_no=new_staff).exists():
                return render(request, 'orgch2.html', {'a_staff': final_json, 'staff': new_staff})
            else:
                messages.warning(request, "Enter a valid staff no!")
                return redirect('/')
        else:
            messages.warning(request, "Please enter a staff no!")
            return redirect('/')


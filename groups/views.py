from django.shortcuts import render, redirect, get_object_or_404
from .models import Group


def home(request):
    return render(request, 'index.html')

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/list.html',ctx)


def group_form(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        group_type = request.POST.get('group_type')
        if   group and group_type:
            Group.objects.create(
                group = group,
                group_type = group_type,
            )
            return redirect('groups:list')
    return render(request, 'groups/form.html')

def group_detail(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    ctx = {'groups': groups}
    return render(request, 'groups/detail.html',ctx)

def group_delete(request,pk):
    groups = get_object_or_404(Group, pk=pk)
    groups.delete()
    return redirect('groups:list')



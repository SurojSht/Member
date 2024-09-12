from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm

# Create - Add a new member
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {'form': form})

# Read - List all members
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

# Update - Edit an existing member
def member_update(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/member_form.html', {'form': form})

# Delete - Delete a member
def member_delete(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/member_confirm_delete.html', {'member': member})


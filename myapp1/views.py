# mysite1/myapp1/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from .models import Contact
from .forms import ContactForm, ContactSearchForm

# Contacts: List + search
def contact_list(request):
    form = ContactSearchForm(request.GET or None)
    qs = Contact.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(email__icontains=q) |
                Q(profession__icontains=q) |
                Q(address__icontains=q) |
                Q(tel_number__icontains=q)
            )
    paginator = Paginator(qs, 10)  # 10 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "myapp1/contacts/contact_list.html", {
        "form": form,
        "page_obj": page_obj,
    })

# Create
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f"Contact “{contact.name}” created.")
            return redirect("contact_detail", pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, "myapp1/contacts/contact_form.html", {
        "form": form,
        "title": "Add Contact",
        "submit_label": "Create",
    })

# Read (detail)
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "myapp1/contacts/contact_detail.html", {"contact": contact})

# Update
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f"Contact “{contact.name}” updated.")
            return redirect("contact_detail", pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, "myapp1/contacts/contact_form.html", {
        "form": form,
        "title": "Edit Contact",
        "submit_label": "Save changes",
    })

# Delete
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        name = contact.name
        contact.delete()
        messages.success(request, f"Contact “{name}” deleted.")
        return redirect("contact_list")
    return render(request, "myapp1/contacts/contact_confirm_delete.html", {"contact": contact})
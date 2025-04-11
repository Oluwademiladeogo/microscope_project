from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SpecimenForm
from .models import Specimen


def index(request):
    if request.method == "POST":
        form = SpecimenForm(request.POST)
        if form.is_valid():
            specimen = form.save(commit=False)
            specimen.actual_size = specimen.calculate_actual_size()
            specimen.save()
            messages.success(
                request,
                f"Calculation successful! Actual size: {specimen.actual_size:.6f} μm",
            )
            return redirect("calculator:index")
    else:
        form = SpecimenForm()

    specimens = Specimen.objects.all().order_by("-created_at")
    return render(
        request, "calculator/index.html", {"form": form, "specimens": specimens}
    )

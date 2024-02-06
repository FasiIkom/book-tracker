from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Muhammad Firaz Al Aqib',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

# Create your views here.

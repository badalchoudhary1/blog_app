from django.shortcuts import render
from .models import Category
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


# Create your views here.
@csrf_exempt
def create_category(request):
    if  request.method == "POST":
        
        name = request.POST.get("name")
        if name:

            if (len(name) < 3):
                return render(request, "add_category.html", {"error": "Mimiman char required 3.", "value": name })
            if (len(name) > 20):
                return render(request, "add_category.html", {"error": "Maximum 10 char required.", "value": name })
            if (Category.objects.filter(name=name).exists()):
                return render(request, "add_category.html", {"error": "Category already exist", "value": name })
            
            Category.objects.create(name=name)
            return redirect("get_all_category")
        
        else:
            # Handle the case where 'name' is not provided
            return render(request, "add_category.html", {"error": "Category name is required."})
    else:
        return render(request, "add_category.html")

def get_all_category(request):
    categories =  Category.objects.all()
    print(categories, "categories")
    return render(request, "get_all_category.html", {"categories": categories, "link": "/shop/category/create" })

def delete_category(request,category_id):
   x = Category.objects.get(id=category_id)
   x.delete()
   return redirect("get_all_category")

def edit_category(request,category_id):
    db_category=Category.objects.get(id=category_id)

    if request.method == "POST":
        name=request.POST.get("name")
        db_category.name=name
        db_category.save()
        return render(request, 'edit_category.html', {"name": db_category.name, "message": "category update successfully"})
    else:
        return render(request, 'edit_category.html', {"name": db_category.name})


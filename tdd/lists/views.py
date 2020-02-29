from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here.

def home_page(request):
    ## 나중에 고친다!
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('lists/the-only-list-in-the-world/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    # request.POST 는 dict형태를 반환하지만 key값에 해당하는 value가 존재하지 않으면 KeyError을 발생시킴
    # 그렇게 때문에 request.POST.get을 사용 -> 존재하지 않을 경우 None 또는 default값을 두번재 인자로 설정 가능


def view_list(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'home.html', context)
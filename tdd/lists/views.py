from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')
    return render(request, 'home.html', {
        'new_item_text' : request.POST.get('item_text', ''), 
    })
    
    # request.POST 는 dict형태를 반환하지만 key값에 해당하는 value가 존재하지 않으면 KeyError을 발생시킴
    # 그렇게 때문에 request.POST.get을 사용 -> 존재하지 않을 경우 None 또는 default값을 두번재 인자로 설정 가능
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader

from food.forms import ItemForm
from food.models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # return HttpResponse(item_list)
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse("<h1>this is item page</h1>")


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context ={'item':item,}
    return render(request, 'food/detail.html', context)
    # return HttpResponse("This is item detail: id: %d" % item.id)


def create_item(request):
    form = ItemForm(request.POST or None)

    # 确保输入到表单中的数据是有效的
    if form.is_valid():
        # 保存数据到数据库
        form.save()
        return redirect('food:index')

    # 如果form无效或者是GET请求，则继续呈现这个html
    return render(request, 'food/item-form.html', {'form':form,})


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form, 'item':item, })

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item':item,})

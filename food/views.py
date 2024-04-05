from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from food.forms import ItemForm
from food.models import Item

# Create your views here.
# def index(request):
#     item_list = Item.objects.all()
#     # return HttpResponse(item_list)
#     # template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'food/index.html', context)


# 现在用django的class view来写，而不是用function写view
from django.views.generic.list import ListView


class IndexClassView(ListView):
    # 只需说明用的model是哪个，just need to clarify the model you are using
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse("<h1>this is item page</h1>")


# def detail(request, item_id):
#     item = Item.objects.get(id=item_id)
#     context = {'item': item, }
#     return render(request, 'food/detail.html', context)
#     # return HttpResponse("This is item detail: id: %d" % item.id)


from django.views.generic.detail import DetailView
class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    # context_object_name = 'item'


# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     # 确保输入到表单中的数据是有效的
#     if form.is_valid():
#         # 保存数据到数据库
#         form.save()
#         return redirect('food:index')
#
#     # 如果form无效或者是GET请求，则继续呈现这个html
#     return render(request, 'food/item-form.html', {'form':form,})


# this is a vlass based view for create item
from django.views.generic.edit import CreateView


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form, 'item': item, })


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item, })

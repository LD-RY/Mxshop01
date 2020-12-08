from django.views.generic import View
from goods.models import Goods

'''django的view实现商品列表页'''

# class GoodsListView(View):
#     def get(self,request):
#         #通过django的view实现商品列表页
#         json_list = []
#         #获取所有商品
#         goods = Goods.objects.all()
#         for good in goods:
#             json_dict = {}
#             #获取商品的每个字段，键值对形式
#             json_dict['name'] = good.name
#             json_dict['category'] = good.category.name
#             json_dict['market_price'] = good.market_price
#             json_list.append(json_dict)
#
#         from django.http import HttpResponse
#         import json
#         #返回json，一定要指定类型content_type='application/json'
#         return HttpResponse(json.dumps(json_list),content_type='application/json')


'''django的serializer序列化model,有个问题ImageFieldFile 和add_time字段不能序列化'''

# from django.views.generic import View
# from goods.models import Goods
#
# class GoodsListView(View):
#     def get(self,request):
#         #通过django的view实现商品列表页
#         json_list = []
#         #获取所有商品
#         goods = Goods.objects.all()
#         # for good in goods:
#         #     json_dict = {}
#         #     #获取商品的每个字段，键值对形式
#         #     json_dict['name'] = good.name
#         #     json_dict['category'] = good.category.name
#         #     json_dict['market_price'] = good.market_price
#         #     json_list.append(json_dict)
#
#         from django.forms.models import model_to_dict
#         for good in goods:
#             json_dict = model_to_dict(good)
#             json_list.append(json_dict)
#
#         from django.http import HttpResponse
#         import json
#         #返回json，一定要指定类型content_type='application/json'
#         return HttpResponse(json.dumps(json_list),content_type='application/json')


'''将所有字段序列化就要用到django的serializers
    字段序列化定死的，要想重组的话非常麻烦
    images保存的是一个相对路径，我们还需要补全路径，而这些drf都可以帮助我们做到
'''

from django.views.generic import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        #通过django的view实现商品列表页
        json_list = []
        #获取所有商品
        goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     #获取商品的每个字段，键值对形式
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        #In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(json_data,safe=False)
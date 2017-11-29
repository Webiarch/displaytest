import os
from biba.environ import *
from django.shortcuts import render
from bigcommerce.api import BigcommerceApi
from django.views import View
from .models import *

os.environ['APP_CLIENT_SECRET'] = 'oam9jfaj4n7olb6gnxetiza5jozt83h'

# api = bigcommerce.api.BigcommerceApi(
#     client_id='hrc4ek4ze2p77enpe08dq56plmdz6z8',
#     store_hash='d2mevog548',
#     access_token='tqmm1s7dvi36mrmqie7yihagrj24owp')


class Display(View):

    template = "display.html"

    def get(self, request):
        # customer = api.Customers.all(email='gabaniromit4892@gmail.com')[0]
        # login_token = bigcommerce.customer_login_token.create(api, customer.id)
        # print('%s/login/token/%s' % ('http://localhost:8000', login_token))

        return render(request, self.template, locals())


class AuthCallback(View):

    def get(self, request):
        # code = request.args['code']
        # context = request.args['context']
        # scope = request.args['scope']
        # store_hash = context.split('/')[1]
        # redirect = APP_URL + '/bigcommerce/callback'
        #
        # client = BigcommerceApi(client_id=APP_CLIENT_ID, store_hash=store_hash)
        # token = client.oauth_fetch_token(APP_CLIENT_SECRET, code, context, scope, redirect)
        # bc_user_id = token['user']['id']
        # email = token['user']['email']
        # access_token = token['access_token']
        #
        # store = Store.objects.get(store_hash=store_hash).first()
        # if store is None:
        #     store = Store.create(store_hash, access_token, scope)
        # else:
        #     store.update(
        #         access_token=access_token,
        #         scope=scope,
        #     )
        #
        # user = User.objects.get(bc_id=bc_user_id).first()
        # if user is None:
        #     user = User.create(
        #         bc_id=bc_user_id,
        #         email=email,
        #     )
        # elif user.email != email:
        #     User.update(
        #         email=email,
        #     )
        #
        # storeuser = StoreUser.objects.get(
        #     user_id=user.id,
        #     store_id=store.id,
        # ).first()
        #
        # if not storeuser:
        #     storeuser = StoreUser.create(store, user, admin=True)
        # else:
        #     StoreUser.update(admin=True)
        pass
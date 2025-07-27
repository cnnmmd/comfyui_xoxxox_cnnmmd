#---------------------------------------------------------------------------

import aiohttp

#---------------------------------------------------------------------------

class MidClt:

  # 定数
  adrini = "/ini" # ルート：初期
  adrset = "/set" # ルート：格納
  adrget = "/get" # ルート：取得
  adrprc = "/prc" # ルート：処理
  adrspp = "/spp" # ルート：格納の引出
  adrgps = "/gps" # ルート：取得の差込

  # 格納：内容を送信〜辞書を受信
  @staticmethod
  async def reqset(datreq, adrreq):
    async with aiohttp.ClientSession() as sssweb:
      async with sssweb.post(adrreq, data=datreq) as datres:
        dicres = await datres.json()
        return dicres

  # 取得：辞書を送信〜内容を受信
  @staticmethod
  async def reqget(datreq, adrreq):
    async with aiohttp.ClientSession() as sssweb:
      async with sssweb.post(adrreq, json=datreq) as datres:
        rawres = await datres.read()
        return rawres

  # 処理：辞書を送信〜辞書を受信
  @staticmethod
  async def reqprc(datreq, adrreq):
    async with aiohttp.ClientSession() as sssweb:
      async with sssweb.post(adrreq, json=datreq) as datres:
        dicres = await datres.json()
        return dicres

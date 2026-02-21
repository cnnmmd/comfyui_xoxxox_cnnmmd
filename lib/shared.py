#---------------------------------------------------------------------------

import os
import json
import asyncio
import threading
from .midclt import MidClt
from .params_cmf import PrmCmf

#---------------------------------------------------------------------------
# 設定の取得

class PrcCmf:

  dictip = {}
  dicsrv = {}
  diccmf = {}

  # gettip()

  @classmethod
  def gettip(cls):
    dirtop = os.path.dirname(__file__)
    pthtip = os.path.join(dirtop, "params_tip.json")
    with open(pthtip, "r") as f:
      dictip = json.load(f)
    return dictip

  # getsrv()

  @classmethod
  def getsrv(cls):
    t = threading.Thread(target=cls.wrksrv)
    t.start()
    t.join()
    return cls.dicsrv

  @classmethod
  def wrksrv(cls):
    cls.dicsrv = asyncio.run(cls.asysrv())

  @classmethod
  async def asysrv(cls):
    adrmid = PrmCmf.adrmid
    datreq = {"keyprc": "xoxxox.AppCmf.dicsrv"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    datres = await MidClt.reqget({"keymmd": datres["keymmd"]}, adrmid + MidClt.adrget)
    dicsrv = json.loads(datres.decode("utf-8"))
    return dicsrv

  # getcmf()

  @classmethod
  def getcmf(cls):
    t = threading.Thread(target=cls.wrkcmf)
    t.start()
    t.join()
    return cls.diccmf

  @classmethod
  def wrkcmf(cls):
    cls.diccmf = asyncio.run(cls.asycmf())

  @classmethod
  async def asycmf(cls):
    adrmid = PrmCmf.adrmid
    datreq = {"keyprc": "xoxxox.AppCmf.diccmf"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    datres = await MidClt.reqget({"keymmd": datres["keymmd"]}, adrmid + MidClt.adrget)
    diccmf = json.loads(datres.decode("utf-8"))
    return diccmf

#---------------------------------------------------------------------------

import json
import numpy as np
from PIL import Image
import asyncio
import torch
from .midclt import MidClt
from .params_cmf import PrmCmf

#---------------------------------------------------------------------------
# 設定の取得

class PrcCmf:

  @staticmethod
  def getsrv():
    adrmid = PrmCmf.adrmid
    datreq = {"keyprc": "xoxxox.AppCmf.dicsrv"}
    datres = asyncio.run(MidClt.reqprc(datreq, adrmid + MidClt.adrprc))
    datres = asyncio.run(MidClt.reqget({"keydat": datres["keydat"]}, adrmid + MidClt.adrget))
    dicsrv = json.loads(datres.decode("utf-8"))
    return dicsrv

  @staticmethod
  def getcmf():
    adrmid = PrmCmf.adrmid
    datreq = {"keyprc": "xoxxox.AppCmf.diccmf"}
    datres = asyncio.run(MidClt.reqprc(datreq, adrmid + MidClt.adrprc))
    datres = asyncio.run(MidClt.reqget({"keydat": datres["keydat"]}, adrmid + MidClt.adrget))
    diccmf = json.loads(datres.decode("utf-8"))
    return diccmf

#---------------------------------------------------------------------------
# 画像の変換

class CnvImg:

  # HWC (256) -> HWC (0-1)
  @staticmethod
  def cnvtsr(imgpil):
    g = np.array(imgpil).astype(np.float32) / 255.0
    imgtsr = torch.from_numpy(g)
    return imgtsr

  # HWC (0-1) -> HWC (256)
  @staticmethod
  def cnvpil(imgtsr):
    g = imgtsr.cpu().numpy() * 255.0
    g = np.clip(g, 0, 255).astype(np.uint8)
    imgpil = Image.fromarray(g)
    return imgpil

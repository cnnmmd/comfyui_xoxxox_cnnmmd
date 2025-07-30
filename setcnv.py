#---------------------------------------------------------------------------

import asyncio
import threading
from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid
diccnf = {}
async def getdic():
  return await PrcCmf.getcmf()
def worker():
  global diccnf
  diccnf = asyncio.run(getdic())
t = threading.Thread(target=worker)
t.start()
t.join()

#---------------------------------------------------------------------------
# データを変換

class Xoxxox_CnvDat:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "method": (diccnf["lstcnv_dat"], {"default": diccnf["defcnv_dat"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcnv"

  async def anchor(self, keydat, method):
    datreq = {"status": "0", "keydat": keydat, "keyprc": method}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

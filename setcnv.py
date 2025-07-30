#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid
diccnf = {}
async def getdic():
  global diccnf
  diccnf = await PrcCmf.getcnf()
getdic()

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

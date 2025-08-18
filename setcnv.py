#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid
diccnf = PrcCmf.getcmf()

#---------------------------------------------------------------------------
# データを変換

class CnvDat:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["CnvDat.keydat"]}),
        "method": (diccnf["lstcnv_dat"], {"default": diccnf["defcnv_dat"], "tooltip": dictip["CnvDat.method"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcnv"

  async def anchor(self, keydat, method):
    datreq = {"status": "0", "keydat": keydat, "keyprc": method}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

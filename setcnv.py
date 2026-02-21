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
        "keymmd": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["CnvDat.keymmd"]}),
        "method": (diccnf["lstcnv_dat"], {"default": diccnf["defcnv_dat"], "tooltip": dictip["CnvDat.method"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcnv"

  async def anchor(self, keymmd, method):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": method}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

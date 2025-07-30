#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid

#---------------------------------------------------------------------------
# メモリに格納

class Xoxxox_SetMem:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "keymem": ("STRING", {"default": "mem000"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keydat, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.setmem", "keydat": keydat, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    return ("",)

#---------------------------------------------------------------------------
# メモリを参照

class Xoxxox_GetMem:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "keymem": ("STRING", {"default": "mem000"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keydat, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.getmem", "keydat": keydat, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

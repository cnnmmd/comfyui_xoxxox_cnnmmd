#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid

#---------------------------------------------------------------------------
# メモリに格納

class SetMem:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetMem.keydat"]}),
        "keymem": ("STRING", {"default": "mem000", "tooltip": dictip["SetMem.keymem"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keydat, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.setmem", "keydat": keydat, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# メモリを参照

class GetMem:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetMem.keydat"]}),
        "keymem": ("STRING", {"default": "mem000", "tooltip": dictip["GetMem.keymem"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keydat, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.getmem", "keydat": keydat, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

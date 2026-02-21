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
        "keymmd": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetMem.keymmd"]}),
        "keymem": ("STRING", {"default": "mem000", "tooltip": dictip["SetMem.keymem"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keymmd, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.setmem", "keymmd": keymmd, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

#---------------------------------------------------------------------------
# メモリを参照

class GetMem:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetMem.keymmd"]}),
        "keymem": ("STRING", {"default": "mem000", "tooltip": dictip["GetMem.keymem"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmem"

  async def anchor(self, keymmd, keymem):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeMem.getmem", "keymmd": keymmd, "keymem": keymem}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

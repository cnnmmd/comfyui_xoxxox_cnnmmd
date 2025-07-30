#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid

#---------------------------------------------------------------------------
# ファイルに格納

class Xoxxox_SetDir:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "target": ("STRING", {"default": "/opt/strage/sample_001.bin"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, keydat, target):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.OpeBlb.setdir", "target": target}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    return ("",)

#---------------------------------------------------------------------------
# ファイルを参照

class Xoxxox_GetDir:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "target": ("STRING", {"default": "/opt/common/web/xoxxox/doc/sample_001.bin"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, string, target):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeBlb.getdir", "target": target}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# ファイルに格納（キーを元に）

class Xoxxox_SetDis:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "folder": ("STRING", {"default": "/opt/strage"}),
        "extdat": ("STRING", {"default": ".txt"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, keydat, extdat, folder):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.OpeBlb.setdis", "extdat": extdat, "folder": folder}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    return ("",)

#---------------------------------------------------------------------------
# ファイルを参照（複数、順次）

class Xoxxox_GetDis:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "folder": ("STRING", {"default": "/opt/common/web/xoxxox/doc"}),
        "extdat": ("STRING", {"default": ".txt"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, string, folder, extdat):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeBlb.getdis", "extdat": extdat, "folder": folder}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid

#---------------------------------------------------------------------------
# ファイルに格納

class SetDir:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetDir.keydat"]}),
        "target": ("STRING", {"default": "/opt/strage/sample_001.bin", "tooltip": dictip["SetDir.target"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, keydat, target):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.OpeBlb.setdir", "target": target}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    return ("",)

#---------------------------------------------------------------------------
# ファイルを参照

class GetDir:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetDir.string"]}),
        "target": ("STRING", {"default": "/opt/common/web/xoxxox/doc/sample_001.bin", "tooltip": dictip["GetDir.target"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, string, target):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeBlb.getdir", "target": target}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# ファイルに格納（キーを元に）

class SetDis:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetDis.keydat"]}),
        "folder": ("STRING", {"default": "/opt/strage", "tooltip": dictip["SetDis.folder"]}),
        "extdat": ("STRING", {"default": ".txt", "tooltip": dictip["SetDis.extdat"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, keydat, extdat, folder):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.OpeBlb.setdis", "extdat": extdat, "folder": folder}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    return ("",)

#---------------------------------------------------------------------------
# ファイルを参照（複数、順次）

class GetDis:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetDis.string"]}),
        "folder": ("STRING", {"default": "/opt/common/web/xoxxox/doc", "tooltip": dictip["GetDis.folder"]}),
        "extdat": ("STRING", {"default": ".txt", "tooltip": dictip["GetDis.extdat"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setblb"

  async def anchor(self, string, folder, extdat):
    datreq = {"status": "0", "keyprc": "xoxxox.OpeBlb.getdis", "extdat": extdat, "folder": folder}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

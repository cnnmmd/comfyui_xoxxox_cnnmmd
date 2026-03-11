#---------------------------------------------------------------------------
# 参照

from PIL import Image
import torch
from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf
from .lib.shared_img import CnvImg

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid
dicsrv = PrcCmf.getsrv()
diccnf = PrcCmf.getcmf()

#---------------------------------------------------------------------------
# 変換（テキストの一部を指定の文字列で置換する）

class RepTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtbdy": ("STRING", {"forceInput": True, "multiline": True, "tooltip": dictip["RepTxt.txtbdy"]}),
        "txtmod": ("STRING", {"forceInput": True, "multiline": True, "tooltip": dictip["RepTxt.txtmod"]}),
        "txtorg": ("STRING", {"forceInput": False, "multiline": False, "default": "<s>", "tooltip": dictip["RepTxt.txtorg"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setetc"

  def anchor(self, txtbdy, txtmod, txtorg):
    txtres = txtbdy.replace(txtorg, txtmod)
    return (txtres,)

#---------------------------------------------------------------------------
# 変換（本体の画像とそのマスクを受け取り、透過画像を生成する）

class TrnBak:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "tsrimg": ("IMAGE",{"tooltip": dictip["TrnBak.tsrimg"]}),
        "tsrmsk": ("MASK",{"tooltip": dictip["TrnBak.tsrmsk"]}),
      },
    }
  RETURN_TYPES = ("IMAGE",)
  RETURN_NAMES = ("tsrimg",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setetc"

  def anchor(self, tsrimg, tsrmsk):
    lstimg = []

    for (i, m) in enumerate(tsrimg):
      pilimg = CnvImg.cnvpil(tsrimg[i])
      pilmsk = CnvImg.cnvpil(tsrmsk[i])
      r, g, b = pilimg.split()
      pilcmp = Image.merge("RGBA", (r, g, b, pilmsk))
      lstimg.append(CnvImg.cnvtsr(pilcmp)[None,])
    tsrimg = torch.cat(lstimg)
    return (tsrimg,)

#---------------------------------------------------------------------------
# 各種のプログミング言語を実行する

class PrcPrc:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lstprc_nod"], {"default": diccnf["defprc_nod"]}),
        "config": (diccnf["lstprc_cnf"], {"default": diccnf["defprc_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING", "STRING")
  RETURN_NAMES = ("keymmd", "keyerr")
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setetc"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcPrc.cnnprc", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["key000"]
    keyerr = datres["key001"]
    return (keymmd, keyerr)

#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid
dicsrv = PrcCmf.getsrv()
diccnf = PrcCmf.getcmf()

#---------------------------------------------------------------------------
# 画像を生成

class GenImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GenImg.keydat"]}),
        "keyneg": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GenImg.keyneg"]}),
        "server": (diccnf["lstimg_nod"], {"default": diccnf["defimg_nod"], "tooltip": dictip["GenImg.server"]}),
        "config": (diccnf["lstimg_cnf"], {"default": diccnf["defimg_cnf"], "tooltip": dictip["GenImg.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setimg"

  async def anchor(self, keydat, keyneg, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyneg": keyneg, "keyprc": "xoxxox.PrcImg.cnnimg", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

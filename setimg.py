#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid
async def getdic():
  dicsrv = await PrcCmf.getsrv()
  diccnf = await PrcCmf.getcnf()
  return (dicsrv, diccnf)
dicsrv, diccnf = getdic()

#---------------------------------------------------------------------------
# 画像を生成

class Xoxxox_GenImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "keyneg": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lstimg_nod"], {"default": diccnf["defimg_nod"]}),
        "config": (diccnf["lstimg_cnf"], {"default": diccnf["defimg_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setimg"

  async def anchor(self, keydat, keyneg, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyneg": keyneg, "keyprc": "xoxxox.PrcImg.cnnimg", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

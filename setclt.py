from server import PromptServer
from .lib.shared import PrcCmf
from .lib.params_tlk import PrmVce, PrmSwt

#---------------------------------------------------------------------------

dicsrv = PrcCmf.getsrv()

#---------------------------------------------------------------------------
# サウンドを送信（フロントエンド（ウェブブラウザ）から）

class Xoxxox_SndVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid}),
        "pthsnd": ("STRING", {"default": PrmVce.pthsnd}),
        "thdvce": ("FLOAT", {"default": 0.05}),
        "mscend": ("INT", {"default": 2000}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setclt"

  def anchor(self, string, srvmid, pthsnd, thdvce, mscend):
    adrsnd = dicsrv[srvmid] + pthsnd
    PromptServer.instance.send_sync("xoxxox_sndvce", {"adrsnd": adrsnd, "thdvce": thdvce, "mscend": mscend})
    return ("",)

#---------------------------------------------------------------------------
# サウンドを受信（フロントエンド（ウェブブラウザ）で）

class Xoxxox_RcvVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid}),
        "pthrcv": ("STRING", {"default": PrmVce.pthrcv}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setclt"

  def anchor(self, string, srvmid, pthrcv):
    adrrcv = dicsrv[srvmid] + pthrcv
    PromptServer.instance.send_sync("xoxxox_rcvvce", {"adrrcv": adrrcv})
    return ("",)

#---------------------------------------------------------------------------
# サウンドを受信〜イメージを切替（フロントエンド（ウェブブラウザ）で）

class Xoxxox_SwtImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid}),
        "srvweb": ("STRING", {"default": PrmSwt.srvweb}),
        "pthrcv": ("STRING", {"default": PrmVce.pthrcv}),
        "thdvce": ("FLOAT", {"default": 0.05}),
        "pthswc": ("STRING", {"default": PrmSwt.pthswc}),
        "adrchr": ("STRING", {"default": PrmSwt.adrchr}),
        "imgchr": ("STRING", {"default": PrmSwt.imgchr}),
        "arrimg": ("STRING", {"default": "r"}),
        "sclimg": ("FLOAT", {"default": 0.25}),
        "poscox": ("FLOAT", {"default": 0.25}),
        "poscoy": ("FLOAT", {"default": 0.00}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setclt"

  def anchor(self, string, srvmid, srvweb, pthrcv, thdvce, pthswc, adrchr, imgchr, arrimg, sclimg, poscox, poscoy):
    adrrcv = dicsrv[srvmid] + pthrcv
    adrswc = ""
    if pthswc != "":
      adrswc = dicsrv[srvmid] + pthswc
    adrchr = dicsrv[srvweb] + adrchr
    PromptServer.instance.send_sync("xoxxox_swtimg", {"adrrcv": adrrcv, "thdvce": thdvce, "adrswc": adrswc, "adrchr": adrchr, "imgchr": imgchr, "arrimg": arrimg, "sclimg": sclimg, "poscox": poscox, "poscoy": poscoy})
    return ("",)

#---------------------------------------------------------------------------

from server import PromptServer
from .lib.shared import PrcCmf
from .lib.params_tlk import PrmVce, PrmSwt

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
dicsrv = PrcCmf.getsrv()

#---------------------------------------------------------------------------
# サウンドを送信（フロントエンド（ウェブブラウザ）から）

class SndVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SndVce.string"]}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid, "tooltip": dictip["SndVce.srvmid"]}),
        "pthsnd": ("STRING", {"default": PrmVce.pthsnd, "tooltip": dictip["SndVce.pthsnd"]}),
        "thdvce": ("FLOAT", {"default": 0.05, "tooltip": dictip["SndVce.thdvce"]}),
        "mscend": ("INT", {"default": 2000, "tooltip": dictip["SndVce.mscend"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setclt"

  def anchor(self, string, srvmid, pthsnd, thdvce, mscend):
    adrsnd = dicsrv[srvmid] + pthsnd
    PromptServer.instance.send_sync("xoxxox_sndvce", {"adrsnd": adrsnd, "thdvce": thdvce, "mscend": mscend})
    return ("",)

#---------------------------------------------------------------------------
# サウンドを受信（フロントエンド（ウェブブラウザ）で）

class RcvVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["RcvVce.string"]}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid, "tooltip": dictip["RcvVce.srvmid"]}),
        "pthrcv": ("STRING", {"default": PrmVce.pthrcv, "tooltip": dictip["RcvVce.pthrcv"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setclt"

  def anchor(self, string, srvmid, pthrcv):
    adrrcv = dicsrv[srvmid] + pthrcv
    PromptServer.instance.send_sync("xoxxox_rcvvce", {"adrrcv": adrrcv})
    return ("",)

#---------------------------------------------------------------------------
# サウンドを受信〜イメージを切替（フロントエンド（ウェブブラウザ）で）

class SwtImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SwtImg.string"]}),
        "srvmid": ("STRING", {"default": PrmVce.srvmid, "tooltip": dictip["SwtImg.srvmid"]}),
        "srvweb": ("STRING", {"default": PrmSwt.srvweb, "tooltip": dictip["SwtImg.srvweb"]}),
        "pthrcv": ("STRING", {"default": PrmVce.pthrcv, "tooltip": dictip["SwtImg.pthrcv"]}),
        "thdvce": ("FLOAT", {"default": 0.05, "tooltip": dictip["SwtImg.thdvce"]}),
        "pthswc": ("STRING", {"default": PrmSwt.pthswc, "tooltip": dictip["SwtImg.pthswc"]}),
        "adrchr": ("STRING", {"default": PrmSwt.adrchr, "tooltip": dictip["SwtImg.adrchr"]}),
        "imgchr": ("STRING", {"default": PrmSwt.imgchr, "tooltip": dictip["SwtImg.imgchr"]}),
        "arrimg": ("STRING", {"default": "r", "tooltip": dictip["SwtImg.arrimg"]}),
        "sclimg": ("FLOAT", {"default": 0.25, "tooltip": dictip["SwtImg.sclimg"]}),
        "poscox": ("FLOAT", {"default": 0.25, "tooltip": dictip["SwtImg.poscox"]}),
        "poscoy": ("FLOAT", {"default": 0.00, "tooltip": dictip["SwtImg.poscoy"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
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

#---------------------------------------------------------------------------

import io
from PIL import Image
import torch
import torchaudio
from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.shared_img import CnvImg
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()
adrmid = PrmCmf.adrmid

#---------------------------------------------------------------------------
# 初期

class IniFlw:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {},
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  @classmethod
  def IS_CHANGED(s):
    return float("nan")

  async def anchor(self):
    datreq = {"status": "0"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrini)
    return ("",)

#---------------------------------------------------------------------------
# 空文字を格納（空データを作る）

class SetNil:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetNil.string"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, string):
    datreq = "" # ウェブ経由でアップロードする際、バイト列に変換される（不要：b"" ）
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 文字列を入力

class PutTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["PutTxt.string"]}),
        "txtreq": ("STRING", {"default": "", "multiline": True, "tooltip": dictip["PutTxt.txtreq"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  def anchor(self, string, txtreq):
    txtres = txtreq
    return (txtres,)

#---------------------------------------------------------------------------
# 文字列を格納

class SetTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtreq": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SetTxt.txtreq"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, txtreq):
    datreq = txtreq
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 文字列を取得

class GetTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetTxt.keydat"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat):
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqget(datreq, adrmid + MidClt.adrget)
    txtres = datres.decode("utf-8")
    return (txtres,)

#---------------------------------------------------------------------------
# 画像を格納

class SetImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "imgtsr": ("IMAGE",{"tooltip": dictip["SetImg.imgtsr"]})
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, imgtsr):
    buffer = io.BytesIO()
    imgpil = CnvImg.cnvpil(imgtsr[0])
    imgpil.save(buffer, format="PNG")
    datreq = buffer.getvalue()
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 画像を取得

class GetImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetImg.keydat"]}),
      },
    }
  RETURN_TYPES = ("IMAGE",)
  RETURN_NAMES = ("tsrimg",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat):
    lstimg = []
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqget(datreq, adrmid + MidClt.adrget)
    buffer = io.BytesIO(datres)
    imgpil = Image.open(buffer)
    lstimg.append(CnvImg.cnvtsr(imgpil)[None,])
    tsrimg = torch.cat(lstimg)
    return (tsrimg,)

#---------------------------------------------------------------------------
# 音声を格納

class SetAud:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "dicwav": ("AUDIO",{"tooltip": dictip["SetAud.dicwav"]})
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, dicwav):
    frmwav = dicwav["waveform"].squeeze(0)
    ratsmp = dicwav["sample_rate"]
    buffer = io.BytesIO()
    torchaudio.save(buffer, frmwav, ratsmp, format="wav")
    datreq = buffer.getvalue()
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 音声を取得

class GetAud:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GetAud.keydat"]}),
      },
    }
  RETURN_TYPES = ("AUDIO",)
  RETURN_NAMES = ("dicwav",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat):

    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqget(datreq, adrmid + MidClt.adrget)
    buffer = io.BytesIO(datres)
    frmwav, ratsmp = torchaudio.load(buffer)
    dicwav = {
        "waveform": frmwav.unsqueeze(0),
        "sample_rate": ratsmp
    }
    return (dicwav,)

#---------------------------------------------------------------------------
# データＩＤを引き渡し／準備ができたら（/sppNNN ）……対になる処理：ローデータを受け取り／受信完了を通知（/spsNNN ）

class DlySet:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["DlySet.string"]}),
        "keyset": ("STRING", {"default": "000", "tooltip": dictip["DlyGet.keyget"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, string, keyset):
    datreq = {"status": "0"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrspp + keyset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# データＩＤを受け取り／受信完了を通知（/gpsNNN ）……対になる処理：ローデータを引き渡し／準備ができたら（/gppNNN ）

class DlyGet:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["DlyGet.keydat"]}),
        "keyget": ("STRING", {"default": "000", "tooltip": dictip["DlyGet.keyget"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("string",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat, keyget):
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrgps + keyget)
    return ("",)

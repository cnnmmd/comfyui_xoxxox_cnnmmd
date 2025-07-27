#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

adrmid = PrmCmf.adrmid
dicsrv = PrcCmf.getsrv()
diccnf = PrcCmf.getcmf()

#---------------------------------------------------------------------------
# 初期

class Xoxxox_IniFlw:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "random": ("INT", {"forceInput": True}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, random):
    datreq = {"status": "0"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrini)
    return ("",)

#---------------------------------------------------------------------------
# 空文字を格納（空データを作る）

class Xoxxox_SetNil:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, string):
    datreq = "" # ウェブ経由でアップロードする際、バイト列に変換される（不要：b"" ）
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 文字列を入力

class Xoxxox_PutTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "txtreq": ("STRING", {"default": "", "multiline": True}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  def anchor(self, string, txtreq):
    return (txtreq,)

#---------------------------------------------------------------------------
# 文字列を格納

class Xoxxox_SetTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtreq": ("STRING", {"default": "", "forceInput": True}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, txtreq):
    datreq = txtreq
    datres = await MidClt.reqset(datreq, adrmid + MidClt.adrset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 文字列を取得

class Xoxxox_GetTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat):
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqget(datreq, adrmid + MidClt.adrget)
    txtres = datres.decode("utf-8")
    return (txtres,)

#---------------------------------------------------------------------------
# 画像を格納

class Xoxxox_SetImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "imgtsr": ("IMAGE",)
      },
    }
  RETURN_TYPES = ("STRING",)
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

class Xoxxox_GetImg:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
      },
    }
  RETURN_TYPES = ("IMAGE",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat):
    lstimg = []
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqget(datreq, adrmid + MidClt.adrget)
    buffer = io.BytesIO(datres)
    imgpil = Image.open(buffer)
    lstimg.append(CnvImg.cnvtsr(imgpil)[None,])
    lsttsr = torch.cat(lstimg)
    return (lsttsr,)

#---------------------------------------------------------------------------
# 音声を格納

class Xoxxox_SetAud:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "dicwav": ("AUDIO",)
      },
    }
  RETURN_TYPES = ("STRING",)
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

class Xoxxox_GetAud:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
      },
    }
  RETURN_TYPES = ("AUDIO",)
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

class Xoxxox_DlySet:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True}),
        "keyset": ("STRING", {"default": "000"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, string, keyset):
    datreq = {"status": "0"}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrspp + keyset)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# データＩＤを受け取り／受信完了を通知（/gpsNNN ）……対になる処理：ローデータを引き渡し／準備ができたら（/gppNNN ）

class Xoxxox_DlyGet:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True}),
        "keyget": ("STRING", {"default": "000"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setmid"

  async def anchor(self, keydat, keyget):
    datreq = {"status": "0", "keydat": keydat}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrgps + keyget)
    return ("",)

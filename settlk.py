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
# サウンドからテキストに変換（ＳＴＴ）

class CnvTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["CnvTxt.keydat"]}),
        "server": (diccnf["lststt_nod"], {"default": diccnf["defstt_nod"], "tooltip": dictip["CnvTxt.server"]}),
        "config": (diccnf["lststt_cnf"], {"default": diccnf["defstt_cnf"], "tooltip": dictip["CnvTxt.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keydat, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.PrcStt.cnnstt", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# テキストからサウンドに変換（ＴＴＳ）

class CnvVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["CnvVce.keydat"]}),
        "server": (diccnf["lsttts_nod"], {"default": diccnf["deftts_nod"], "tooltip": dictip["CnvVce.server"]}),
        "config": (diccnf["lsttts_cnf"], {"default": diccnf["deftts_cnf"], "tooltip": dictip["CnvVce.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keydat, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.PrcTts.cnntts", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# テキストからテキストを生成（ＬＬＭ）

class GenTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GenTxt.keydat"]}),
        "server": (diccnf["lstttt_nod"], {"default": diccnf["defttt_nod"], "tooltip": dictip["GenTxt.server"]}),
        "config": (diccnf["lstttt_cnf"], {"default": diccnf["defttt_cnf"], "tooltip": dictip["GenTxt.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keydat, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.PrcTtt.cnnttt", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# テキストからテキストを生成（ＬＬＭ）：オプションあり

class GenTxt_Opt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["GenTxt.keydat"]}),
        "server": (diccnf["lstttt_nod"], {"default": diccnf["defttt_nod"], "tooltip": dictip["GenTxt.server"]}),
        "config": (diccnf["lstttt_cnf"], {"default": diccnf["defttt_cnf"], "tooltip": dictip["GenTxt.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat", "keyopt")
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keydat, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.PrcTtt_Opt.cnnttt", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    keyopt = datres["key001"]
    return (keydat, keyopt)

#---------------------------------------------------------------------------
# サウンドからテキストに変換（感情分析）

class CnvSen:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keydat": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["CnvSen.keydat"]}),
        "server": (diccnf["lstsen_nod"], {"default": diccnf["defsen_nod"], "tooltip": dictip["CnvSen.server"]}),
        "config": (diccnf["lstsen_cnf"], {"default": diccnf["defsen_cnf"], "tooltip": dictip["CnvSen.config"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keydat",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keydat, server, config):
    datreq = {"status": "0", "keydat": keydat, "keyprc": "xoxxox.PrcSen.cnnsen", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keydat = datres["keydat"]
    return (keydat,)

#---------------------------------------------------------------------------
# 感情分析（テキスト〜テキスト）
# 0: 喜び/joy
# 1: 悲嘆/sadness
# 2: 期待/anticipation
# 3: 驚き/surprise
# 4: 怒り/anger
# 5: 恐れ/fear
# 6: 嫌悪/disgust
# 7: 信頼/trust

class SenTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtreq": ("STRING", {"forceInput": True, "tooltip": dictip["SenTxt.txtreq"]}),
        "sen000": ("STRING", {"forceInput": False, "multiline": False, "default": "joy", "tooltip": dictip["SenTxt.sen000"]}),
        "sen001": ("STRING", {"forceInput": False, "multiline": False, "default": "sadness", "tooltip": dictip["SenTxt.sen001"]}),
        "sen002": ("STRING", {"forceInput": False, "multiline": False, "default": "anticipation", "tooltip": dictip["SenTxt.sen002"]}),
        "sen003": ("STRING", {"forceInput": False, "multiline": False, "default": "surprise", "tooltip": dictip["SenTxt.sen003"]}),
        "sen004": ("STRING", {"forceInput": False, "multiline": False, "default": "anger", "tooltip": dictip["SenTxt.sen004"]}),
        "sen005": ("STRING", {"forceInput": False, "multiline": False, "default": "fear", "tooltip": dictip["SenTxt.sen005"]}),
        "sen006": ("STRING", {"forceInput": False, "multiline": False, "default": "disgust", "tooltip": dictip["SenTxt.sen006"]}),
        "sen007": ("STRING", {"forceInput": False, "multiline": False, "default": "trust", "tooltip": dictip["SenTxt.sen007"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  def anchor(self, txtreq, sen000, sen001, sen002, sen003, sen004, sen005, sen006, sen007):
    if txtreq   == "0":
      txtres = sen000
    elif txtreq == "1":
      txtres = sen001
    elif txtreq == "2":
      txtres = sen002
    elif txtreq == "3":
      txtres = sen003
    elif txtreq == "4":
      txtres = sen004
    elif txtreq == "5":
      txtres = sen005
    elif txtreq == "6":
      txtres = sen006
    elif txtreq == "7":
      txtres = sen007
    return (txtres,)

#---------------------------------------------------------------------------
# 感情分析（セレクタ〜テキスト）

class SenSlc:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"default": "", "forceInput": True, "tooltip": dictip["SenSlc.string"]}),
        "select": (["0", "1", "2", "3", "4", "5", "6", "7"], {"default": "0", "tooltip": dictip["SenSlc.select"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, string, select):
    return (select,)

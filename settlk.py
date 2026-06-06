#---------------------------------------------------------------------------

from .lib.midclt import MidClt
from .lib.shared import PrcCmf
from .lib.params_cmf import PrmCmf

#---------------------------------------------------------------------------

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
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lststt_nod"], {"default": diccnf["defstt_nod"]}),
        "config": (diccnf["lststt_cnf"], {"default": diccnf["defstt_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcStt.cnnstt", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

#---------------------------------------------------------------------------
# テキストからサウンドに変換（ＴＴＳ）

class CnvVce:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lsttts_nod"], {"default": diccnf["deftts_nod"]}),
        "config": (diccnf["lsttts_cnf"], {"default": diccnf["deftts_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcTts.cnntts", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

#---------------------------------------------------------------------------
# テキストからテキストを生成（ＬＬＭ）：オプションあり

class GenTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lstttt_nod"], {"default": diccnf["defttt_nod"]}),
        "config": (diccnf["lstttt_cnf"], {"default": diccnf["defttt_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING", "STRING")
  RETURN_NAMES = ("keymmd", "keyopt")
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcTtt.cnnttt", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["key000"]
    keyopt = datres["key001"]
    return (keymmd, keyopt)

#---------------------------------------------------------------------------
# テキストからテキストに変換（感情分析）

class CnvSen:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lstsen_nod"], {"default": diccnf["defsen_nod"]}),
        "config": (diccnf["lstsen_cnf"], {"default": diccnf["defsen_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcSen.cnnsen", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

#---------------------------------------------------------------------------
# テキストからテキストに変換（ＲＡＧ）

class CnvRag:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "keymmd": ("STRING", {"default": "", "forceInput": True}),
        "server": (diccnf["lstsen_nod"], {"default": diccnf["defsen_nod"]}),
        "config": (diccnf["lstsen_cnf"], {"default": diccnf["defsen_cnf"]}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("keymmd",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, keymmd, server, config):
    datreq = {"status": "0", "keymmd": keymmd, "keyprc": "xoxxox.PrcRag.cnnrag", "server": dicsrv[server], "config": config}
    datres = await MidClt.reqprc(datreq, adrmid + MidClt.adrprc)
    keymmd = datres["keymmd"]
    return (keymmd,)

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
        "txtreq": ("STRING", {"forceInput": True}),
        "sen000": ("STRING", {"forceInput": False, "multiline": False, "default": "joy"}),
        "sen001": ("STRING", {"forceInput": False, "multiline": False, "default": "sadness"}),
        "sen002": ("STRING", {"forceInput": False, "multiline": False, "default": "anticipation"}),
        "sen003": ("STRING", {"forceInput": False, "multiline": False, "default": "surprise"}),
        "sen004": ("STRING", {"forceInput": False, "multiline": False, "default": "anger"}),
        "sen005": ("STRING", {"forceInput": False, "multiline": False, "default": "fear"}),
        "sen006": ("STRING", {"forceInput": False, "multiline": False, "default": "disgust"}),
        "sen007": ("STRING", {"forceInput": False, "multiline": False, "default": "trust"}),
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
        "string": ("STRING", {"default": "", "forceInput": True}),
        "select": (["0", "1", "2", "3", "4", "5", "6", "7"], {"default": "0"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("txtres",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/settlk"

  async def anchor(self, string, select):
    return (select,)

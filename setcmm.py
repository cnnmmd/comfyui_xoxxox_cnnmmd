#---------------------------------------------------------------------------
# 参照

import server
import time
from .lib.shared import PrcCmf

#---------------------------------------------------------------------------

dictip = PrcCmf.gettip()

#---------------------------------------------------------------------------
# 機能：入力をコンソールに出力（文字）

class LogTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtreq": ("STRING", {"forceInput": True, "default": "", "tooltip": dictip["LogTxt.txtreq"]}),
      },
    }
  OUTPUT_NODE = True
  RETURN_TYPES = ()
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcmm"

  def anchor(self, txtreq):
    print(txtreq, flush=True)
    return ()

#---------------------------------------------------------------------------
# 機能：入力をコンソールに出力（数値）

class LogNum:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "numreq": ("INT", {"forceInput": True, "default": 0, "tooltip": dictip["LogNum.numreq"]}),
      },
    }
  OUTPUT_NODE = True
  RETURN_TYPES = ()
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcmm"

  def anchor(self, numreq):
    print(numreq, flush=True)
    return ()

#---------------------------------------------------------------------------
# 機能：ワークフローを実行

class RunFlw:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"forceInput": True, "default": "", "tooltip": dictip["RunFlw.string"]}),
        "numsec": ("INT", {"default": 5, "tooltip": dictip["RunFlw.numsec"]}),
      },
    }
  OUTPUT_NODE = True
  RETURN_TYPES = ()
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setcmm"

  def anchor(self, string, numsec):
    time.sleep(numsec)
    server.PromptServer.instance.send_sync("xoxxox_runflw", {})
    return ()

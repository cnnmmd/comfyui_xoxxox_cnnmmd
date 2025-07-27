#---------------------------------------------------------------------------
# 参照

import server
import time

#---------------------------------------------------------------------------
# 機能：入力をコンソールに出力（文字）

class Xoxxox_LogTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtreq": ("STRING", {"forceInput": True, "default": ""}),
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

class Xoxxox_LogNum:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "numreq": ("INT", {"forceInput": True, "default": 0}),
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

class Xoxxox_RunFlw:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "string": ("STRING", {"forceInput": True, "default": ""}),
        "numsec": ("INT", {"default": 5}),
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

#---------------------------------------------------------------------------
# 参照

from PIL import Image
import torch
from .lib.shared import CnvImg

#---------------------------------------------------------------------------
# 変換（テキストの一部を指定の文字列で置換する）

class Xoxxox_RepTxt:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "txtbdy": ("STRING", {"forceInput": True, "multiline": True}),
        "txtmod": ("STRING", {"forceInput": True, "multiline": True}),
        "txtorg": ("STRING", {"forceInput": False, "multiline": False, "default": "<s>"}),
      },
    }
  RETURN_TYPES = ("STRING",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setetc"

  def anchor(self, txtbdy, txtmod, txtorg):
    txtres = txtbdy.replace(txtorg, txtmod)
    return (txtres,)

#---------------------------------------------------------------------------
# 変換（本体の画像とそのマスクを受け取り、透過画像を生成する）

class Xoxxox_TrnBak:
  @classmethod
  def INPUT_TYPES(s):
    return {
      "required": {
        "imgtsr_con": ("IMAGE",),
        "imgtsr_msk": ("MASK",),
      },
    }
  RETURN_TYPES = ("IMAGE",)
  FUNCTION = "anchor"
  CATEGORY = "xoxxox/setetc"

  def anchor(self, imgtsr_con, imgtsr_msk):
    lstimg = []

    for (i, m) in enumerate(imgtsr_con):
      imgpil_con = CnvImg.cnvpil(imgtsr_con[i])
      imgpil_msk = CnvImg.cnvpil(imgtsr_msk[i])
      r, g, b = imgpil_con.split()
      imgpil_cmp = Image.merge("RGBA", (r, g, b, imgpil_msk))
      lstimg.append(CnvImg.cnvtsr(imgpil_cmp)[None,])
    lsttsr = torch.cat(lstimg)
    return (lsttsr,)

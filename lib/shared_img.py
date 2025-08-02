#---------------------------------------------------------------------------

import numpy as np
from PIL import Image
import torch

#---------------------------------------------------------------------------
# 画像の変換

class CnvImg:

  # HWC (256) -> HWC (0-1)
  @staticmethod
  def cnvtsr(imgpil):
    g = np.array(imgpil).astype(np.float32) / 255.0
    imgtsr = torch.from_numpy(g)
    return imgtsr

  # HWC (0-1) -> HWC (256)
  @staticmethod
  def cnvpil(imgtsr):
    g = imgtsr.cpu().numpy() * 255.0
    g = np.clip(g, 0, 255).astype(np.uint8)
    imgpil = Image.fromarray(g)
    return imgpil

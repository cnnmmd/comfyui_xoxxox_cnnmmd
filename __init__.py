from .setcmm import Xoxxox_LogTxt, Xoxxox_LogNum, Xoxxox_RunFlw
from .setetc import Xoxxox_RepTxt, Xoxxox_TrnBak
from .setmid import Xoxxox_IniFlw, Xoxxox_SetNil, Xoxxox_PutTxt, Xoxxox_SetTxt, Xoxxox_GetTxt, Xoxxox_SetImg, Xoxxox_GetImg, Xoxxox_SetAud, Xoxxox_GetAud, Xoxxox_DlySet, Xoxxox_DlyGet
from .setmem import Xoxxox_SetMem, Xoxxox_GetMem
from .setblb import Xoxxox_GetDir, Xoxxox_SetDir, Xoxxox_GetDis, Xoxxox_SetDis
from .setcnv import Xoxxox_CnvDat
from .setimg import Xoxxox_GenImg
from .settlk import Xoxxox_CnvVce, Xoxxox_CnvTxt, Xoxxox_GenTxt, Xoxxox_CnvSen, Xoxxox_SenTxt
from .setclt import Xoxxox_SndVce, Xoxxox_RcvVce, Xoxxox_SwtImg

NODE_CLASS_MAPPINGS = {
  "Xoxxox_LogTxt": Xoxxox_LogTxt,
  "Xoxxox_LogNum": Xoxxox_LogNum,
  "Xoxxox_RunFlw": Xoxxox_RunFlw,

  "Xoxxox_RepTxt": Xoxxox_RepTxt,
  "Xoxxox_TrnBak": Xoxxox_TrnBak,

  "Xoxxox_IniFlw": Xoxxox_IniFlw,
  "Xoxxox_SetNil": Xoxxox_SetNil,
  "Xoxxox_PutTxt": Xoxxox_PutTxt,
  "Xoxxox_SetTxt": Xoxxox_SetTxt,
  "Xoxxox_GetTxt": Xoxxox_GetTxt,
  "Xoxxox_SetImg": Xoxxox_SetImg,
  "Xoxxox_GetImg": Xoxxox_GetImg,
  "Xoxxox_SetAud": Xoxxox_SetAud,
  "Xoxxox_GetAud": Xoxxox_GetAud,
  "Xoxxox_DlySet": Xoxxox_DlySet,
  "Xoxxox_DlyGet": Xoxxox_DlyGet,

  "Xoxxox_SetMem": Xoxxox_SetMem,
  "Xoxxox_GetMem": Xoxxox_GetMem,

  "Xoxxox_GetDir": Xoxxox_GetDir,
  "Xoxxox_SetDir": Xoxxox_SetDir,
  "Xoxxox_GetDis": Xoxxox_GetDis,
  "Xoxxox_SetDis": Xoxxox_SetDis,

  "Xoxxox_CnvDat": Xoxxox_CnvDat,

  "Xoxxox_GenImg": Xoxxox_GenImg,

  "Xoxxox_CnvVce": Xoxxox_CnvVce,
  "Xoxxox_CnvTxt": Xoxxox_CnvTxt,
  "Xoxxox_GenTxt": Xoxxox_GenTxt,
  "Xoxxox_CnvSen": Xoxxox_CnvSen,
  "Xoxxox_SenTxt": Xoxxox_SenTxt,

  "Xoxxox_SndVce": Xoxxox_SndVce,
  "Xoxxox_RcvVce": Xoxxox_RcvVce,
  "Xoxxox_SwtImg": Xoxxox_SwtImg,
}

WEB_DIRECTORY = "./web"

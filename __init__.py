from .setcmm import LogTxt, LogNum, RunFlw, EndFlw
from .setetc import RepTxt, GrpTxt, TrnBak, PrcPrc, PrcXws
from .setmid import IniFlw, SetNil, PutTxt, SetTxt, GetTxt, SetImg, GetImg, SetAud, GetAud, DlySet, DlyGet
from .setmem import SetMem, GetMem
from .setblb import GetDir, SetDir, GetDis, SetDis
from .setcnv import CnvDat
from .setimg import GenImg
from .settlk import CnvVce, CnvTxt, GenTxt, CnvSen, CnvRag, SenTxt, SenSlc
from .setclt import SndVce, RcvVce, SwtImg

NODE_CLASS_MAPPINGS = {
  "Xoxxox_LogTxt": LogTxt,
  "Xoxxox_LogNum": LogNum,
  "Xoxxox_RunFlw": RunFlw,
  "Xoxxox_EndFlw": EndFlw,

  "Xoxxox_RepTxt": RepTxt,
  "Xoxxox_GrpTxt": GrpTxt,
  "Xoxxox_TrnBak": TrnBak,
  "Xoxxox_PrcPrc": PrcPrc,
  "Xoxxox_PrcXws": PrcXws,

  "Xoxxox_IniFlw": IniFlw,
  "Xoxxox_SetNil": SetNil,
  "Xoxxox_PutTxt": PutTxt,
  "Xoxxox_SetTxt": SetTxt,
  "Xoxxox_GetTxt": GetTxt,
  "Xoxxox_SetImg": SetImg,
  "Xoxxox_GetImg": GetImg,
  "Xoxxox_SetAud": SetAud,
  "Xoxxox_GetAud": GetAud,
  "Xoxxox_DlySet": DlySet,
  "Xoxxox_DlyGet": DlyGet,

  "Xoxxox_SetMem": SetMem,
  "Xoxxox_GetMem": GetMem,

  "Xoxxox_GetDir": GetDir,
  "Xoxxox_SetDir": SetDir,
  "Xoxxox_GetDis": GetDis,
  "Xoxxox_SetDis": SetDis,

  "Xoxxox_CnvDat": CnvDat,

  "Xoxxox_GenImg": GenImg,

  "Xoxxox_CnvVce": CnvVce,
  "Xoxxox_CnvTxt": CnvTxt,
  "Xoxxox_GenTxt": GenTxt,
  "Xoxxox_CnvSen": CnvSen,
  "Xoxxox_CnvRag": CnvRag,
  "Xoxxox_SenTxt": SenTxt,
  "Xoxxox_SenSlc": SenSlc,

  "Xoxxox_SndVce": SndVce,
  "Xoxxox_RcvVce": RcvVce,
  "Xoxxox_SwtImg": SwtImg,
}

WEB_DIRECTORY = "./web"

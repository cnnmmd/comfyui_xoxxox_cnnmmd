from .setcmm import LogTxt, LogNum, RunFlw
from .setetc import RepTxt, TrnBak
from .setmid import IniFlw, SetNil, PutTxt, SetTxt, GetTxt, SetImg, GetImg, SetAud, GetAud, DlySet, DlyGet
from .setmem import SetMem, GetMem
from .setblb import GetDir, SetDir, GetDis, SetDis
from .setcnv import CnvDat
from .setimg import GenImg
from .settlk import CnvVce, CnvTxt, GenTxt, GenTxt_Opt, CnvSen, SenTxt, SenSlc
from .setclt import SndVce, RcvVce, SwtImg

NODE_CLASS_MAPPINGS = {
  "Xoxxox_LogTxt": LogTxt,
  "Xoxxox_LogNum": LogNum,
  "Xoxxox_RunFlw": RunFlw,

  "Xoxxox_RepTxt": RepTxt,
  "Xoxxox_TrnBak": TrnBak,

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
  "Xoxxox_GenTxt_Opt": GenTxt_Opt,
  "Xoxxox_CnvSen": CnvSen,
  "Xoxxox_SenTxt": SenTxt,
  "Xoxxox_SenSlc": SenSlc,

  "Xoxxox_SndVce": SndVce,
  "Xoxxox_RcvVce": RcvVce,
  "Xoxxox_SwtImg": SwtImg,
}

NODE_DISPLAY_NAME_MAPPINGS = {
  "Xoxxox_LogNum": "Log Number",
  "Xoxxox_LogTxt": "Log Text",
  "Xoxxox_RunFlw": "Restart Workflow",
  "Xoxxox_RepTxt": "Replace Text",
  "Xoxxox_TrnBak": "Convert Mask to Alpha",
  "Xoxxox_IniFlw": "Initialize Relay State",
  "Xoxxox_SetNil": "Send Empty Data",
  "Xoxxox_PutTxt": "Input Text",
  "Xoxxox_SetTxt": "Send Text",
  "Xoxxox_GetTxt": "Receive Text",
  "Xoxxox_SetImg": "Send Image",
  "Xoxxox_GetImg": "Receive Image",
  "Xoxxox_SetAud": "Send Audio",
  "Xoxxox_GetAud": "Receive Audio",
  "Xoxxox_DlySet": "Poll (Send Data-Key when Ready)",
  "Xoxxox_DlyGet": "Poll (Receive Data-Key when Ready)",
  "Xoxxox_SetDir": "Write File",
  "Xoxxox_GetDir": "Read File",
  "Xoxxox_SetDis": "Auto-Write Files",
  "Xoxxox_GetDis": "Auto-Read Files",
  "Xoxxox_SetMem": "Write Memory",
  "Xoxxox_GetMem": "Read Memory",
  "Xoxxox_CnvDat": "Convert Data",
  "Xoxxox_GenImg": "Generate Image",
  "Xoxxox_CnvTxt": "Transcribe Speech (STT, ...)",
  "Xoxxox_CnvVce": "Synthesize Speech (TTS, ...)",
  "Xoxxox_GenTxt": "Generate Text (LLM, ...)",
  "Xoxxox_GenTxt_Opt": "Generate Text (LLM, ...)",
  "Xoxxox_CnvSen": "Analyze Sentiment (SA, ER, ...)",
  "Xoxxox_SenTxt": "Convert Emotion Label to Text",
  "Xoxxox_SenSlc": "Select Emotion Label",
  "Xoxxox_SndVce": "Record and Send Audio",
  "Xoxxox_RcvVce": "Receive and Play Audio",
  "Xoxxox_SwtImg": "Receive and Play Audio (Lip-Sync)"
}

WEB_DIRECTORY = "./web"

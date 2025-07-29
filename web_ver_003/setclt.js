import { app } from '../../../scripts/app.js';
import { api } from '../../../scripts/api.js';
import { SndVce, RcvVce, SwtImg } from 'http://localhost:10002/xoxxox/lib/shared_tlk.js';
const UrlAud = 'http://localhost:10002/xoxxox/lib/worker_aud.js';

//--------------------------------------------------------------------------
// 音声送信

app.registerExtension({
  name: 'Xoxxox_SndvVce',
  async setup() {

    api.addEventListener('xoxxox_sndvce', async ({detail}) => {      
      console.log('sts: load xoxxox_sndvce'); // DBG
      const sndvce = new SndVce(detail['adrsnd'], detail['thdvce'], detail['mscend'], UrlAud);
      await sndvce.iniAud();
      await sndvce.recVce();
    })
  }
});

//--------------------------------------------------------------------------
// 音声受信

app.registerExtension({
  name: 'Xoxxox_RcvVce',
  async setup() {

    api.addEventListener('xoxxox_rcvvce', async ({detail}) => {
      console.log('sts: load xoxxox_rcvvce'); // DBG
      const rcvvce = new RcvVce(detail['adrrcv']);
      await rcvvce.plyVce();
    })
  }
});

//--------------------------------------------------------------------------
// 音声受信〜画像切替

app.registerExtension({
  name: 'Xoxxox_SwtImg',
  async setup() {

    api.addEventListener('xoxxox_swtimg', async ({detail}) => {
      console.log('sts: load xoxxox_swtimg'); // DBG
      const rcvvce = new SwtImg(detail['adrrcv'], detail['thdvce'], detail['adrswc'],  detail['adrchr'], detail['imgchr'], detail['arrimg'], detail['sclimg'], detail['poscox'], detail['poscoy']);
      await rcvvce.swtChr();
      await rcvvce.plyVce();
    })
  }
});

//--------------------------------------------------------------------------
// 参照

import { app } from '../../../scripts/app.js';
import { api } from '../../../scripts/api.js';

//--------------------------------------------------------------------------
// 機能：ワークフローを起動

app.registerExtension({
  name: 'Xoxxox_RunFlw',
  async setup() {

    api.addEventListener('xoxxox_runflw', async ({detail}) => {
      app.queuePrompt(0);
 
    })

  }
});

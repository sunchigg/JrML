## Warning

### 請保持誠信正直，若於訓練過程中，請勿參考，謝謝。

### Please be HONEST and DO NOT refer these materials during the training courses or practice periods. We uphold a corporate culture of integrity, prudence, and professionalism to move towards our goals.

## Overview

每間有經營信用卡業務的公司都必須要有辨識偽冒信用卡交易的能力，因為這對獲利、損失、顧客體驗、顧客信任事關重要。身為最美的山、顧客心中最愛的玉山銀行當然也不例外。

這次正式比賽的資料來自行內信用卡處的真實營運資料，在權衡建模難度、資料筆數、單機能處理的檔案大小等因素後，我們以歸戶為單位從2017年5月至2018年2月間，抽樣了533,202筆資料作訓練資料集，當中有76,721筆是偽冒交易；而在測試資料集部分共有來自2018年3月間的472,335筆資料，當中僅有1,438筆冒用資料，與真實的資料比例較為接近，冒用比例僅佔0.305%。

如同先前舉行的練習比賽，為了讓大家可以在開獎日之前檢視自己的模型是否有更近一步，所以開放公開排行榜，讓大家可以在每次上傳之後，根據測試資料集的30%計算該次預測結果的F1 score排名。

Detecting credit card fraud is a must-have capability in companies that run credit card business, because this is truly matter not only to  customer’s trusts and experiences but also to company’s profits and losses. Notably, like the most beautiful mountain in Taiwan, E.Sun Bank is the most beloved bank and doing well in  FRAUD DETECTION without exception.

The data in this game is sampled from actual credit card transactions. After considering the hardness of model building, number of entries, the memory in PC and other reasonable causes. The training data is sampled by customer from 1 May, 2017 to 28 February, 2018.  In the same way, we collected 472,335 transactions from 1 March, 2018 to 31 March, 2018 to build testing data. 
Especially, there are 1,438 fraud transactions in testing data. It’s a tiny proportion of transactions. The fraud ratio in testing data is 0.305% and that is close to the fraud ratio in all transactions.

Like the toy game hold before, the ranking method is F1 score. It’s open to see the latest ranking in public leader board after uploading your result every time. The public score is computed based on 50% of testing data and the private score will be based on the other 70%.
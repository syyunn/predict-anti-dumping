# Predict Antidumping 
From the U.S.

## What is Antidumping?
- U.S. industries may petition the government for relief from imports that are sold in the United States at less than fair value ("dumped"). 
- Then 1) the USITC and 2) the U.S. Department of Commerce conducts investigation and determines whether an industry in the United States is materially injured. 
- If the industry is determined as materially injured, the head of the U.S. Department of Commerce issues an antidumping order 
- This order is enforced by the U.S. Customs Service with the increased duty for the products within the scope of that antidumping case.

## Motivation
- Worked with Korean Government Officers from the Ministry of Trade for 2 months.
- They want to predict any U.S. trade actions in advance.
    - AD/CVD petition filings, initiation of investigation, outcome of preliminary/affirmative determination.
    - Export regulation - such as Huawei added to the Entity List of EAR (Export Administration Regulations)
    - ...

## Literature 
### Classification of Literature 
1. Target of Prediction
    - Predicting the total number of petition filed during the certain period of time (e.g. 201X QX)      
       - [Ahmad, 2018](https://usitc.gov/publications/332/working_papers/ecwp-2018-10-a.pdf) 
    - Predicting final outcome of the U.S. Department of Commerce & USITC investigation - whether the material injury is admitted or not (affirmative or not)
       - [Drope, 2004](https://sci-hub.tw/10.2307/3219832)
       - [Iliescu, 2016](http://www2.southeastern.edu/orgs/econjournal/index_files/JIGES%20DECEMBER%202016%20Nicoleta%20Iliescu%20%20US%20Lobby%20Activity.pdf)
2. Model Input(s) (to predict one of the targets of prediction above)
    - Macro Economic Data 
        - Domestic: GDP or RGDP, Domestic Industrial Production (from FRED), Employment Rate
            - [Ahmad, 2018](https://usitc.gov/publications/332/working_papers/ecwp-2018-10-a.pdf)  
        - External: Real Exchange Rate, Import Penetration, Overall Trade
            - [Ahmad, 2018](https://usitc.gov/publications/332/working_papers/ecwp-2018-10-a.pdf) 
    - Political Spending Data
        - Lobby Report (LD-2; amount of money spent to hire lobbyists or expenditure that lobbyists spent)
            - [Drope, 2004](https://sci-hub.tw/10.2307/3219832)
        - PAC contribution
            - [Drope, 2004](https://sci-hub.tw/10.2307/3219832)
        - Average Soft Money Spending
            - [Drope, 2004](https://sci-hub.tw/10.2307/3219832)        
    - Industry Level Data 
        - Industry Size
           - [Iliescu, 2016](http://www2.southeastern.edu/orgs/econjournal/index_files/JIGES%20DECEMBER%202016%20Nicoleta%20Iliescu%20%20US%20Lobby%20Activity.pdf)
        - UNComtrade Data (Bilateral trade volume & total value in product-group level)    
           - [Iliescu, 2016](http://www2.southeastern.edu/orgs/econjournal/index_files/JIGES%20DECEMBER%202016%20Nicoleta%20Iliescu%20%20US%20Lobby%20Activity.pdf)

### What is Lacking Current Literature?
1. Scope
- HS
2. Model
- So Linear.
  - Linear models are hard to catch the interaction between multiple variables
- However, if non

## Final Miscellaneous sharing is..
### Hard to reproduce
### Outdated
### Current Trend of Antidumping Orders
### So Linear but Is Non Linear Acceptable with its Lack of Interpretability (of the model)?


## References 
- [Can Macroeconomic Factors Predict Antidumping Filings in the United States? (Ahmad, 2018)](https://usitc.gov/publications/332/working_papers/ecwp-2018-10-a.pdf) 

- [Purchasing Protection? The effect of Political Spending on U.S. Trade Policy (Drope, 2004)](https://sci-hub.tw/10.2307/3219832)

- [US Lobby Activity and Antidumping Outcomes (Iliescu, 2016)](http://www2.southeastern.edu/orgs/econjournal/index_files/JIGES%20DECEMBER%202016%20Nicoleta%20Iliescu%20%20US%20Lobby%20Activity.pdf)
 
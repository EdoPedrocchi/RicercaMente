# PREDICT IPO USING MACHINE LEARNING

# TABLE OF CONTENT
1. [Introduction](#introduction)
2. [Literature Review](#literature-review)
3. [Research Methodology](#research-methodology)
5. [Results](#results)
6. [Conclusion](#conclusion)
7. [References](#references)


# INTRODUCTION
What's that?

We've created an **open source paper** where anyone, including you, can contribute. 

Predicting the success or failure of an IPO using machine learning, is it possible?
We will start by analyzing the most important papers in the field, doing a literature review. 
Then, we will be the ones trying our hand at this endeavor and analyzing the results. 
If you want to help, you can contribute by improving each section of the paper. 

An initial public offering (IPO) is the process through which a private company becomes publicly traded by offering shares of its stock to the general public for the first time. This is typically done to raise capital for expansion, pay off debts, or provide liquidity to existing shareholders. 

During an IPO, the company works with investment banks to determine the offering price for its shares. 

This price is often determined through a process of valuation, which considers factors such as the company's financial performance, growth prospects, industry comparables, and market conditions. 

In this research, we will seek to understand the success or failure of an IPO in the short term.
By success, we mean if the stock price significantly increases immediately after the IPO and remains stable or continues to rise in the subsequent period, it can be considered a success. 

However, remember, it is in the long term that the quality of a company is truly seen.

# LITERATURE REVIEW

[Contribute and write it!](https://github.com/EdoPedrocchi/RicercaMente/issues/25)

# RESEARCH METHODOLOGY
## Dataset

The dataset used come from the platfotm ["Orbis M&A"](https://orbismanda.bvdinfo.com/) and contains over 20k companies that have made an IPO.

For each company, we know these variables:

1. **Target country code**: The code of the target country where the target company is located or primarily associated with.

2. **Deal value th USD**: The value of the deal expressed in thousands of US dollars.

3. **Target business description(s)**: Description or descriptions of the sector or activities of the target company subject to the deal.

4. **Completed date**: Date when the deal was completed or finalized.

5. **Deal equity value th USD**: The equity value of the deal expressed in thousands of US dollars.

6. **Pre-deal target operating revenue/turnover th USD Last avail. yr**: The operating revenue or turnover of the target company before the deal, expressed in thousands of US dollars, for the last available year.

7. **Pre-deal target EBITDA th USD Last avail. yr**: The earnings before interest, taxes, depreciation, and amortization (EBITDA) of the target company before the deal, expressed in thousands of US dollars, for the last available year.

8. **Pre-deal target EBIT th USD Last avail. yr**: The earnings before interest and taxes (EBIT) of the target company before the deal, expressed in thousands of US dollars, for the last available year.

9. **Pre-deal target profit before tax th USD Last avail. yr**: The profit before tax of the target company before the deal, expressed in thousands of US dollars, for the last available year.

10. **Pre-deal target profit after tax th USD Last avail. yr**: The profit after tax of the target company before the deal, expressed in thousands of US dollars, for the last available year.

11. **Pre-deal target net profit th USD Last avail. yr**: The net profit of the target company before the deal, expressed in thousands of US dollars, for the last available year.

12. **Pre-deal target total assets th USD Last avail. yr**: The total assets of the target company before the deal, expressed in thousands of US dollars, for the last available year.

13. **Pre-deal target net assets th USD Last avail. yr**: The net assets of the target company before the deal, expressed in thousands of US dollars, for the last available year.

14. **Pre-deal target current liabilities th USD Last avail. yr**: The current liabilities of the target company before the deal, expressed in thousands of US dollars, for the last available year.

15. **Pre-deal target shareholders funds th USD Last avail. yr**: The shareholders' funds of the target company before the deal, expressed in thousands of US dollars, for the last available year.

16. **Pre-deal target market capitalisation (Last available year) th USD**: The market capitalization of the target company before the deal, expressed in thousands of US dollars, for the last available year.

17. **Pre-deal target number of months Last avail. yr**: The number of months for which pre-deal financial data of the target company are available, for the last available year.

18. **Target stock price 1 month after completion USD**: The stock price of the target company one month after the completion of the deal, expressed in US dollars.

19. **Target major sector**: The major sector in which the target company operates.

20. **Target stock price after completion USD**: The stock price of the target company after the completion of the deal, expressed in US dollars.

21. **Target stock price 1 week after completion USD**: The stock price of the target company one week after the completion of the deal, expressed in US dollars.

## Research objective

How do we decide whether an IPO is a success or failure in the short term?

1. If  "**Target stock price after completion USD**" <  "**Target stock price 1 week after completion USD**" < "**Target stock price 1 month after completion USD**" , The IPO is a "succes"
2. If  "**Target stock price after completion USD**" >  "**Target stock price 1 week after completion USD**" > "**Target stock price 1 month after completion USD**" , The IPO is a "failure"
3. . If  "**Target stock price after completion USD**" =  "**Target stock price 1 week after completion USD**" = "**Target stock price 1 month after completion USD**" , The IPO is "constant"
4. Else, null value

Why this decision?
Markets are variable, so we need a trend (we use 2 variables to figure out if the price is going up or down).

Taking the photo at one time, say only a month later, without an intermediate date is certainly less accurate, although this interpretation is not perfect


The goal will then be to create models that use all other variables to predict the success or failure of the IPO

## Exploratory data analysis

[Contribute and do it!](https://github.com/EdoPedrocchi/RicercaMente)

# RESULTS

# CONCLUSION

# REFERNCES

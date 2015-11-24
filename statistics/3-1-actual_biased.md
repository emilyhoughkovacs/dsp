[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

This exercise took us through the example in `chap03ex.ipynb`. The purpose of this example was to illustrate the difference in a biased PMF and an unbiased PMF, using number of children in a household as an example. If you asked a group of children how many children in their household there are, you would get a higher average number of children than the actual number. This is due to overcounting households with greater numbers of children, in direct proportion to the number of children.

For example, an only child's household would be counted once because that child is the only respondent. However, a household with six children would count six times as much since each child responded '6'. Clearly this biases the results towards larger households.

On the other hand, if you ask the head of household how many kids they have, each parent would respond only once. Therefore, the household of 6 children would get counted once and the household of 1 child would get counted once. I guess this is why parents do taxes and not kids. :wink:

To do this, I basically followed the instructions for importation and writing the Bias function. I then created two Pmf objects as follows:

```
pmf = thinkstats2.Pmf(resp['numkdhh'], label='numkdhh')
biased = BiasPmf(pmf, label='biased numkdhh')
```
What BiasPmf does is it multiplies each (parent's) response by itself - just like how the six children who respond '6' would be 6 x6 kids as opposed to their head of household responding 6 x1 times. It then normalizes the Pmf so it still sums to 1.

The result is the following chart:
![Biased PMF chart]
(http://41.media.tumblr.com/77d79216d95dc1d2c387db186dd73fce/tumblr_nybt3j6hjA1rhoazgo1_400.png)
As you can see, the probability that a household has 0 children is almost half. However, the biased PMF peaks at 2. Some special things to note: since anything times 0 is 0, the portion of the PMF under 0 has completely disappeared. Also, 6+ children is roughly 6 times higher, and 5 children is 5x greater than the actual number of households with this many children.

Downey mentions that you can also do the reverse from this. Suppose you had sampled children in the school and asked them the number of children in their home including themselves. Their principal could determine an unbiased PMF for the number of children per household given that data without speaking to the parents, by dividing 1 by each of the responses. This would 'unweight' each response from siblings. (Of course, this is assuming all siblings are school-aged and go to the same school.) This is an effective way to get unbiased data from biased data.

A good question to ask yourself is, "Am I double-counting the data?" This comes up often in analytics when you are measuring visitors to the site. If a visitor hits your site via web and the mobile app, you need to "de-dup" their visit. Any visitor to the site via multiple pathways (iPhone app, mobile web, web, Android app, API/3rd party) needs to be divided by the number of paths they visited with.
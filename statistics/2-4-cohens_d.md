[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The question was to use Cohen's D to measure the difference, if any, between the birthweight of firstborns and other pregnancies. For this investigation I only considered live births.

Cohen's D measures the effect size by giving the standard deviation of the difference of two means. Because it is the difference of means divided by the pooled standard deviation, the negative or positive sign on Cohen's D value only indicates if you subtracted the larger mean from the smaller one or the reverse. I subtracted the 'others mean' from the firstborn mean and got a negative value, showing that the birth weight of firstborns is slightly smaller than the birthweight of other babies.

I solved the problem the easy way and the hard way. The easy way was implementing the Cohen's D method from the thinkstats2 module. The hard way was implementing Cohen's D using numpy and pandas.

```
import thinkstats2
import first
# Even though numpy and pandas are already imported in thinkstats2,
# I wanted them handy.
import numpy as np
import pandas as pd
```
`live, firsts, others = first.MakeFrames()`
```
# From scratch
firstwgt = firsts['totalwgt_lb']
otherswgt = others['totalwgt_lb']
first_mean = firstwgt.mean()
others_mean = otherswgt.mean()
diff_mean = others_mean-first_mean
first_var = firstwgt.var()
others_var = otherswgt.var()
first_n = len(firstwgt)
others_n = len(otherswgt)
s = np.sqrt((first_n*first_var + others_n*others_var)/(first_n+others_n))
cohens_d = (first_mean-others_mean)/s
print cohens_d
```
Result: *-0.089*<br>
The difference in means for total birthweight is 0.089 standard deviations. The average firstborn is 7.20 lbs and the average other child is 7.33. According to [this site](http://rpsychologist.com/d3/cohend/), a small effect would be between 0.2 and 0.5. Given this knowledge, I would say the difference in birthweight between firstborns and other pregnancies is insignificant.
[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The purpose of this question was to use the PMF and CDF to determine if the random number generator included in python is truly random. To do this, I created 1000 random numbers and then plotted their PMF and CDF using Allen Downey's `thinkplot` and `thinkstats2` packages.

First, however, I practiced creating the PMF by hand using this methodology:<br>
```from collections import Counter```<br>
```import random```<br>
```rand1000 = [random.random() for x in range(1000)]```<br>
```
hist = {}
pmf = {}
hist = Counter(rand1000)
for x in hist:
    pmf[x] = hist[x]/1000.0
```
However, then I could not convert my pmf dictionary into a Pmf object so I simply used my hist dictionary.

As expected, the PMF was useless. Each of the random numbers was unique because the digits are very long, so they each had a 0.0001 probability.

Plotting the CDF was a little bit more interesting.<br>
![CDF of 1000 random numbers 0-1](https://41.media.tumblr.com/6b971d0f58929c6b6192e600de00782a/tumblr_nyc098nYai1u37fsho1_400.png)<br>
The numbers do seem almost uniform, but the CDF reveals some (very slight) abberations. Below about 0.6, the slope is almost exactly one, meaning that, as expected, 10% of the values are under .1, 20% are under .2, etc. However, at 0.6 there is a slight dip. The way to interpret this dip is as follows: when the slope goes down to less than 1 (it flatlines at about 0 for a short while), there are fewer values in that neighborhood. When the dip increases at a rate faster than 1 (to realign itself to the linear model), there are slightly more values than would be expected in that area.

If you know calculus, you can take the first derivative of the CDF to have an even easier way of interpreting the results. Wherever dy/dx is above 1, there are more values than is to be expected by random chance in that range. Conversely, a derivative of less than 1 indicates fewer values.
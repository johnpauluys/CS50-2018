<html>
<body>
<div id="content">
<h1>Cash</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that calculates the minimum number of coins required to give a user change.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./cash</span>
Change owed: <span class="underline">0.41</span>
4</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">

<div class="paragraph">
<p>When using a device like this, odds are you want to minimize the number of coins you&#8217;re dispensing for each customer, lest you have to press levers more times than are necessary. Fortunately, computer science has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.</p>
</div>
<div class="paragraph">
<p>According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one "that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems."</p>
</div>
<div class="paragraph">
<p>What&#8217;s all that mean? Well, suppose that a cashier owes a customer some change and on that cashier&#8217;s belt are levers that dispense quarters, dimes, nickels, and pennies. Solving this "problem" requires one or more presses of one or more levers. Think of a "greedy" cashier as one who wants to take, with each press, the biggest bite out of this problem as possible. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is "best" inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.</p>
</div>
<div class="paragraph">
<p>It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America&#8217;s currency (and also the European Union&#8217;s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible. How few? Well, you tell us!</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>Write, in a file called <code>cash.c</code> in <code>~/workspace/pset1/cash/</code>, a program that first asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made.</p>
</li>
<li>
<p>Use <code>get_float</code> from the CS50 Library to get the user&#8217;s input and <code>printf</code> from the Standard I/O library to output your answer. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).</p>
<div class="ulist">
<ul>
<li>
<p>We ask that you use <code>get_float</code> so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program&#8217;s input will be <code>9.75</code> and not <code>$9.75</code> or <code>975</code>. However, if some customer is owed $9 exactly, assume that your program&#8217;s input will be <code>9.00</code> or just <code>9</code> but, again, not <code>$9</code> or <code>900</code>. Of course, by nature of floating-point values, your program will likely work with inputs like <code>9.0</code> and <code>9.000</code> as well; you need not worry about checking whether the user&#8217;s input is "formatted" like money should be.</p>
</li>
</ul>
</div>
</li>
<li>
<p>You need not try to check whether a user&#8217;s input is too large to fit in a <code>float</code>. Using <code>get_float</code> alone will ensure that the user&#8217;s input is indeed a floating-point (or integral) value but not that it is non-negative.</p>
</li>
<li>
<p>If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.</p>
</li>
<li>
<p>Incidentally, so that we can automate some tests of your code, we ask that your program&#8217;s last line of output be only the minimum number of coins possible: an integer followed by <code>\n</code>.</p>
</li>
</ul>
</div>
</div>
</div>
<div class="sect1">
<h2 id="usage"><a class="link" href="#usage">Usage</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Your program should behave per the example below. Assumed that the underlined text is what some user has typed.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./cash</span>
Change owed: <span class="underline">0.41</span>
4</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./cash</span>
Change owed: <span class="underline">-0.41</span>
Change owed: <span class="underline">-0.41</span>
Change owed: <span class="underline">foo</span>
Change owed: <span class="underline">0.41</span>
4</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>Per the final bullet point of the Specification, above, don&#8217;t forget to put a newline character at the end of your printout!</p>
</li>
<li>
<p>Do beware the inherent imprecision of floating-point values. For instance, <code>0.1</code> cannot be represented exactly as a <code>float</code>. Try printing its value to, say, <code>55</code> decimal places, with code like the below:</p>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-kt">float</span> <span class="tok-n">f</span> <span class="tok-o">=</span> <span class="tok-mf">0.1</span><span class="tok-p">;</span>
<span class="tok-n">printf</span><span class="tok-p">(</span><span class="tok-s">&quot;%.55f</span><span class="tok-se">\n</span><span class="tok-s">&quot;</span><span class="tok-p">,</span> <span class="tok-n">f</span><span class="tok-p">);</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>And so, before making change, you&#8217;ll probably want to convert the user&#8217;s input entirely to cents (i.e., from a <code>float</code> to an <code>int</code>) to avoid tiny errors that might otherwise add up! Of course, don&#8217;t just cast the user&#8217;s input from a <code>float</code> to an <code>int</code>! After all, how many cents does one dollar equal?</p>
</div>
</li>
<li>
<p>And take care to <a href="https://reference.cs50.net/math/round">round</a> your cents (to the nearest penny); don&#8217;t "truncate" (i.e., floor) your cents!</p>
</li>
</ul>
</div>
</div>
</div>
</div>
</body>
</html>

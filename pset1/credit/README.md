<html>
<body>
<div id="content">
<h1>Credit</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that determines whether a provided credit card number is valid according to Luhn&#8217;s algorithm.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./credit</span>
Number: <span class="underline">378282246310005</span>
AMEX</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Odds are you or someone you know has a credit card. That card has a number, both printed on its face and embedded (perhaps with some other data) in the magnetic stripe on back.  That number is also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.  And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^(15) = 1,000,000,000,000,000 unique cards! (That&#8217;s, ahem, a quadrillion.)</p>
</div>
<div class="paragraph">
<p>Now that&#8217;s a bit of an exaggeration, because credit card numbers actually have some structure to them.  American Express numbers all start with 34 or 37; MasterCard numbers start with 51, 52, 53, 54, or 55 (technically, they also have some other potential starting numbers which we won&#8217;t concern ourselves with for this problem); and Visa numbers all start with 4.  But credit card numbers also have a "checksum" built into them, a mathematical relationship between at least one number and others.  That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow.  (Consider the awkward silence you may have experienced at some point whilst paying by credit card at a store whose computer uses a dial-up modem to verify your card.)  Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.</p>
</div>
<div class="paragraph">
<p>So what&#8217;s the secret formula?  Well, most cards use an algorithm invented by Hans Peter Luhn, a nice fellow from IBM.  According to Luhn&#8217;s algorithm, you can determine if a credit card number is (syntactically) valid as follows:</p>
</div>
<div class="olist arabic">
<ol class="arabic" start="0">
<li>
<p>Multiply every other digit by 2, starting with the number&#8217;s second-to-last digit, and then add those products' digits together.</p>
</li>
<li>
<p>Add the sum to the sum of the digits that weren&#8217;t multiplied by 2.</p>
</li>
<li>
<p>If the total&#8217;s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!</p>
</li>
</ol>
</div>
<div class="paragraph">
<p>That&#8217;s kind of confusing, so let&#8217;s try an example with my AmEx: 378282246310005.</p>
</div>
<div class="olist arabic">
<ol class="arabic" start="0">
<li>
<p>For the sake of discussion, let&#8217;s first underline every other digit, starting with the number&#8217;s second-to-last digit:</p>
<div class="paragraph">
<p>3<span class="underline">7</span>8<span class="underline">2</span>8<span class="underline">2</span>2<span class="underline">4</span>6<span class="underline">3</span>1<span class="underline">0</span>0<span class="underline">0</span>5</p>
</div>
<div class="paragraph">
<p>Okay, let&#8217;s multiply each of the underlined digits by 2:</p>
</div>
<div class="paragraph">
<p>7•2 + 2•2 + 2•2 + 4•2 + 3•2 + 0•2 + 0•2</p>
</div>
<div class="paragraph">
<p>That gives us:</p>
</div>
<div class="paragraph">
<p>14 + 4 + 4 + 8 + 6 + 0 + 0</p>
</div>
<div class="paragraph">
<p>Now let&#8217;s add those products' digits (i.e., not the products themselves) together:</p>
</div>
<div class="paragraph">
<p>1 + 4 + 4 + 4 + 8 + 6 + 0 + 0 = 27</p>
</div>
</li>
<li>
<p>Now let&#8217;s add that sum (27) to the sum of the digits that weren&#8217;t multiplied by 2:</p>
<div class="paragraph">
<p>27 + 3 + 8 + 8 + 2 + 6 + 1 + 0 + 5 = 60</p>
</div>
</li>
<li>
<p>Yup, the last digit in that sum (60) is a 0, so my card is legit!</p>
</li>
</ol>
</div>
<div class="paragraph">
<p>So, validating credit card numbers isn&#8217;t hard, but it does get a bit tedious by hand.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>In <code>credit.c</code> in <code>~/workspace/pset1/credit/</code>, write a program that prompts the user for a credit card number and then reports (via <code>printf</code>) whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each&#8217;s format herein.</p>
</li>
<li>
<p>So that we can automate some tests of your code, we ask that your program&#8217;s last line of output be <code>AMEX\n</code> or <code>MASTERCARD\n</code> or <code>VISA\n</code> or <code>INVALID\n</code>, nothing more, nothing less, and that <code>main</code> always return <code>0</code>.</p>
</li>
<li>
<p>For simplicity, you may assume that the user&#8217;s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).</p>
</li>
<li>
<p>Do not assume that the user&#8217;s input will fit in an <code>int</code>! Best to use <code>get_long_long</code> from CS50&#8217;s library to get users' input. (Why?)</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./credit</span>
Number: <span class="underline">378282246310005</span>
AMEX</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./credit</span>
Number: <span class="underline">3782-822-463-10005</span>
Number: <span class="underline">foo</span>
Number: <span class="underline">378282246310005</span>
AMEX</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./credit</span>
Number: <span class="underline">6176292929</span>
INVALID</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Test out your program with a whole bunch of inputs, both valid and invalid. (We certainly will!) Here are a few card numbers that PayPal recommends for testing:</p>
</div>
<div class="paragraph">
<p><a href="https://developer.paypal.com/docs/classic/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing" class="bare">https://developer.paypal.com/docs/classic/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing</a></p>
</div>
<div class="paragraph">
<p>Google (or perhaps a roommate&#8217;s wallet) should turn up more. (If your roommate asks what you&#8217;re doing, don&#8217;t mention us.) If your program behaves incorrectly on some inputs (or doesn&#8217;t compile at all), time to debug!</p>
</div>
</div>
</div>
</div>
</body>
</html>

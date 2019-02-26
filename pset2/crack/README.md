<html>
<body>
<div id="content">
<h1>Crack</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that cracks passwords, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./crack 50fkUxYHbnXGw</span>
rofl</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>On most systems running Linux these days is a file called <code>/etc/shadow</code>, which contains usernames and passwords. Fortunately, the passwords therein aren&#8217;t stored "in the clear" but are instead encrypted using a "one-way hash function." When a user logs into these systems by typing a username and password, the latter is encrypted with the very same hash function, and the result is compared against the username&#8217;s entry in <code>/etc/shadow</code>. If the two hashes match, the user is allowed in. If you&#8217;ve ever forgotten some password, you might have been told that tech support can&#8217;t look up your password but can change it for you. Odds are that&#8217;s because tech support can only see, if anything at all, a hash of your password, not your password itself. But they can create a new hash for you.</p>
</div>
<div class="paragraph">
<p>Even though passwords in <code>/etc/shadow</code> are hashed, the hash function is not always that strong. Quite often are adversaries, upon obtaining that file somehow, able to guess (and check) users' passwords or crack them using brute force (i.e., trying all possible passwords). Below is what <code>/etc/shadow</code> might look like, albeit simplified, wherein each line is formatted as <code>username:hash</code>.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>anushree:50xcIMJ0y.RXo
brian:50mjprEcqC/ts
bjbrown:50GApilQSG3E2
lloyd:50n0AAUD.pL8g
malan:50CcfIk1QrPr6
maria:509nVI8B9VfuA
natmelo:50JIIyhDORqMU
rob:50JGnXUgaafgc
stelios:51u8F0dkeDSbY
zamyla:50cI2vYkF0YU2</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Design and implement a program, <code>crack</code>, that cracks passwords.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Implement your program in a file called <code>crack.c</code> in a directory called <code>crack</code>.</p>
</li>
<li>
<p>Your program should accept a single command-line argument: a hashed password.</p>
</li>
<li>
<p>If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error (of your choice) and exit immediately, with <code>main</code> returning <code>1</code> (thereby signifying an error).</p>
</li>
<li>
<p>Otherwise, your program must proceed to crack the given password, ideally as quickly as possible, ultimately printing the password in the clear followed by <code>\n</code>, nothing more, nothing less, with <code>main</code> returning <code>0</code>.</p>
</li>
<li>
<p>Assume that each password has been hashed with C&#8217;s DES-based (not MD5-based) <code>crypt</code> function.</p>
</li>
<li>
<p>Assume that each password is no longer than five (5) characters. Gasp!</p>
</li>
<li>
<p>Assume that each password is composed entirely of alphabetical characters (uppercase and/or lowercase).</p>
</li>
</ul>
</div>
</div>
</div>
<div class="sect1">
<h2 id="usage"><a class="link" href="#usage">Usage</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Your program should behave per the examples below. Assumed that the underlined text is what some user has typed.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./crack</span>
Usage: ./crack hash</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./crack 50JGnXUgaafgc</span>
rofl</code></pre>
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
<p>Be sure to read up on <code>crypt</code>, taking particular note of its mention of "salt":</p>
</li>
</ul>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>man crypt</code></pre>
</div>
</div>
<div class="paragraph">
<p>Per that man page, you&#8217;ll likely want to put</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-cp">#define _XOPEN_SOURCE</span>
<span class="tok-cp">#include</span> <span class="tok-cpf">&lt;unistd.h&gt;</span><span class="tok-cp"></span></code></pre>
</div>
</div>
<div class="paragraph">
<p>at the top of your file in order to use <code>crypt</code>.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>While testing your code for efficiency, you might want to an easy way to time how long it takes to crack a password.  You can do this easily with the unix <code>time</code> program:</p>
</li>
</ul>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>time ./crack 50JGnXUgaafgc</code></pre>
</div>
</div>
</div>
</div>
</div>
</body>
</html>

<html>
<body>
<div id="content">
<h1>Caesar</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that encrypts messages using Caesar&#8217;s cipher, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./caesar 13</span>
plaintext:  <span class="underline">HELLO</span>
ciphertext: URYYB</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Supposedly, Caesar (yes, that Caesar) used to "encrypt" (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, &#8230;&#8203;, and, wrapping around alphabetically, Z as A.  And so, to say HELLO to someone, Caesar might write IFMMP. Upon receiving such messages from Caesar, recipients would have to "decrypt" them by shifting letters in the opposite direction by the same number of places.</p>
</div>
<div class="paragraph">
<p>The secrecy of this "cryptosystem" relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you&#8217;re perhaps the first in the world to do it, pretty secure!</p>
</div>
<div class="paragraph">
<p>Unencrypted text is generally called <em>plaintext</em>. Encrypted text is generally called <em>ciphertext</em>. And the secret used is called a <em>key</em>.</p>
</div>
<table class="tableblock frame-all grid-all stretch">
<caption class="title">Table 1. Encrypting HELLO with a key of 1 yields IFMMP.</caption>
<colgroup>
<col style="width: 16.6666%;">
<col style="width: 16.6666%;">
<col style="width: 16.6666%;">
<col style="width: 16.6666%;">
<col style="width: 16.6666%;">
<col style="width: 16.667%;">
</colgroup>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>plaintext</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">H</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">E</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">L</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">L</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">O</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>+ key</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>= ciphertext</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">I</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">F</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">M</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">M</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">P</p></td>
</tr>
</tbody>
</table>
<div class="paragraph">
<p>More generally, Caesar&#8217;s algorithm (i.e., cipher) encrypts messages by "rotating" each letter by <em>k</em> positions. More formally, if <em>p</em> is some plaintext (i.e., an unencrypted message), <em>p<sub>i</sub></em> is the <em>i<sup>th</sup></em> character in <em>p</em>, and <em>k</em> is a secret key (i.e., a non-negative integer), then each letter, <em>c<sub>i</sub></em>, in the ciphertext, <em>c</em>, is computed as</p>
</div>
<div class="stemblock">
<div class="content">
\[c_i = (p_i + k) \bmod 26\]
</div>
</div>
<div class="paragraph">
<p>wherein \(\bmod 26\) here means "remainder when dividing by 26." This formula perhaps makes the cipher seem more complicated than it is, but it&#8217;s really just a concise way of expressing the algorithm precisely.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Design and implement a program, <code>caesar</code>, that encrypts messages using Caesar&#8217;s cipher.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Implement your program in a file called <code>caesar.c</code> in a directory called <code>caesar</code>.</p>
</li>
<li>
<p>Your program must accept a single command-line argument, a non-negative integer. Let&#8217;s call it <em>k</em> for the sake of discussion.</p>
</li>
<li>
<p>If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with <code>printf</code>) and return from <code>main</code> a value of <code>1</code> (which tends to signify an error) immediately.</p>
</li>
<li>
<p>You can assume that, if a user does provide a command-line argument, it will be a non-negative integer (e.g., <code>1</code>). No need to check that it&#8217;s indeed numeric.</p>
</li>
<li>
<p>Do not assume that <em>k</em> will be less than or equal to 26. Your program should work for all non-negative integral values of <em>k</em> less than 2<sup>31</sup> - 26. In other words, you don&#8217;t need to worry if your program eventually breaks if the user chooses a value for <em>k</em> that&#8217;s too big or almost too big to fit in an <code>int</code>. (Recall that an <code>int</code> can overflow.) But, even if <em>k</em> is greater than 26, alphabetical characters in your program&#8217;s input should remain alphabetical characters in your program&#8217;s output. For instance, if <em>k</em> is 27, <code>A</code> should not become <code>[</code> even though <code>[</code> is 27 positions away from <code>A</code> in ASCII, per <a href="http://www.asciichart.com/">asciichart.com</a>; <code>A</code> should become <code>B</code>, since <code>B</code> is 27 positions away from <code>A</code>, provided you wrap around from <code>Z</code> to <code>A</code>.</p>
</li>
<li>
<p>Your program must output <code>plaintext:</code> (without a newline) and then prompt the user for a <code>string</code> of plaintext (using <code>get_string</code>).</p>
</li>
<li>
<p>Your program must output <code>ciphertext:</code> (without a newline) followed by the plaintext&#8217;s corresponding ciphertext, with each alphabetical character in the plaintext "rotated" by <em>k</em> positions; non-alphabetical characters should be outputted unchanged.</p>
</li>
<li>
<p>Your program must preserve case: capitalized letters, though rotated, must remain capitalized letters; lowercase letters, though rotated, must remain lowercase letters.</p>
</li>
<li>
<p>After outputting ciphertext, you should print a newline. Your program should then exit by returning <code>0</code> from <code>main</code>.</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./caesar 1</span>
plaintext:  <span class="underline">HELLO</span>
ciphertext: IFMMP</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./caesar 13</span>
plaintext:  <span class="underline">hello, world</span>
ciphertext: uryyb, jbeyq</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./caesar 13</span>
plaintext:  <span class="underline">be sure to drink your Ovaltine</span>
ciphertext: or fher gb qevax lbhe Binygvar</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./caesar</span>
Usage: ./caesar k</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./caesar 1 2 3 4 5</span>
Usage: ./caesar k</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>This program needs to accept a command-line argument, <em>k</em>, so you&#8217;ll want to declare <code>main</code> with:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-kt">int</span> <span class="tok-n">main</span><span class="tok-p">(</span><span class="tok-kt">int</span> <span class="tok-n">argc</span><span class="tok-p">,</span> <span class="tok-n">string</span> <span class="tok-n">argv</span><span class="tok-p">[])</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Recall that <code>argv</code> is an "array" of strings. You can think of an array as row of gym lockers, inside each of which is some value (and maybe some socks). In this case, inside each such locker is a <code>string</code>. To open (i.e., "index into") the first locker, you use syntax like <code>argv[0]</code>, since arrays are "zero-indexed." To open the next locker, you use syntax like <code>argv[1]</code>. And so on. Of course, if there are <code>n</code> lockers, you&#8217;d better stop opening lockers once you get to <code>argv[n - 1]</code>, since <code>argv[n]</code> doesn&#8217;t exist!  (That or it belongs to someone else, in which case you still shouldn&#8217;t open it.)</p>
</div>
<div class="paragraph">
<p>And so you can access <em>k</em> with code like</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-n">string</span> <span class="tok-n">k</span> <span class="tok-o">=</span> <span class="tok-n">argv</span><span class="tok-p">[</span><span class="tok-mi">1</span><span class="tok-p">];</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>assuming it&#8217;s actually there! Recall that <code>argc</code> is an <code>int</code> that equals the number of strings that are in <code>argv</code>, so you&#8217;d best check the value of <code>argc</code> before opening a locker that might not exist!  Ideally, <code>argc</code> will be <code>2</code>. Why? Well, recall that inside of <code>argv[0]</code>, by default, is a program&#8217;s own name. So <code>argc</code> will always be at least <code>1</code>. But for this program you want the user to provide a command-line argument, <code>k</code>, in which case <code>argc</code> should be <code>2</code>. Of course, if the user provides more than one command-line argument at the prompt, <code>argc</code> could be greater than <code>2</code>, in which case, again, your program should print an error and return <code>1</code>.</p>
</div>
<div class="paragraph">
<p>Now, just because the user types an integer at the prompt, that doesn&#8217;t mean their input will be automatically stored in an <code>int</code>. Au contraire, it will be stored as a <code>string</code> that just so happens to look like an <code>int</code>!  And so you&#8217;ll need to convert that <code>string</code> to an actual <code>int</code>. As luck would have it, a function, <a href="https://reference.cs50.net/stdlib/atoi"><code>atoi</code></a>, exists for exactly that purposes. Here&#8217;s how you might use it:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-kt">int</span> <span class="tok-n">k</span> <span class="tok-o">=</span> <span class="tok-n">atoi</span><span class="tok-p">(</span><span class="tok-n">argv</span><span class="tok-p">[</span><span class="tok-mi">1</span><span class="tok-p">]);</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Notice, this time, we&#8217;ve declared <code>k</code> as an actual <code>int</code> so that you can actually do some arithmetic with it.</p>
</div>
<div class="paragraph">
<p>Because <code>atoi</code> is declared in <code>stdlib.h</code>, you&#8217;ll want to <code>#include</code> that header file atop your own code. (Technically, your code will compile without it there, since we already <code>#include</code> it in <code>cs50.h</code>. But best not to trust another library to <code>#include</code> header files you know you need.)</p>
</div>
<div class="paragraph">
<p>Okay, so once you&#8217;ve got <code>k</code> stored as an <code>int</code>, you&#8217;ll need to ask the user for some plaintext. Odds are CS50&#8217;s own <code>get_string</code> can help you with that.</p>
</div>
<div class="paragraph">
<p>Once you have both <code>k</code> and some plaintext, <code>p</code>, it&#8217;s time to encrypt the latter with the former. Recall that you can iterate over the characters in a <code>string</code>, printing each one at a time, with code like the below:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-k">for</span> <span class="tok-p">(</span><span class="tok-kt">int</span> <span class="tok-n">i</span> <span class="tok-o">=</span> <span class="tok-mi">0</span><span class="tok-p">,</span> <span class="tok-n">n</span> <span class="tok-o">=</span> <span class="tok-n">strlen</span><span class="tok-p">(</span><span class="tok-n">p</span><span class="tok-p">);</span> <span class="tok-n">i</span> <span class="tok-o">&lt;</span> <span class="tok-n">n</span><span class="tok-p">;</span> <span class="tok-n">i</span><span class="tok-o">++</span><span class="tok-p">)</span>
<span class="tok-p">{</span>
    <span class="tok-n">printf</span><span class="tok-p">(</span><span class="tok-s">&quot;%c&quot;</span><span class="tok-p">,</span> <span class="tok-n">p</span><span class="tok-p">[</span><span class="tok-n">i</span><span class="tok-p">]);</span>
<span class="tok-p">}</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>In other words, just as <code>argv</code> is an array of strings, so is a <code>string</code> an array of chars. And so you can use square brackets to access individual characters in strings just as you can individual strings in <code>argv</code>. Neat, eh?  Of course, printing each of the characters in a string one at a time isn&#8217;t exactly cryptography. Well, maybe technically if <em>k</em> is 0. But the above should help you help Caesar implement his cipher!</p>
</div>
<div class="paragraph">
<p>Incidentally, you&#8217;ll need to <code>#include</code> yet another header file in order to use <a href="https://reference.cs50.net/string/strlen"><code>strlen</code></a>.</p>
</div>
<div class="paragraph">
<p>Besides <code>atoi</code>, you might find some handy functions documented at <a href="https://reference.cs50.net/">reference.cs50.net</a> under <strong>ctype.h</strong> and <strong>stdlib.h</strong>. For instance, <code>isalpha</code> might prove helpful when iterating over plaintext&#8217;s characters.</p>
</div>
<div class="paragraph">
<p>And, with regard to wrapping around from <code>Z</code> to <code>A</code> (or <code>z</code> to <code>a</code>), don&#8217;t forget about <code>%</code>, C&#8217;s modulo operator. You might also want to check out <a href="http://asciichart.com/" class="bare">http://asciichart.com/</a>, which reveals the ASCII codes for more than just alphabetical characters, just in case you find yourself printing some characters accidentally.</p>
</div>
</div>
</div>
</div>
</body>
</html>

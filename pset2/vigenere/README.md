<html>
<body>
<div id="content">
<h1>Vigenère</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that encrypts messages using Vigenère&#8217;s cipher, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./vigenere ABC</span>
plaintext:  <span class="underline">HELLO</span>
ciphertext: HFNLP</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Vigenère&#8217;s cipher improves upon <a href="../caesar/caesar.html">Caesar&#8217;s cipher</a> by encrypting messages using a sequence of keys (or, put another way, a keyword). In other words, if <em>p</em> is some plaintext and <em>k</em> is a keyword (i.e., an alphbetical string, whereby A represents 0, B represents 1, C represents 2, &#8230;&#8203;, and Z represents 25), then each letter, <em>c<sub>i</sub></em>, in the ciphertext, <em>c</em>, is computed as:</p>
</div>
<div class="stemblock">
<div class="content">
\[c_i = (p_i + k_j) \bmod 26\]
</div>
</div>
<div class="paragraph">
<p>Note this cipher&#8217;s use of <em>k<sub>j</sub></em> as opposed to just <em>k</em>. And if <em>k</em> is shorter than <em>p</em>, then the letters in <em>k</em> must be reused cyclically as many times as it takes to encrypt <em>p</em>.</p>
</div>
<div class="paragraph">
<p>In other words, if Vigenère himself wanted to say HELLO to someone confidentially, using a keyword of, say, ABC, he would encrypt the H with a key of 0 (i.e., A), the E with a key of 1 (i.e., B), and the first L with a key of 2 (i.e., C), at which point he&#8217;d be out of letters in the keyword, and so he&#8217;d reuse (part of) it to encrypt the second L with a key of 0 (i.e., A) again, and the O with a key of 1 (i.e., B) again. And so he&#8217;d write HELLO as HFNLP.</p>
</div>
<table class="tableblock frame-all grid-all stretch">
<caption class="title">Table 1. Encrypting HELLO with a keyword of ABC (reused cyclically as ABCAB) yields HFNLP.</caption>
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
<td class="tableblock halign-left valign-middle" rowspan="2"><p class="tableblock"><strong>+ key</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">A</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">B</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">C</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">A</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">B</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">0</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">2</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">0</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">1</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock"><strong>= ciphertext</strong></p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">H</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">F</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">N</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">L</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">P</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Design and implement a program that encrypts messages using Vigenère&#8217;s cipher.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Implement your program in a file called <code>vigenere.c</code> in a directory called <code>vigenere</code>.</p>
</li>
<li>
<p>Your program must accept a single command-line argument: a keyword, <em>k</em>, composed entirely of alphabetical characters.</p>
</li>
<li>
<p>If your program is executed without any command-line arguments, with more than one command-line argument, or with one command-line argument that contains any non-alphabetical character, your program should print an error (of your choice) and exit immediately, with <code>main</code> returning <code>1</code> (thereby signifying an error).</p>
</li>
<li>
<p>Otherwise, your program must proceed to prompt the user for a string of plaintext, <em>p</em>, (as by a prompt for <code>plaintext:</code>) which it must then encrypt according to Vigenère&#8217;s cipher with <em>k</em>, ultimately printing the result (prepended with <code>ciphertext:</code> and ending with a newline) and exiting, with <code>main</code> returning <code>0</code>.</p>
</li>
<li>
<p>With respect to the characters in <em>k</em>, you must treat <code>A</code> and <code>a</code> as 0, <code>B</code> and <code>b</code> as 1, &#8230;&#8203; , and <code>Z</code> and <code>z</code> as 25.</p>
</li>
<li>
<p>Your program must only apply Vigenère&#8217;s cipher to a character in <em>p</em> if that character is a letter. All other characters (numbers, symbols, spaces, punctuation marks, etc.) must be outputted unchanged. Moreover, if your code is about to apply the <em>j<sup>th</sup></em> character of <em>k</em> to the <em>i<sup>th</sup></em> character of <em>p</em>, but the latter proves to be a non-alphabetical character, you must wait to apply that <em>j<sup>th</sup></em> character of <em>k</em> to the next alphabetical character in <em>p</em>; you must not yet advance to the next character in <em>k</em>.</p>
</li>
<li>
<p>Your program must preserve the case of each letter in <em>p</em>.</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./vigenere 13</span>
Usage: ./vigenere k</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./vigenere</span>
Usage: ./vigenere k</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./vigenere bacon and eggs</span>
Usage: ./vigenere k</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./vigenere bacon</span>
plaintext: <span class="underline">Meet me at the park at eleven am</span>
ciphertext: Negh zf av huf pcfx bt gzrwep oz</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Not sure where to begin? As luck would have it, this program&#8217;s pretty similar to caesar! Only this time, you need to decide which character in <em>k</em> to use as you iterate from character to character in <em>p</em>.</p>
</div>
</div>
</div>
</div>
</body>
</html>

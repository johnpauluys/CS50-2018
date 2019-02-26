<html>
<body>
<div id="content">
                <h1>Resize</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that resizes BMPs, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./resize 4 small.bmp large.bmp</span></code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Be sure you&#8217;re familiar with the structure of 24-bit uncompressed BMPs, as introduced in <a href="../../whodunit/whodunit">Whodunit</a>.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="distribution"><a class="link" href="#distribution">Distribution</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="downloading"><a class="link" href="#downloading">Downloading</a></h3>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ wget <a href="http://cdn.cs50.net/2017/fall/psets/4/resize.zip" class="bare">http://cdn.cs50.net/2017/fall/psets/4/resize.zip</a>
$ unzip resize.zip
$ rm resize.zip
$ cd resize
$ ls
bmp.h  copy.c  large.bmp  small.bmp  smiley.bmp</code></pre>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program called <code>resize</code> that resizes (i.e., enlarges) 24-bit uncompressed BMPs by a factor of <code>n</code>.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Implement your program in a file called <code>resize.c</code> in a directory called <code>resize</code>.</p>
</li>
<li>
<p>Your program should accept exactly three command-line arguments, whereby</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p>the first (<code>n</code>) must be a positive integer less than or equal to <code>100</code>,</p>
</li>
<li>
<p>the second must be the name of a BMP to be resized, and</p>
</li>
<li>
<p>the third must be the name of the resized version to be written.</p>
</li>
</ul>
</div>
</div>
</div>
<div class="paragraph">
<p>+ If your program is not executed with such, it should remind the user of correct usage, as with <code>fprintf</code> (to <code>stderr</code>), and <code>main</code> should return <code>1</code>.</p>
</div>
</li>
<li>
<p>Your program, if it uses <code>malloc</code>, must not leak any memory.</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./resize</span>
Usage: ./resize n infile outfile
$ <span class="underline">echo $?</span>
1</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./resize 2 small.bmp larger.bmp</span>
$ <span class="underline">echo $?</span>
0</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>With a program like this, we could have created <code>large.bmp</code> out of <code>small.bmp</code> by resizing the latter by a factor of 4 (i.e., by multiplying both its width and its height by 4), per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>./resize 4 small.bmp large.bmp</code></pre>
</div>
</div>
<div class="paragraph">
<p>You&#8217;re welcome to get started by copying (yet again) <code>copy.c</code> and naming the copy <code>resize.c</code>. But spend some time thinking about what it means to resize a BMP. (You may assume that <code>n</code> times the size of <code>infile</code> will not exceed 2<sup>32</sup> - 1.) Decide which of the fields in <code>BITMAPFILEHEADER</code> and <code>BITMAPINFOHEADER</code> you might need to modify. Consider whether or not you&#8217;ll need to add or subtract padding to scanlines. And do be sure to support a value of <code>1</code> for <code>n</code>, the result of which should be an <code>outfile</code> with dimensions identical to <code>infile</code>'s.</p>
</div>
<div class="paragraph">
<p>If you happen to use <code>malloc</code>, be sure to use <code>free</code> so as not to leak memory. Try using <code>valgrind</code> to check for any leaks!</p>
</div>
</div>
</div>
</body>
</html>

<html>
<body>
<div id="content">
<h1>Mario</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that prints out a double half-pyramid of a specified height, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./mario</span>
Height: <span class="underline">4</span>
   #  #
  ##  ##
 ###  ###
####  ####</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Toward the beginning of World 1-1 in Nintendo&#8217;s Super Mario Brothers, Mario must hop over two "half-pyramids" of blocks as he heads toward a flag pole.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>Write, in a file called <code>mario.c</code> in your <code>~/workspace/pset1/mario/more/</code> directory, a program that recreates these half-pyramids using hashes (<code>#</code>) for blocks.</p>
</li>
<li>
<p>To make things more interesting, first prompt the user for the half-pyramids' heights, a non-negative integer no greater than <code>23</code>. (The height of the half-pyramids pictured above happens to be <code>4</code>, the width of each half-pyramid <code>4</code>, with an a gap of size <code>2</code> separating them.)</p>
</li>
<li>
<p>If the user fails to provide a non-negative integer no greater than <code>23</code>, you should re-prompt for the same again.</p>
</li>
<li>
<p>Then, generate (with the help of <code>printf</code> and one or more loops) the desired half-pyramids.</p>
</li>
<li>
<p>Take care to left-align the bottom-left corner of the left-hand half-pyramid with the left-hand edge of your terminal window.</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./mario</span>
Height: <span class="underline">4</span>
   #  #
  ##  ##
 ###  ###
####  ####</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./mario</span>
Height: <span class="underline">0</span></code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./mario</span>
Height: <span class="underline">-5</span>
Height: <span class="underline">4</span>
   #  #
  ##  ##
 ###  ###
####  ####</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./mario</span>
Height: <span class="underline">-5</span>
Height: <span class="underline">five</span>
Height: <span class="underline">40</span>
Height: <span class="underline">24</span>
Height: <span class="underline">4</span>
   #  #
  ##  ##
 ###  ###
####  ####</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Try to establish a relationship between (a) the height the user would like the pyramid to be, (b) what row is currently being printed, and (c) how many spaces and how many hashes are in that row. Once you establish the formula, you can translate that to C!</p>
</div>
</div>
</div>
</div>
</body>
    
</html>

<html>
<div id="content">
<h1>Mario</h1>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Toward the end of World 1-1 in Nintendo&#8217;s Super Mario Brothers, Mario must ascend a "half-pyramid" of blocks before leaping (if he wants to maximize his score) toward a flag pole. Below is a screenshot.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>Write, in a file called <code>mario.c</code> in <code>~/workspace/pset1/mario/less/</code>, a program that recreates this half-pyramid using hashes (<code>#</code>) for blocks.</p>
</li>
<li>
<p>To make things more interesting, first prompt the user for the half-pyramid&#8217;s height, a non-negative integer no greater than <code>23</code>. (The height of the half-pyramid pictured above happens to be <code>8</code>.)</p>
</li>
<li>
<p>If the user fails to provide a non-negative integer no greater than <code>23</code>, you should re-prompt for the same again.</p>
</li>
<li>
<p>Then, generate (with the help of <code>printf</code> and one or more loops) the desired half-pyramid.</p>
</li>
<li>
<p>Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.</p>
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
   ##
  ###
 ####
#####</code></pre>
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
   ##
  ###
 ####
#####</code></pre>
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
   ##
  ###
 ####
#####</code></pre>
</div>
</div>
</div>
</div>
            </div>
        </body>
    
</html>

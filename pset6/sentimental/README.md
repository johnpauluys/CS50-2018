<html>
<body>
<div id="content">
                <h1>Sentimental</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Port <code>hello.c</code> to <code>hello.py</code>.</p>
</li>
<li>
<p>Port <code>mario.c</code> to <code>mario.py</code>.</p>
</li>
<li>
<p>Port <code>cash.c</code> to <code>cash.py</code> or <code>credit.c</code> to <code>credit.py</code>.</p>
</li>
<li>
<p>Port <code>caesar.c</code> to <code>caesar.py</code>, <code>vigenere.c</code> to <code>vigenere.py</code>, or <code>crack.c</code> to <code>crack.py</code>.</p>
</li>
</ol>
</div>
</div>
</div>
<div class="sect1">
<h2 id="problems"><a class="link" href="#problems">Problems</a></h2>
<div class="sectionbody">
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Implement the below exactly as specified but in Python:</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p><a href="../../../../../problems/hello/hello.html">Hello</a>, in <code>pset6/hello/hello.py</code></p>
</li>
</ul>
</div>
</div>
</div>
</li>
<li>
<p>Implement either of the below exactly as specified but in Python:</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p><a href="../../../../../problems/mario/less/mario.html">Mario</a>, less comfortable, in <code>pset6/mario/mario.py</code></p>
</li>
<li>
<p><a href="../../../../../problems/mario/more/mario.html">Mario</a>, more comfortable, in <code>pset6/mario/mario.py</code></p>
</li>
</ul>
</div>
</div>
</div>
</li>
<li>
<p>Implement either of the below exactly as specified but in Python:</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p><a href="../../../../../problems/cash/cash.html">Cash</a>, less comfortable, in <code>pset6/cash/cash.py</code></p>
</li>
<li>
<p><a href="../../../../../problems/credit/credit.html">Credit</a>, more comfortable, in <code>pset6/credit/credit.py</code></p>
</li>
</ul>
</div>
</div>
</div>
</li>
<li>
<p>Implement any (one) of the below exactly as specified but in Python:</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p><a href="../../2/caesar/caesar.html">Caesar</a>, less comfortable, in <code>pset6/caesar/caesar.py</code></p>
</li>
<li>
<p><a href="../../2/vigenere/vigenere.html">Vigenère</a>, less comfortable, in <code>pset6/vigenere/vigenere.py</code></p>
</li>
<li>
<p><a href="../../2/crack/crack.html">Crack</a>, more comfortable, in <code>pset6/crack/crack.py</code></p>
</li>
</ul>
</div>
</div>
</div>
</li>
</ol>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>Be sure to use Python 3, not Python 2. The former is installed by default on CS50 IDE, but if Google leads you to Python&#8217;s official documentation, be sure the URLs begin with <a href="https://docs.python.org/3/" class="bare">https://docs.python.org/3/</a>, not <a href="https://docs.python.org/2/" class="bare">https://docs.python.org/2/</a>.</p>
</li>
<li>
<p>If a program is in a file called, say, <code>foo.py</code>, you can run that program with <code>python foo.py</code>.</p>
</li>
<li>
<p>For Hello, Mario, Greedy, Credit, Caesar, Vigenère, and Crack, it is <strong>reasonable</strong> to look at your own implementations thereof in C and others' implementations thereof in C, including the staff&#8217;s implementations thereof (and postmortems) in C. It is <strong>not reasonable</strong> to look at others' implementations of the same in Python.</p>
</li>
<li>
<p>Consider this problem set an opportunity not only to port your own prior work from C to Python but to improve upon your earlier designs using lessons learned since!</p>
</li>
<li>
<p>When porting code from C to Python in CS50 IDE, you might want to select <strong>View &gt; Layout &gt; Horizontal Split</strong> so that you can see both side by side.</p>
</li>
<li>
<p>Insofar as a goal of these problems is to teach you how to teach yourself a new language, keep in mind that these acts are not only <strong>reasonable</strong>, per the syllabus, but encouraged toward that end:</p>
<div class="ulist">
<ul>
<li>
<p>Incorporating a few lines of code that you find online or elsewhere into your own code, provided that those lines are not themselves solutions to assigned problems and that you cite the lines' origins.</p>
</li>
<li>
<p>Turning to the web or elsewhere for instruction beyond the course&#8217;s own, for references, and for solutions to technical difficulties, but not for outright solutions to problem set&#8217;s problems or your own final project.</p>
</li>
</ul>
</div>
</li>
<li>
<p>You&#8217;re welcome to use the CS50 Library for Python, which includes <code>get_float</code>, <code>get_int</code>, and <code>get_string</code>. Just remember to include any of</p>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>from cs50 import get_float
from cs50 import get_int
from cs50 import get_string</code></pre>
</div>
</div>
<div class="paragraph">
<p>atop your code. Or you can use <a href="https://docs.python.org/3/library/functions.html#input"><code>input</code></a> and validate users' input yourself.</p>
</div>
</li>
<li>
<p>You might find <a href="https://docs.python.org/3/library/functions.html#chr"><code>chr</code></a> and/or <a href="https://docs.python.org/3/library/functions.html#ord"><code>ord</code></a> of help.</p>
</li>
<li>
<p>You might find these references of interest:</p>
<div class="ulist">
<ul>
<li>
<p><a href="https://docs.python.org/3/reference/index.html">The Python Language Reference</a></p>
</li>
<li>
<p><a href="https://docs.python.org/3/library/">The Python Standard Library</a></p>
</li>
<li>
<p><a href="https://docs.python.org/3/tutorial/index.html">The Python Tutorial</a></p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</div>
</div>
</div>
</body>
</html>

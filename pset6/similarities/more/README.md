<html>
<body>
<div id="content">
<h1>Similarities</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Implement a program that measures the edit distance between two strings.</p>
</li>
<li>
<p>Implement a web app that depicts the costs of transforming one string into another.</p>
</li>
</ol>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Determining whether two strings are identical is (relatively!) trivial: iterate over the characters in each, checking whether each and every one is identical. But it&#8217;s non-trivial to quantify just how dissimilar two (non-identical) strings are. And it can be time-consuming, as there are multiple (and often many!) ways to transform one string into the other.</p>
</div>
<div class="paragraph">
<p>The challenge ahead is to measure the "edit distance" between two strings, the minimal number of additions, deletions, and/or edits necessary to transform one string into the other.</p>
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
<pre class="pygments highlight"><code>$ wget <a href="http://cdn.cs50.net/2017/fall/psets/6/similarities/more/similarities.zip" class="bare">http://cdn.cs50.net/2017/fall/psets/6/similarities/more/similarities.zip</a>
$ unzip similarities.zip
$ rm similarities.zip
$ cd similarities
$ chmod a+x score
$ ls
application.py  helpers.py  requirements.txt  score*  static/  templates/</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="understanding"><a class="link" href="#understanding">Understanding</a></h3>
<div class="sect3">
<h4 id="score"><a class="link" href="#score"><code>score</code></a></h4>
<div class="paragraph">
<p>Open up <code>score</code>. Suffice it to say that file&#8217;s name doesn&#8217;t end in <code>.py</code>, even though the file contains a program written in Python. But that&#8217;s okay! Notice the "shebang" atop the file:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>#!/usr/bin/env python3</code></pre>
</div>
</div>
<div class="paragraph">
<p>That line tells a computer to interpret (i.e., run) the program using <code>python3</code> (aka <code>python</code> on CS50 IDE), an interpreter that understands Python 3.</p>
</div>
<div class="paragraph">
<p>Notice how the file defines a function called <code>main</code> and calls that function toward the bottom of the file. Defining <code>main</code> isn&#8217;t strictly necessary in Python, but it&#8217;s not uncommon.</p>
</div>
<div class="paragraph">
<p>Notice how <code>score</code> uses Python&#8217;s <a href="https://docs.python.org/3/library/argparse.html">argparse</a> module in order to parse two command-line arguments, <code>FILE1</code> and <code>FILE2</code>, the files to compare. The program then tries to read the contents of those files into strings, <code>file1</code> and <code>file2</code>. If something goes wrong, as indicated by an <code>IOError</code>, the "exception" is caught. See <a href="https://docs.python.org/3/tutorial/errors.html" class="bare">https://docs.python.org/3/tutorial/errors.html</a> for more on exceptions.</p>
</div>
<div class="paragraph">
<p>Finally, the program passes those strings to <code>distances</code>, a function we&#8217;ll soon see, and ultimately prints the edit distance between the two files!</p>
</div>
</div>
</div>
<div class="sect2">
<h3 id="helpers-py"><a class="link" href="#helpers-py"><code>helpers.py</code></a></h3>
<div class="paragraph">
<p>Open up <code>helpers.py</code>. Ah, the familiar <code>TODO</code>. Declared in this file is a function called <code>distances</code> that takes two strings as arguments, <code>a</code> and <code>b</code>, and is supposed to return (via a matrix of costs) the edit distance between one and the other. At the moment, though, it simply returns an empty two-dimensional <code>list</code>!</p>
</div>
<div class="paragraph">
<p>This file also defines an "enumeration" (i.e., <code>Enum</code>) that essentially defines three constants, each of which represents an operation via which a string might be transformed into another: <code>Operation.DELETED</code>, <code>Operation.INSERTED</code>, and <code>Operation.SUBSTITUTED</code>.</p>
</div>
</div>
<div class="sect2">
<h3 id="application-py"><a class="link" href="#application-py"><code>application.py</code></a></h3>
<div class="paragraph">
<p>Open up <code>application.py</code>. This file implements a web application that, ultimately, will allow you to visualize the edit distance between two strings as well as the operations necessary to transform one into the other at minimal cost. No need to understand the entirety of this file, but notice how <code>score</code> infers from the matrix returned by <code>distances</code> the sequence of operations that yield that minimal cost.</p>
</div>
</div>
<div class="sect2">
<h3 id="templateslayout-html"><a class="link" href="#templateslayout-html"><code>templates/layout.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/layout.html</code>. In this file is a template for the web application&#8217;s overall layout. Odds are you&#8217;ll recognize a few of the HTML tags therein and notice a few new ones. Notice, in particular, how the template uses Bootstrap, a popular library. In fact, we based this template on their own <a href="http://getbootstrap.com/docs/4.0/getting-started/introduction/">starter template</a>.</p>
</div>
</div>
<div class="sect2">
<h3 id="templatesindex-html"><a class="link" href="#templatesindex-html"><code>templates/index.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/index.html</code>. Ah, another <code>TODO</code>. Notice how this template "extends" <code>layout.html</code>, which is to say that <code>layout.html</code> is the "mold" from which <code>index.html</code> itself will be made. The <code>block</code> defined in <code>index.html</code> will effectively get plugged into the placeholder for <code>block</code> in <code>layout.html</code>.</p>
</div>
<div class="paragraph">
<p>Ultimately, this file will contain the form via which users will be able to submit two strings to your web application for comparison.</p>
</div>
</div>
<div class="sect2">
<h3 id="templatesscore-html"><a class="link" href="#templatesscore-html"><code>templates/score.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/score.html</code>. We took the liberty of implementing this file for you. Thanks to its use of some CSS (particularly a class called <code>row</code>), it ensures that <code>matrix.html</code> will fill the top half of a browser&#8217;s viewport and that <code>log.html</code> will fill the bottom half of the same.</p>
</div>
</div>
<div class="sect2">
<h3 id="templatesmatrix-html"><a class="link" href="#templatesmatrix-html"><code>templates/matrix.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/matrix.html</code>. Ah, another <code>TODO</code>. It&#8217;s via this file that you&#8217;ll need to generate an HTML table that depicts the costs via which one string can be transformed into another.</p>
</div>
</div>
<div class="sect2">
<h3 id="templateslog-html"><a class="link" href="#templateslog-html"><code>templates/log.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/log.html</code>. Phew, looks like we implemented this file for you. Indeed, it&#8217;s via this file that your web app will generate an HTML table that summarizes the operations via which one string can be transformed into another.</p>
</div>
</div>
<div class="sect2">
<h3 id="templateserror-html"><a class="link" href="#templateserror-html"><code>templates/error.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/error.html</code>. In this file is a template with which any HTTP errors will be displayed. It happens to use Bootstrap&#8217;s <a href="https://getbootstrap.com/docs/4.0/components/jumbotron/">Jumbotron</a> feature.</p>
</div>
</div>
<div class="sect2">
<h3 id="staticstyles-css"><a class="link" href="#staticstyles-css"><code>static/styles.css</code></a></h3>
<div class="paragraph">
<p>Open up <code>static/styles.css</code>. In this file are some CSS properties that collectively implement your web application&#8217;s user interface. Essentially, they modify some of Bootstrap&#8217;s own defaults.</p>
</div>
<div class="sect3">
<h4 id="requirements-txt"><a class="link" href="#requirements-txt"><code>requirements.txt</code></a></h4>
<div class="paragraph">
<p>Open up <code>requirements.txt</code> (without changing it, though you can later if you&#8217;d like). This file specifies the libraries, one per line, on which all of this functionality depends.</p>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="helpers-py-2"><a class="link" href="#helpers-py-2"><code>helpers.py</code></a></h3>
<div class="sect3">
<h4 id="distances"><a class="link" href="#distances"><code>distances</code></a></h4>
<div class="paragraph">
<p>Implement <code>distances</code> in such a way that, given two strings, <code>a</code> and <code>b</code>, it calculates the edit distance from <code>a</code> to <code>b</code>, returning (as a <code>list</code> of <code>lists</code>) the matrix of operational costs incurred along the way. Treat the matrix&#8217;s top-left corner as <code>[0][0]</code> and the matrix&#8217;s bottom-right corner as <code>[len(a)][len(b)]</code>. Stored in each element of the matrix should be a <code>tuple</code>, <code>(cost, operation)</code>, where <code>cost</code> is an <code>int</code> and <code>operation</code> is an <code>Operation</code>.</p>
</div>
</div>
</div>
<div class="sect2">
<h3 id="templatesindex-html-2"><a class="link" href="#templatesindex-html-2"><code>templates/index.html</code></a></h3>
<div class="paragraph">
<p>Implement <code>templates/index.html</code> in such a way that it contains an HTML form via which a user can submit:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>a string called <code>string1</code></p>
</li>
<li>
<p>a string called <code>string2</code></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>You&#8217;re welcome to look at the HTML of the staff&#8217;s solution as needed, but do try to figure out the right syntax on your own first, as via <a href="https://www.google.com/search?q=html+forms!" class="bare">https://www.google.com/search?q=html+forms!</a></p>
</div>
</div>
<div class="sect2">
<h3 id="templatesmatrix-html-2"><a class="link" href="#templatesmatrix-html-2"><code>templates/matrix.html</code></a></h3>
<div class="paragraph">
<p>Implement <code>templates/matrix.html</code> in such a way that it generates, using <a href="http://jinja.pocoo.org/">Jinja2</a>, a visualization of a matrix returned by <code>distances</code> (given some <code>a</code> and <code>b</code>) via an HTML table. In each cell of the table should be only a cost, not an operation. Along the lefmost column should be the characters from <code>a</code>, each in its own cell (and row); along the topmost row should be the characters from <code>b</code>, each in its cell (and column).</p>
</div>
</div>
</div>
</div>
<div class="sect2">
<h3 id="web"><a class="link" href="#web">Web</a></h3>
<div class="paragraph">
<p><a href="http://similarities.cs50.net/more" class="bare">http://similarities.cs50.net/more</a></p>
</div>
</div>
</div>
</div>
</div>
</body>
</html>

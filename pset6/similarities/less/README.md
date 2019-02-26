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
<p>Implement a program that compares two files for similarities.</p>
</li>
<li>
<p>Implement a website that highlights similarities across files.</p>
</li>
</ol>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Determining whether two files are identical is (relatively!) trivial: iterate over the characters in each, checking whether each and every one is identical. But determining whether two files are similar is non-trivial. After all, what does it mean to be similar? Perhaps the files have lines in common. Perhaps the files have sentences in common. Perhaps the files have only substrings in common.</p>
</div>
<div class="paragraph">
<p>Suffice it to say, the challenge ahead is to determine if two files are similar!</p>
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
<pre class="pygments highlight"><code>$ wget <a href="http://cdn.cs50.net/2017/fall/psets/6/similarities/less/similarities.zip" class="bare">http://cdn.cs50.net/2017/fall/psets/6/similarities/less/similarities.zip</a>
$ unzip similarities.zip
$ rm similarities.zip
$ cd similarities
$ chmod a+x compare
$ ls
application.py  compare* helpers.py  requirements.txt  static/  templates/</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="understanding"><a class="link" href="#understanding">Understanding</a></h3>
<div class="sect3">
<h4 id="compare"><a class="link" href="#compare"><code>compare</code></a></h4>
<div class="paragraph">
<p>Open up <code>compare</code>. Suffice it to say that file&#8217;s name doesn&#8217;t end in <code>.py</code>, even though the file contains a program written in Python. But that&#8217;s okay! Notice the "shebang" atop the file:</p>
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
<p>Notice how the file defines a function called <code>main</code> and calls that function toward the bottom of the file. Defining <code>main</code> isn&#8217;t strictly necessary in Python, but it is necessary to define functions before you call them. Accordingly, because <code>main</code> calls a function called <code>positive</code>, and because we wanted to keep the "main" part of this program atop the file, it made sense to implement <code>main</code> as a function as well. That way, <code>main</code> doesn&#8217;t get called until the bottom of the file (after <code>positive</code> has been implemented), even though <code>main</code> is implemented atop the file.</p>
</div>
<div class="paragraph">
<p>No need to understand each of the lines in <code>compare</code>, but notice, per its comments, what it does overall: it parses its command-line arguments, reads two files into variables as strings, and compares those strings, and then prints a list of similarities. The strings themselves are compared in one of three ways, as specified by a command-line argument: line by line, sentence by sentence, or substring by substring.</p>
</div>
</div>
</div>
<div class="sect2">
<h3 id="helpers-py"><a class="link" href="#helpers-py"><code>helpers.py</code></a></h3>
<div class="paragraph">
<p>Open up <code>helpers.py</code>. Ah, the familiar <code>TODO</code>. Declared in this file are three functions, each of which is meant to implement a different algorithm: <code>lines</code>, <code>sentences</code>, and <code>substrings</code>. At the moment, each of them returns an empty list. But not for long!</p>
</div>
</div>
<div class="sect2">
<h3 id="application-py"><a class="link" href="#application-py"><code>application.py</code></a></h3>
<div class="paragraph">
<p>Open up <code>application.py</code>. This file implements a web application that, ultimately, will allow you to run any of those three algorithms on any two text files. No need to understand the entirety of this file, particularly <code>highlight</code> and <code>errorhandler</code>. But know that <code>highlight</code>, given a string, <code>s</code>, and a list of other strings, <code>strings</code>, highlights (by wrapping them in HTML <code>span</code> tags) all instances of the former in the latter. And <code>errorhandler</code> ensures that any HTTP errors are displayed on a page of their own.</p>
</div>
<div class="paragraph">
<p>But do read through <code>index</code> and <code>compare</code>, the latter of which handles form submissions.</p>
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
<p>Open up <code>templates/index.html</code>. Ah, the final <code>TODO</code>. Notice how this template "extends" <code>layout.html</code>, which is to say that <code>layout.html</code> is the "mold" from which <code>index.html</code> itself will be made. The <code>block</code> defined in <code>index.html</code> will effectively get plugged into the placeholder for <code>block</code> in <code>layout.html</code>.</p>
</div>
<div class="paragraph">
<p>Ultimately, this file will contain the form via which users will be able to upload two files to your web application for comparison via one of your three algorithms.</p>
</div>
</div>
<div class="sect2">
<h3 id="templatescompare-html"><a class="link" href="#templatescompare-html"><code>templates/compare.html</code></a></h3>
<div class="paragraph">
<p>Open up <code>templates/compare.html</code>. We took the liberty of implementing this file for you. Thanks to its use of some CSS (particularly a class called <code>col-6</code>), it ensures that users' files, once uploaded and highlighted, will be displayed side by side.</p>
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
<h4 id="lines"><a class="link" href="#lines"><code>lines</code></a></h4>
<div class="paragraph">
<p>Implement <code>lines</code> in such a way that, given two strings, <code>a</code> and <code>b</code>, it returns a <code>list</code> of the lines that are, identically, in both <code>a</code> and <code>b</code>. The <code>list</code> should not contain any duplicates. Assume that lines in <code>a</code> and <code>b</code> will be be separated by <code>\n</code>, but the strings in the returned <code>list</code> should not end in <code>\n</code>. If both <code>a</code> and <code>b</code> contain one or more blank lines (i.e., a <code>\n</code> immediately preceded by no other characters), the returned <code>list</code> should include an empty string (i.e., <code>""</code>).</p>
</div>
</div>
<div class="sect3">
<h4 id="sentences"><a class="link" href="#sentences"><code>sentences</code></a></h4>
<div class="paragraph">
<p>Implement <code>sentences</code> in such a way that, given two strings, <code>a</code> and <code>b</code>, it returns a <code>list</code> of the <em>unique</em> English sentences that are, identically, present in both <code>a</code> and <code>b</code>. The <code>list</code> should not contain any duplicates. Use <code>sent_tokenize</code> from the Natural Language Toolkit to "tokenize" (i.e., separate) each string into a <code>list</code> of sentences. It can be imported with:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="python"><span></span><span class="tok-kn">from</span> <span class="tok-nn">nltk.tokenize</span> <span class="tok-kn">import</span> <span class="tok-n">sent_tokenize</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Per its <a href="http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize">documentation</a>, <code>sent_tokenize</code>, given a <code>str</code> as input, returns a <code>list</code> of English sentences therein. It assumes that its input is indeed English text (and not, e.g., code, which might coincidentally have periods too).</p>
</div>
</div>
<div class="sect3">
<h4 id="substrings"><a class="link" href="#substrings"><code>substrings</code></a></h4>
<div class="paragraph">
<p>Implement <code>substrings</code> in such a way that, given two strings, <code>a</code> and <code>b</code>, and an integer, <code>n</code>, it returns a <code>list</code> of all substrings of length <code>n</code> that are, identically, present in both <code>a</code> and <code>b</code>. The <code>list</code> should not contain any duplicates.</p>
</div>
<div class="paragraph">
<p>Recall that a substring of length <code>n</code> of some string is just a sequence of <code>n</code> characters from that string. For instance, if <code>n</code> is <code>2</code> and the string is <code>Yale</code>, there are three possible substrings of length <code>2</code>: <code>Ya</code>, <code>al</code>, and <code>le</code>. Meanwhile, if <code>n</code> is <code>1</code> and the string is <code>Harvard</code>, there are seven possible substrings of length <code>1</code>: <code>H</code>, <code>a</code>, <code>r</code>, <code>v</code>, <code>a</code>, <code>r</code>, and <code>d</code>. But once we eliminate duplicates, there are only five unique substrings: <code>H</code>, <code>a</code>, <code>r</code>, <code>v</code>, and <code>d</code>.</p>
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
<p>a file called <code>file1</code></p>
</li>
<li>
<p>a file called <code>file2</code></p>
</li>
<li>
<p>a value of <code>lines</code>, <code>sentences</code>, or <code>substrings</code> for an <code>input</code> called <code>algorithm</code></p>
</li>
<li>
<p>a number called <code>length</code></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>You&#8217;re welcome to look at the HTML of the staff&#8217;s solution as needed, but do try to figure out the right syntax on your own first, as via <a href="https://www.google.com/search?q=html+forms!" class="bare">https://www.google.com/search?q=html+forms!</a></p>
</div>
</div>
</div>
</div>
</body>
</html>

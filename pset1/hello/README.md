<div id="content">
<h1>Hello</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that prints out a simple greeting to the user, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./hello</span>
hello, world</code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Shall we have you write your first program? Inside of your <strong>pset1</strong> folder, create a new folder called <strong>hello</strong>. Then create a new file and immediately save it as <strong>hello.c</strong> inside of your <strong>hello</strong> folder (which should be inside of your <strong>pset1</strong> folder). Be sure to name the file just as we have, in all lowercase; files' and folders' names in Linux are "case-sensitive." Proceed to write your first program by typing precisely these lines into the file:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-cp">#include</span> <span class="tok-cpf">&lt;stdio.h&gt;</span><span class="tok-cp"></span>

<span class="tok-kt">int</span> <span class="tok-nf">main</span><span class="tok-p">(</span><span class="tok-kt">void</span><span class="tok-p">)</span>
<span class="tok-p">{</span>
    <span class="tok-n">printf</span><span class="tok-p">(</span><span class="tok-s">&quot;hello, world</span><span class="tok-se">\n</span><span class="tok-s">&quot;</span><span class="tok-p">);</span>
<span class="tok-p">}</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Notice how CS50 IDE adds "syntax highlighting" (i.e., color) as you type, though CS50 IDE&#8217;s choice of colors might differ from this problem set&#8217;s. Those colors aren&#8217;t actually saved inside of the file itself; they&#8217;re just added by CS50 IDE to make certain syntax stand out. Had you not saved the file as <code>hello.c</code> from the start, CS50 IDE wouldn&#8217;t know (per the filename&#8217;s extension) that you&#8217;re writing C code, in which case those colors would be absent.</p>
</div>
<div class="paragraph">
<p>Do be sure that you type this program just right, else you&#8217;re about to experience your first bug! In particular, capitalization matters, so don&#8217;t accidentally capitalize words (unless they&#8217;re between those two quotes). And don&#8217;t overlook that one semicolon. C is quite nitpicky!</p>
</div>
<div class="paragraph">
<p>When done typing, select <strong>File &gt; Save</strong> (or hit command- or control-s), but don&#8217;t quit. Recall that the red dot atop the tab should then disappear. Click anywhere in the terminal window beneath your code, and be sure that you&#8217;re inside of <code>~/workspace/pset1/hello/</code>. (Remember how? If not, type <code>cd</code> and then Enter, followed by <code>cd pset1/hello/</code> and then Enter.) Your prompt should be:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>~/workspace/pset1/hello/ $</code></pre>
</div>
</div>
<div class="paragraph">
<p>Let&#8217;s confirm that <code>hello.c</code> is indeed where it should be. Type</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>ls</code></pre>
</div>
</div>
<div class="paragraph">
<p>followed by Enter, and you should see <code>hello.c</code>? If not, no worries; you probably just missed a small step. Best to restart these past several steps or ask for help!</p>
</div>
<div class="paragraph">
<p>Assuming you indeed see <code>hello.c</code>, let&#8217;s try to compile! Cross your fingers and then type</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>make hello</code></pre>
</div>
</div>
<div class="paragraph">
<p>at the prompt, followed by Enter. (Well, maybe don&#8217;t cross your fingers whilst typing.) To be clear, type only <code>hello</code> here, not <code>hello.c</code>. If all that you see is another, identical prompt, that means it worked! Your source code has been translated to machine code (0s and 1s) that you can now execute. Type</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>./hello</code></pre>
</div>
</div>
<div class="paragraph">
<p>at your prompt, followed by Enter, and you should see the below:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>hello, world</code></pre>
</div>
</div>
<div class="paragraph">
<p>And if you type</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>ls</code></pre>
</div>
</div>
<div class="paragraph">
<p>followed by Enter, you should see a new file, <code>hello</code>, alongside <code>hello.c</code>. The first of those files, <code>hello</code>, should have an asterisk after its name that, in this context, means it&#8217;s "executable," a program that you can execute (i.e., run).</p>
</div>
<div class="paragraph">
<p>If, though, upon running <code>make</code>, you instead see some error(s), it&#8217;s time to debug! (If the terminal window&#8217;s too small to see everything, click and drag its top border upward to increase its height.) If you see an error like "expected declaration" or something just as mysterious, odds are you made a syntax error (i.e., typo) by omitting some character or adding something in the wrong place. Scour your code for any differences vis-à-vis the template above. It&#8217;s easy to miss the slightest of things when learning to program, so do compare your code against ours character by character; odds are the mistake(s) will jump out! Anytime you make changes to your own code, just remember to re-save via <strong>File &gt; Save</strong> (or command- or control-s), then re-click inside of the terminal window, and then re-type</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>make hello</code></pre>
</div>
</div>
<div class="paragraph">
<p>at your prompt, followed by Enter. (Just be sure that you are inside of <code>~/workspace/pset1/hello/</code> within your terminal window, as your prompt will confirm or deny.) If still seeing errors, try "prepending" <code>help50</code> to your command like this:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>help50 make hello</code></pre>
</div>
</div>
<div class="paragraph">
<p>That&#8217;ll pass the output of <code>make hello</code> to a program called <code>help50</code>, which CS50&#8217;s staff wrote. If <code>help50</code> recognizes your error message, it&#8217;ll offer some suggestions (in yellow). Just realize <code>help50</code> is new this year, so odds are it won&#8217;t recognize all error messages just yet!</p>
</div>
<div class="paragraph">
<p>Once you see no more errors, try "executing" (i.e., running) your program by typing</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>./hello</code></pre>
</div>
</div>
<div class="paragraph">
<p>at your prompt, followed by Enter! Hopefully you now see whatever you told <code>printf</code> to print?</p>
</div>
<div class="paragraph">
<p>If not, reach out for help!  Incidentally, if you find the terminal window too small for your tastes, know that you can open one in a bigger tab by clicking the circled plus (+) icon to the right of your <code>hello.c</code> tab.</p>
</div>
</div>
</div>

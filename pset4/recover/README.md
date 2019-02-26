<html>
<body>
<div id="content">
<h1>Recover</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program that recovers JPEGs from a forensic image, per the below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./recover card.raw</span></code></pre>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>In anticipation of this problem, we spent the past several days taking photos of people we know, all of which were saved on a digital camera as JPEGs on a memory card. (Okay, it&#8217;s possible we actually spent the past several days on Facebook instead.) Unfortunately, we somehow deleted them all! Thankfully, in the computer world, "deleted" tends not to mean "deleted" so much as "forgotten." Even though the camera insists that the card is now blank, we&#8217;re pretty sure that&#8217;s not quite true. Indeed, we&#8217;re hoping (er, expecting!) you can write a program that recovers the photos for us!</p>
</div>
<div class="paragraph">
<p>Even though JPEGs are more complicated than BMPs, JPEGs have "signatures," patterns of bytes that can distinguish them from other file formats. Specifically, the first three bytes of JPEGs are</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>0xff 0xd8 0xff</code></pre>
</div>
</div>
<div class="paragraph">
<p>from first byte to third byte, left to right. The fourth byte, meanwhile, is either <code>0xe0</code>, <code>0xe1</code>, <code>0xe2</code>, <code>0xe3</code>, <code>0xe4</code>, <code>0xe5</code>, <code>0xe6</code>, <code>0xe7</code>, <code>0xe8</code>, <code>0xe9</code>, <code>0xea</code>, <code>0xeb</code>, <code>0xec</code>, <code>0xed</code>, <code>0xee</code>, of <code>0xef</code>. Put another way, the fourth byte&#8217;s first four bits are <code>1110</code>.</p>
</div>
<div class="paragraph">
<p>Odds are, if you find this pattern of four bytes on media known to store photos (e.g., my memory card), they demarcate the start of a JPEG. To be fair, you might encounter these patterns on some disk purely by chance, so data recovery isn&#8217;t an exact science.</p>
</div>
<div class="paragraph">
<p>Fortunately, digital cameras tend to store photographs contiguously on memory cards, whereby each photo is stored immediately after the previously taken photo. Accordingly, the start of a JPEG usually demarks the end of another. However, digital cameras often initialize cards with a FAT file system whose "block size" is 512 bytes (B). The implication is that these cameras only write to those cards in units of 512 B. A photo that&#8217;s 1 MB (i.e., 1,048,576 B) thus takes up 1048576 ÷ 512 = 2048 "blocks" on a memory card. But so does a photo that&#8217;s, say, one byte smaller (i.e., 1,048,575 B)! The wasted space on disk is called "slack space." Forensic investigators often look at slack space for remnants of suspicious data.</p>
</div>
<div class="paragraph">
<p>The implication of all these details is that you, the investigator, can probably write a program that iterates over a copy of my memory card, looking for JPEGs' signatures. Each time you find a signature, you can open a new file for writing and start filling that file with bytes from my memory card, closing that file only once you encounter another signature. Moreover, rather than read my memory card&#8217;s bytes one at a time, you can read 512 of them at a time into a buffer for efficiency&#8217;s sake. Thanks to FAT, you can trust that JPEGs' signatures will be "block-aligned." That is, you need only look for those signatures in a block&#8217;s first four bytes.</p>
</div>
<div class="paragraph">
<p>Realize, of course, that JPEGs can span contiguous blocks. Otherwise, no JPEG could be larger than 512 B. But the last byte of a JPEG might not fall at the very end of a block. Recall the possibility of slack space. But not to worry. Because this memory card was brand-new when I started snapping photos, odds are it&#8217;d been "zeroed" (i.e., filled with 0s) by the manufacturer, in which case any slack space will be filled with 0s. It&#8217;s okay if those trailing 0s end up in the JPEGs you recover; they should still be viewable.</p>
</div>
<div class="paragraph">
<p>Now, I only have one memory card, but there are a lot of you! And so I&#8217;ve gone ahead and created a "forensic image" of the card, storing its contents, byte after byte, in a file called <code>card.raw</code>. So that you don&#8217;t waste time iterating over millions of 0s unnecessarily, I&#8217;ve only imaged the first few megabytes of the memory card. But you should ultimately find that the image contains 50 JPEGs.</p>
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
<pre class="pygments highlight"><code>$ mkdir recover
$ cd recover
$ wget http://cdn.cs50.net/2017/fall/psets/4/recover/card.raw
$ ls
card.raw</code></pre>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a program called <code>recover</code> that recovers JPEGs from a forensic image.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Implement your program in a file called <code>recover.c</code> in a directory called <code>recover</code>.</p>
</li>
<li>
<p>Your program should accept exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
+ If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, as with <code>fprintf</code> (to <code>stderr</code>), and <code>main</code> should return <code>1</code>.</p>
</li>
<li>
<p>If the forensic image cannot be opened for reading, your program should inform the user as much, as with <code>fprintf</code> (to <code>stderr</code>), and <code>main</code> should return <code>2</code>.</p>
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
<pre class="pygments highlight"><code>$ <span class="underline">./recover</span>
Usage: ./recover image
$ <span class="underline">echo $?</span>
1</code></pre>
</div>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ <span class="underline">./recover card.raw</span>
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
<p>Odds are you&#8217;ll want to start by creating a file called <code>recover.c</code> (in the same directory as is <code>card.raw</code>). No need for the CS50 Library, but you will want to declare <code>main</code> in such a way that it supports command-line arguments. (Remember how?)</p>
</div>
<div class="paragraph">
<p>Keep in mind that you can open <code>card.raw</code> programmatically with <code>fopen</code>, as with the below, provided <code>argv[1]</code> exists.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="c"><span></span><span class="tok-kt">FILE</span> <span class="tok-o">*</span><span class="tok-n">file</span> <span class="tok-o">=</span> <span class="tok-n">fopen</span><span class="tok-p">(</span><span class="tok-n">argv</span><span class="tok-p">[</span><span class="tok-mi">1</span><span class="tok-p">],</span> <span class="tok-s">&quot;r&quot;</span><span class="tok-p">);</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>When executed, your program should recover every one of the JPEGs from <code>card.raw</code>, storing each as a separate file in your current working directory. Your program should number the files it outputs by naming each <code>###.jpg</code>, where <code>###</code> is three-digit decimal number from <code>000</code> on up. (Befriend <a href="https://reference.cs50.net/stdio/sprintf"><code>sprintf</code></a>.) You need not try to recover the JPEGs' original names. To check whether the JPEGs your program spit out are correct, simply double-click and take a look! If each photo appears intact, your operation was likely a success!</p>
</div>
<div class="paragraph">
<p>Odds are, though, the JPEGs that the first draft of your code spits out won&#8217;t be correct. (If you open them up and don&#8217;t see anything, they&#8217;re probably not correct!) Execute the command below to delete all JPEGs in your current working directory.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>rm *.jpg</code></pre>
</div>
</div>
<div class="paragraph">
<p>If you&#8217;d rather not be prompted to confirm each deletion, execute the command below instead.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>rm -f *.jpg</code></pre>
</div>
</div>
<div class="paragraph">
<p>Just be careful with that <code>-f</code> switch, as it "forces" deletion without prompting you.</p>
</div>
</div>
</div>
</div>
</body>
</html>

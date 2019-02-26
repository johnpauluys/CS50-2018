<html>
<body>
<div id="content">
<h1>Music</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Learn to read sheet music.</p>
</li>
<li>
<p>Learn to read code.</p>
</li>
<li>
<p>Convert musical notes to frequencies.</p>
</li>
<li>
<p>Synthesize songs.</p>
</li>
</ol>
</div>
</div>
</div>
<div class="sect1">
<h2 id="distribution"><a class="link" href="#distribution">Distribution</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Included with this problem is a "distribution," some files that we&#8217;ve written that you&#8217;ll first need to read (and understand!) before contributing improvements of your own. Unlike <code>cs50.h</code> and <code>stdio.h</code> and other header files you&#8217;ve been using for some time, which live somewhere in CS50 IDE, these files will live alongside your own code, where you can see them more easily.</p>
</div>
<div class="sect2">
<h3 id="downloading"><a class="link" href="#downloading">Downloading</a></h3>
<div class="paragraph">
<p>Here&#8217;s how to download it.</p>
</div>
<div class="paragraph">
<p>First, execute</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>cd ~/workspace/pset3/</code></pre>
</div>
</div>
<div class="paragraph">
<p>to ensure you&#8217;re in <code>~/workspace/pset3/</code>. Then, execute</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>wget http://cdn.cs50.net/2017/fall/psets/3/music.zip</code></pre>
</div>
</div>
<div class="paragraph">
<p>to download the distribution code as a ZIP (i.e., compressed file). If you then execute <code>ls</code>, you should see <code>music.zip</code> inside of your <code>pset3</code> directory. To unzip (i.e., uncompress) that file, execut</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>unzip music.zip</code></pre>
</div>
</div>
<div class="paragraph">
<p>and then execute</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>rm music.zip</code></pre>
</div>
</div>
<div class="paragraph">
<p>in order to delete the ZIP file itself. If you execute <code>ls</code>, you should now see a folder called <code>music</code> inside of your <code>pset3</code> directory. Then execute</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>cd music/</code></pre>
</div>
</div>
<div class="paragraph">
<p>in order to change into that directory. And then execute <code>ls</code>. You should see the files and folder below, which collectively compose this problem&#8217;s distribution!</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>Makefile  helpers.c  helpers.h  notes.c  synthesize.c  songs/  wav.c  wav.h</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="understanding"><a class="link" href="#understanding">Understanding</a></h3>
<div class="paragraph">
<p>Let&#8217;s read through those files in order to understand them. Moving forward, reading (and understanding!) someone else&#8217;s code, whether ours or some library&#8217;s, will often be the first step in solving a problem. That way, you can build upon the work of others and solve even more interesting problems yourself!</p>
</div>
<div class="sect3">
<h4 id="songs"><a class="link" href="#songs"><code>songs/</code></a></h4>
<div class="paragraph">
<p>First open up <code>songs/</code>, as with <code>cd</code> or CS50 IDE&#8217;s file browser. In that directory are a bunch of <code>.txt</code> files, inside of which, it turns out, are a number of songs! Because ASCII alone doesn&#8217;t lend itself to beautiful sheet music, we&#8217;ve instead adopted for these files a "machine-readable" format for songs instead. On each line of a file is a note and duration, separated by an <code>@</code>. For instance, atop <code>jeopardy.txt</code> (which you&#8217;re welcome to open) are these lines:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>G4@1/4
C5@1/4
G4@1/4
C4@1/4
G4@1/4
C5@1/4
G4@1/4</code></pre>
</div>
</div>
<div class="paragraph">
<p>The first note in the theme song for Jeopardy is indeed a quarter note (per the <code>1/4</code>), specifically a G in the fourth octave. The second note is also a quarter note, but that one&#8217;s a C in the fifth octave (a few keys to the right of the first one on a piano). Thereafter are five additional quarter notes.</p>
</div>
<div class="paragraph">
<p>Below those first seven lines in <code>jeopardy.txt</code>, notice, are two blank lines, the implication of which is that the seventh note is followed by two eighth rests (or, equivalently, one quarter rest). After those rests, the song resumes, resting only once more several notes later.</p>
</div>
<div class="paragraph">
<p>Make sense? Feel free to look through some of the other <code>.txt</code> files in <code>songs</code>. Cryptic though the files' lines might be at first glance, they&#8217;re really just a top-down translation of (prettier) sheet music to a machine-readable text format, machine-readable in the sense that you&#8217;re soon going to write code that reads those notes and durations!</p>
</div>
</div>
<div class="sect3">
<h4 id="notes-c"><a class="link" href="#notes-c"><code>notes.c</code></a></h4>
<div class="paragraph">
<p>Next open up <code>notes.c</code>. In this file is a program (soon to be called <code>notes</code>) that not only prints the frequencies (in Hz) of all of the notes in an octave, it also outputs a WAV file (an audio file) via which you can hear those same notes. By default, it does so for the fourth octave, but if you pass it a command-line argument (a number between 0 and 8, inclusive), you can see and hear the frequencies of any octave&#8217;s notes.</p>
</div>
<div class="paragraph">
<p>Read through the comments and code in <code>notes.c</code> and try to understand most, if not all, of its lines. Some might look unfamiliar. For instance, by convention, it uses a function called <code>fprintf</code> to print error messages to <code>stderr</code> (aka standard error) rather than <code>printf</code>, which, it turns out, prints to something called <code>stdout</code> (aka standard output). By default, messages printed to <code>stdout</code> and <code>stderr</code> both appear on the user&#8217;s screens. But it&#8217;s possible to separate them when running a program so that users can distinguish error messages from non-error messages. But more on that perhaps another time!</p>
</div>
<div class="paragraph">
<p>Notice, too, how <code>main</code> returns <code>1</code> in cases of error. That, too, is a convention. To date, we&#8217;ve not returned any values from <code>main</code>. But, recall that, all this time, <code>main</code> <em>has</em> had a return type, specifically <code>int</code>. It turns out, when <code>main</code> is done executing, it returns <code>0</code> by default, which, by convention, signifies success. If something goes wrong in a program, though, it&#8217;s convention to return some value other than <code>0</code> (e.g., <code>1</code>). That value is called an "exit code" and can be used to distinguish one type of error from another. In fact, if you&#8217;ve ever seen a cryptic error code on your Mac&#8217;s or PC&#8217;s screen, it might very well have been the value returned by some (buggy) program&#8217;s <code>main</code> function.</p>
</div>
<div class="paragraph">
<p>Notice too how this program uses a function called <code>sprintf</code> which doesn&#8217;t actually print to the screen but instead stores its output in a string (hence the <code>s</code> in <code>sprintf</code>). We&#8217;re using it in order to create a string from two placeholders, <code>%s</code> and <code>%i</code>. Notice how we allocate space for a (short) string by declaring an array for 4 <code>char</code>s. We then use <code>sprintf</code> to store a <code>NOTES[i]</code> (a <code>string</code>, ergo the <code>%s</code>) in that memory followed by <code>octave</code> (an <code>int</code>, ergo the <code>%i</code>). That way, we can take values like <code>"A"</code> and <code>4</code> and, effectively, concatenate them (i.e., append the latter to the former) in order to create a new <code>string</code>, the value of which is, for instance, <code>A4</code>.</p>
</div>
<div class="paragraph">
<p>Along the way in this program do we call some (presumably) unfamilar functions called <code>song_open</code>, <code>frequency</code>, <code>note_write</code>, and <code>song_close</code>. It turns out those functions are implemented in other files in this problem&#8217;s distribution. Keep an eye out for them!</p>
</div>
</div>
<div class="sect3">
<h4 id="synthesize-c"><a class="link" href="#synthesize-c"><code>synthesize.c</code></a></h4>
<div class="paragraph">
<p>In this file is a program (soon to be called <code>synthesize</code>) that synthesizes (i.e., generates) a song from a sequence of notes. Notice how it gets those notes from a user one at a time using <code>get_string</code>. It first checks, though, whether the user&#8217;s input is a rest, as would happen if the user simply hits Enter. Else it proceeds to "tokenize" the user&#8217;s input into two tokens: a note, which can be found to the left of the <code>@</code> in the user&#8217;s input, and a fraction, which can be found to the right of the <code>@</code> in the user&#8217;s input. The program uses a function called <code>strtok</code> to facilitate such. It then writes that note (or rest) to a file.</p>
</div>
</div>
<div class="sect3">
<h4 id="wav-h"><a class="link" href="#wav-h"><code>wav.h</code></a></h4>
<div class="paragraph">
<p>Next open up <code>wav.h</code>, a header file used by both <code>notes.c</code> and <code>synthesize.c</code>. This file, together with <code>wav.c</code>, represents not a program but a "library," a set of functions that other programs can use as building blocks, much like <code>cs50</code> and <code>stdio</code> are libraries. This library&#8217;s code just so happens to live in your work workspace now.</p>
</div>
<div class="paragraph">
<p>In <code>wav.h</code> too are definitions of two new data types, one called <code>note</code> and one called <code>song</code>. But more on those (and keywords like <code>typedef</code> and <code>struct</code> another time). For now, just notice how this file declares four functions (<code>note_write</code>, <code>rest_write</code>, <code>song_close</code>, and <code>song_open</code>), which <code>notes</code> and <code>synthesize</code> use.</p>
</div>
</div>
<div class="sect3">
<h4 id="wav-c"><a class="link" href="#wav-c"><code>wav.c</code></a></h4>
<div class="paragraph">
<p>In <code>wav.c</code>, meanwhile, are the actual implementations of those functions plus a few others. Indeed, this file contains functions that implement support for WAV files, a popular (if dated) file format for audio. Those functions allow <code>notes</code> and <code>synthesize</code> to save notes to disk in files ending in <code>.wav</code>. To play those <code>.wav</code> files, simply open them via CS50 IDE&#8217;s file browser. Or download them to your Mac or PC to play them locally.</p>
</div>
<div class="paragraph">
<p>No need to understand all of the code in <code>wav.c</code>, but you&#8217;re welcome to read through it if you&#8217;d like!</p>
</div>
</div>
<div class="sect3">
<h4 id="makefile"><a class="link" href="#makefile"><code>Makefile</code></a></h4>
<div class="paragraph">
<p>Next open up <code>Makefile</code>, the format of which is perhaps quite different from anything you&#8217;ve seen before. As its name might suggest, it&#8217;s related to <code>make</code>, the program you&#8217;ve probably been using compile most of your programs, if only because compiling programs with <code>clang</code> itself tends to require more keystrokes. In previous problems, we&#8217;ve not needed a <code>Makefile</code>, which is essentially a configuration file for <code>make</code>, since <code>make</code> can infer how to compile a program that&#8217;s composed of a single file (e.g., <code>hello.c</code>). But compiling both <code>notes</code> and <code>synthesize</code> requires multiple files, since both programs rely on <code>wav.h</code> and <code>wav.c</code>, plus two other files, <code>helpers.h</code> and <code>helpers.c</code>.</p>
</div>
<div class="paragraph">
<p>Simply executing</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>make notes</code></pre>
</div>
</div>
<div class="paragraph">
<p>or</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>make synthesize</code></pre>
</div>
</div>
<div class="paragraph">
<p>wouldn&#8217;t provide nearly enough information for <code>make</code> to be able to infer which files it needs. So this <code>Makefile</code> exists so that <code>make</code> knows how to compile these programs.</p>
</div>
</div>
<div class="sect3">
<h4 id="helpers-h"><a class="link" href="#helpers-h"><code>helpers.h</code></a></h4>
<div class="paragraph">
<p>In this file, now, are declarations for three functions:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>duration</code>, which should take as input as a <code>string</code> a fraction (e.g., <code>1/4</code>) and return as an <code>int</code> a corresponding number of eigths (<code>2</code>, in this case, since <code>1/4</code> is equivalent to <code>2/8</code>);</p>
</li>
<li>
<p><code>frequency</code>, which should take as input as a <code>string</code> a note formatted as</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p><code>XY</code> (e.g., <code>A4</code>), where <code>X</code> is any of <code>A</code> through <code>G</code> and <code>Y</code> is any of <code>0</code> through <code>8</code>, or</p>
</li>
<li>
<p><code>XYZ</code> (e.g., <code>A#4</code>), where <code>X</code> is any of <code>A</code> through <code>G</code>, <code>Y</code> is <code>#</code> or <code>b</code>, and <code>Z</code> is any of <code>0</code> through <code>8</code>,</p>
</li>
</ul>
</div>
</div>
</div>
<div class="paragraph">
<p>and return as an <code>int</code> the note&#8217;s corresponding frequency, rounded to the nearest integer; and</p>
</div>
</li>
<li>
<p><code>is_rest</code>, which should return <code>true</code> if its input, a <code>string</code>, represents a rest in our machine-readable format, otherwise <code>false</code>.</p>
</li>
</ul>
</div>
</div>
<div class="sect3">
<h4 id="helpers-c"><a class="link" href="#helpers-c"><code>helpers.c</code></a></h4>
<div class="paragraph">
<p>And in this file there <em>should</em> be implementations of those three functions, but no! Not yet. That&#8217;s where you come in!</p>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="bday-txt"><a class="link" href="#bday-txt"><code>bday.txt</code></a></h3>
<div class="paragraph">
<p>In <code>bday.txt</code>, type the ASCII representation of <em>Happy Birthday</em>, translating its sheet music, above, to the machine-readable representation prescribed herein. You should find that the song begins with:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>D4@1/8
D4@1/8
E4@1/4
D4@1/4
G4@1/4
F#4@1/2</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="helpers-c-2"><a class="link" href="#helpers-c-2"><code>helpers.c</code></a></h3>
<div class="sect3">
<h4 id="is_rest"><a class="link" href="#is_rest"><code>is_rest</code></a></h4>
<div class="paragraph">
<p>Complete the implementation of <code>is_rest</code> in <code>helpers.c</code>. Recall that blank lines represent rests in our machine-readable format. And recall that <code>synthesize</code> will call this function in order to determine if one of the lines a user has typed in is indeed blank.</p>
</div>
<div class="paragraph">
<p>What does it mean for a line to be blank? To answer that question, start by looking at <code>cs50.h</code> itself, wherein <code>get_string</code> is documented:</p>
</div>
<div class="paragraph">
<p><a href="https://github.com/cs50/libcs50/blob/develop/src/cs50.h" class="bare">https://github.com/cs50/libcs50/blob/develop/src/cs50.h</a></p>
</div>
<div class="paragraph">
<p>What do the comments atop <code>get_string</code> say that the function returns if a user simply hits Enter, thereby inputting only a "line ending" (i.e., <code>\n</code>)?</p>
</div>
<div class="paragraph">
<p>When <code>is_rest</code> is subsequently passed such a <code>string</code>, <code>s</code>, how should it (nay, you!) recognize as much?</p>
</div>
</div>
<div class="sect3">
<h4 id="duration"><a class="link" href="#duration"><code>duration</code></a></h4>
<div class="paragraph">
<p>Complete the implementation of <code>duration</code> in <code>helpers.c</code>. Recall that this function should take as input as a <code>string</code> a fraction and convert it into some integral number of eighths. You may assume that <code>duration</code> will only be passed a <code>string</code> formatted as <code>X/Y</code>, whereby each of <code>X</code> and <code>Y</code> is a positive decimal digit, and <code>Y</code> is, moreover, a power of 2.</p>
</div>
</div>
<div class="sect3">
<h4 id="frequency"><a class="link" href="#frequency"><code>frequency</code></a></h4>
<div class="paragraph">
<p>Finally, complete the implementation of <code>frequency</code> in <code>helpers.c</code>. Recall that this function should take as input as a <code>string</code> a note (e.g., <code>A4</code>) and return its corresponding frequency in hertz as an <code>int</code>.</p>
</div>
<div class="paragraph">
<p>And recall that:</p>
</div>
<div class="olist arabic">
<ol class="arabic">
<li>
<p>The frequency, <em>f</em>, of some note is 2<sup><em>n</em>/12</sup> × 440, where <em>n</em> is the number of semitones from that note to <code>A4</code>.</p>
</li>
<li>
<p>Each key on a piano is said to be one semitone, otherwise known as a half step, away from its adjacent neighbor, whether white or black.</p>
</li>
<li>
<p>The effect of <code>#</code> and <code>b</code>, otherwise known as accidentals, is to raise or lower, respectively, the pitch of a note by one semitone.</p>
</li>
</ol>
</div>
<div class="paragraph">
<p>In implementing this function, you might find <code>pow</code> and <code>round</code>, both declared in <code>math.h</code>, of interest.</p>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>As always, when writing code, take baby steps, only implementing enough lines to make progress before testing (and, if need be, debugging) your code. Only once that first step is succesful (i.e., debugged!) should you take another. Plan each of your steps by writing pseudocode before code.</p>
</div>
<div class="paragraph">
<p>In the context of <code>frequency</code> specifically, taking baby steps might mean:</p>
</div>
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Only implement support initially for <code>A0</code> through <code>A8</code>, no other notes. Ensure that <code>frequency</code> returns the expected values for those notes, as by running <code>notes</code> or using <code>debug50</code> or <code>eprintf</code>. Compare your function&#8217;s output against your own calculations on paper or on a calculator.</p>
</li>
<li>
<p>Then add support for <code>#</code> and <code>b</code> but still only for <code>A0</code> through <code>A8</code> (i.e., <code>A#0</code> through <code>A#8</code> and <code>Ab0</code> through <code>Ab8</code>).</p>
</li>
<li>
<p>Then add support for <code>B</code>. Then for <code>C</code>. Then beyond.</p>
</li>
</ol>
</div>
</div>
</div>
</div>
</body>
</html>

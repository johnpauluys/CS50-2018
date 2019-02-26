<html>
<body>
<div id="content">
                <h1>Mashup</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a website that lets users search for articles atop a map.</p>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>A "mashup" is a web app that combines data or functionality from multiple sources. In this here mashup, you&#8217;ll combine data from Google News with functionality from Google Maps!</p>
</div>
<div class="sect2">
<h3 id="google-maps"><a class="link" href="#google-maps">Google Maps</a></h3>
<div class="paragraph">
<p>Odds are you&#8217;re already familiar, but head to Google Maps anyway at <a href="https://www.google.com/maps" class="bare">https://www.google.com/maps</a>. Input <strong>42.374490, -71.117185</strong> into the search box up top, and you should find yourself at Harvard. Input <strong>41.3163284, -72.9245318</strong>, and you should find yourself at Yale.</p>
</div>
<div class="paragraph">
<p>Interesting! It seems Google Maps understands GPS coordinates (i.e., latitude and longitude). In fact, search for <strong>28.410, -81.584</strong>. Perhaps you&#8217;d rather be there? (You might need to zoom out.)</p>
</div>
<div class="paragraph">
<p>It turns out that Google Maps offers an API that allows you to embed Google&#8217;s maps into your own web apps. Hey, that&#8217;s one of the ingredients we need! Go ahead and familiarize yourself with <a href="https://developers.google.com/maps/documentation/javascript/">Google Maps Javascript API</a> by perusing the three sections below of its Developer&#8217;s Guide. Read through any sample code carefully, clicking <strong>View example</strong> below it, if present, to see the code in action.</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="https://developers.google.com/maps/documentation/javascript/tutorial">Getting Started</a></p>
</li>
<li>
<p>Drawing on the Map</p>
<div class="ulist">
<ul>
<li>
<p><a href="https://developers.google.com/maps/documentation/javascript/markers">Markers</a></p>
</li>
<li>
<p><a href="https://developers.google.com/maps/documentation/javascript/infowindows">Info Windows</a></p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</div>
<div class="sect2">
<h3 id="google-news"><a class="link" href="#google-news">Google News</a></h3>
<div class="paragraph">
<p>Okay, now we need us some news. Fortunately, Google News offers just that! In fact, if you visit the URLs below, you should see stories pertaining to Cambridge, Massachusetts and New Haven, Connecticut, respectively:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="https://news.google.com/news/local/section/geo/Cambridge,%20Massachusetts" class="bare">https://news.google.com/news/local/section/geo/Cambridge,%20Massachusetts</a></p>
</li>
<li>
<p><a href="https://news.google.com/news/local/section/geo/New%20Haven,%20Connecticut" class="bare">https://news.google.com/news/local/section/geo/New%20Haven,%20Connecticut</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Notice how the spaces in those towns' names have been "URL-encoded" (i.e., escaped) as <code>%20</code>. Notice, too, that you can query for news by postal code:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="https://news.google.com/news/local/section/geo/02138" class="bare">https://news.google.com/news/local/section/geo/02138</a></p>
</li>
<li>
<p><a href="https://news.google.com/news/local/section/geo/06511" class="bare">https://news.google.com/news/local/section/geo/06511</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>The pages you&#8217;re seeing are, of course, written in HTML. But all we want, if the staff&#8217;s solution is any indication, is a bulleted list of articles' titles and links. How to get those without "scraping" this page&#8217;s (surely complicated) HTML? Scroll down to the page&#8217;s bottom and look for <strong>RSS</strong>. Click that link, and you should find yourself at URLs like the below, perhaps with some HTTP parameters after a question mark?</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="https://news.google.com/news/rss/local/section/geo/02138" class="bare">https://news.google.com/news/rss/local/section/geo/02138</a></p>
</li>
<li>
<p><a href="https://news.google.com/news/rss/local/section/geo/06511" class="bare">https://news.google.com/news/rss/local/section/geo/06511</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Now, what&#8217;s all this markup that&#8217;s now on your screen? It looks a bit like HTML, but you&#8217;re actually looking at an "RSS feed," a flavor of XML (a tag-based markup language). For quite some time, RSS was all the rage insofar as it enabled websites to "syndicate" articles in a standard format that "RSS readers" could read. RSS isn&#8217;t quite as hip anymore these days, but it&#8217;s still a terrific find for us because it&#8217;s "machine-readable". Because it adheres to a standard format, we can parse it (pretty easily!) with software. Here&#8217;s what an RSS feed generally looks like (sans actual data):</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="xml"><span></span><span class="tok-nt">&lt;rss</span> <span class="tok-na">version=</span><span class="tok-s">&quot;2.0&quot;</span><span class="tok-nt">&gt;</span>
    <span class="tok-nt">&lt;channel&gt;</span>
        <span class="tok-nt">&lt;title&gt;</span>...<span class="tok-nt">&lt;/title&gt;</span>
        <span class="tok-nt">&lt;description&gt;</span>...<span class="tok-nt">&lt;/description&gt;</span>
        <span class="tok-nt">&lt;link&gt;</span>...<span class="tok-nt">&lt;/link&gt;</span>
        <span class="tok-nt">&lt;item&gt;</span>
            <span class="tok-nt">&lt;guid&gt;</span>...<span class="tok-nt">&lt;/guid&gt;</span>
            <span class="tok-nt">&lt;title&gt;</span>...<span class="tok-nt">&lt;/title&gt;</span>
            <span class="tok-nt">&lt;link&gt;</span>...<span class="tok-nt">&lt;/link&gt;</span>
            <span class="tok-nt">&lt;description&gt;</span>...<span class="tok-nt">&lt;/description&gt;</span>
            <span class="tok-nt">&lt;category&gt;</span>...<span class="tok-nt">&lt;/category&gt;</span>
            <span class="tok-nt">&lt;pubDate&gt;</span>...<span class="tok-nt">&lt;/pubDate&gt;</span>
        <span class="tok-nt">&lt;/item&gt;</span>
        ...
    <span class="tok-nt">&lt;/channel&gt;</span>
<span class="tok-nt">&lt;/rss&gt;</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>In other words, an RSS feed contains a root element called <code>rss</code>, the child of which is an element called <code>channel</code>.  Inside of <code>channel</code> are elements called <code>title</code>, <code>description</code>, and <code>link</code>, followed by one or more elements called <code>item</code>, each of which represents an article (or blog post or the like). Each <code>item</code>, meanwhile, contains elements called <code>guid</code>, <code>title</code>, <code>link</code>, <code>description</code>, <code>category</code>, and <code>pubDate</code>. Of course, between most of these start tags and end tags should be actual data (e.g., an article&#8217;s actual title). For more details, see <a href="https://cyber.law.harvard.edu/rss/rss.html" class="bare">https://cyber.law.harvard.edu/rss/rss.html</a>.</p>
</div>
<div class="paragraph">
<p>Ultimately, we&#8217;ll parse RSS feeds from Google News using Python and then return articles' titles and links to our web app via Ajax as JSON. But more on that in a bit.</p>
</div>
</div>
<div class="sect2">
<h3 id="jquery"><a class="link" href="#jquery">jQuery</a></h3>
<div class="paragraph">
<p>Recall that <a href="http://jquery.com/">jQuery</a> is a popular JavaScript library that "makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers." To be fair, though, it&#8217;s not without a learning curve. Read through a few sections of jQuery&#8217;s documentation if you&#8217;d like.</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="http://learn.jquery.com/using-jquery-core/document-ready/">$( document ).ready()</a></p>
</li>
<li>
<p><a href="http://learn.jquery.com/using-jquery-core/selecting-elements/">Selecting Elements</a></p>
</li>
<li>
<p><a href="http://learn.jquery.com/ajax/jquery-ajax-methods/">jQuery&#8217;s Ajax-Related Methods</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>jQuery&#8217;s documentation isn&#8217;t the most user-friendly, though, so odds are you&#8217;ll ultimately find <a href="https://www.google.com/">Google</a> and <a href="http://stackoverflow.com/">Stack Overflow</a> handier resources.</p>
</div>
<div class="paragraph">
<p>Recall that <code>$</code> is usually (though not always) an alias for a global object that&#8217;s otherwise called <code>jQuery</code>.</p>
</div>
</div>
<div class="sect2">
<h3 id="typeahead-js"><a class="link" href="#typeahead-js">typeahead.js</a></h3>
<div class="paragraph">
<p>Now take a look at some examples of Twitter&#8217;s typeahead.js library, a jQuery "plugin" that adds support for autocompletion to HTML text fields. Play with <strong>The Basics</strong>, <strong>Custom Templates</strong>, and <strong>Scrollable Dropdown Menu</strong> in particular.</p>
</div>
<div class="paragraph">
<p><a href="http://twitter.github.io/typeahead.js/examples/" class="bare">http://twitter.github.io/typeahead.js/examples/</a></p>
</div>
<div class="paragraph">
<p>And now skim the documentation for a "fork" (i.e., someone else&#8217;s version) of that same library:</p>
</div>
<div class="paragraph">
<p><a href="https://github.com/corejavascript/typeahead.js/blob/master/doc/jquery_typeahead.md" class="bare">https://github.com/corejavascript/typeahead.js/blob/master/doc/jquery_typeahead.md</a></p>
</div>
<div class="paragraph">
<p>Note that Twitter hasn&#8217;t updated their own version of the library for quite some time, so take care to rely on <a href="https://github.com/corejavascript/typeahead.js">github.com/corejavascript/typeahead.js</a>, not <a href="https://github.com/twitter/typeahead.js">github.com/twitter/typeahead.js</a>.</p>
</div>
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
<pre class="pygments highlight"><code>$ wget <a href="http://cdn.cs50.net/2018/x/psets/8/mashup/mashup.zip" class="bare">http://cdn.cs50.net/2018/x/psets/8/mashup/mashup.zip</a>
$ unzip mashup.zip
$ rm mashup.zip
$ cd mashup
$ ls
application.py  mashup.db         static/
helpers.py      requirements.txt  templates/
$ wget <a href="http://cdn.cs50.net/2017/fall/psets/8/mashup/US.zip" class="bare">http://cdn.cs50.net/2017/fall/psets/8/mashup/US.zip</a>
$ unzip US.zip
$ rm US.zip
$ ls
application.py  mashup.db   requirements.txt  templates/
helpers.py      readme.txt  static/           US.txt</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="running"><a class="link" href="#running">Running</a></h3>
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Start Flask&#8217;s built-in web server (within <code>mashup/</code>):</p>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>flask run</code></pre>
</div>
</div>
<div class="paragraph">
<p>Visit the URL outputted by <code>flask</code> to see the distribution code in action. You won&#8217;t be able to search for news, though, just yet!</p>
</div>
</li>
<li>
<p>Via CS50&#8217;s file browser, double-click <strong>mashup.db</strong> in order to open it with phpLiteAdmin. Notice that it doesn&#8217;t have any tables yet! (That&#8217;s where you come in.) Here on out, though, if you&#8217;d prefer a command line, you&#8217;re welcome to use <code>sqlite3</code> instead of phpLiteAdmin.</p>
</li>
</ol>
</div>
</div>
<div class="sect2">
<h3 id="understanding"><a class="link" href="#understanding">Understanding</a></h3>
<div class="sect3">
<h4 id="index-html"><a class="link" href="#index-html">index.html</a></h4>
<div class="paragraph">
<p>Open up <code>templates/index.html</code>, which will be your app&#8217;s one and only HTML page. If you look at the page&#8217;s <code>head</code>, you&#8217;ll see all those CSS and JavaScript libraries we&#8217;ll be using (plus some others). Included in HTML comments are URLs for each library&#8217;s documentation if curious.</p>
</div>
<div class="paragraph">
<p>Next take a look at the page&#8217;s <code>body</code>, inside of which is <code>div</code> with a unique <code>id</code> of <code>map-canvas</code>. It&#8217;s into that <code>div</code> that we&#8217;ll be injecting a map. Below that <code>div</code>, meanwhile, is a <code>form</code>, inside of which is an <code>input</code> of type <code>text</code> with a unique <code>id</code> of <code>q</code> that we&#8217;ll use to take input from users.</p>
</div>
</div>
<div class="sect3">
<h4 id="styles-css"><a class="link" href="#styles-css">styles.css</a></h4>
<div class="paragraph">
<p>Next open up <code>static/styles.css</code>. In there is a bunch of CSS that implements the mashup&#8217;s default UI. Feel free to tinker (i.e., make changes, save the file, and reload the page in Chrome) to see how everything works, but best to undo any such changes for now before forging ahead.</p>
</div>
</div>
<div class="sect3">
<h4 id="scripts-js"><a class="link" href="#scripts-js">scripts.js</a></h4>
<div class="paragraph">
<p>Next open up <code>static/scripts.js</code>. Ah, the most interesting file yet! It&#8217;s this file that implements the mashup&#8217;s "front-end" UI, relying on Google Maps and some "back-end" Flask routes for data (that we&#8217;ll soon explore). Let&#8217;s walk through this one.</p>
</div>
<div class="paragraph">
<p>Atop the file are some global variables:</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>map</code>, which will contain a reference (i.e., a pointer of sorts) to the map we&#8217;ll soon be instantiating;</p>
</li>
<li>
<p><code>markers</code>, an array that will contain references to any markers we add atop the map; and</p>
</li>
<li>
<p><code>info</code>, a reference to an "info window" in which we&#8217;ll ultimately display links to articles.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Below those global variables is an anonymous function that will be called automatically by jQuery when the mashup&#8217;s DOM is fully loaded (i.e., when <code>index.html</code> and all its assets, CSS and JavaScript especially, have been loaded into memory).</p>
</div>
<div class="paragraph">
<p>Atop this anonymous function is a definition of <code>styles</code>, an array of two objects that we&#8217;ll use to configure our map, as per <a href="https://developers.google.com/maps/documentation/javascript/styling" class="bare">https://developers.google.com/maps/documentation/javascript/styling</a>. Recall that <code>[</code> and <code>]</code> denote an array, while <code>{</code> and <code>}</code> denote an object. The (very pretty) indentation you see is just a stylistic convention to which it&#8217;s probably ideal to adhere in your code as well.</p>
</div>
<div class="paragraph">
<p>Below <code>styles</code> is <code>options</code>, another collection of keys and values that will ultimately be used to configure the map further, as per <a href="https://developers.google.com/maps/documentation/javascript/3.exp/reference#MapOptions" class="bare">https://developers.google.com/maps/documentation/javascript/3.exp/reference#MapOptions</a>.</p>
</div>
<div class="paragraph">
<p>Next we define <code>canvas</code>, by using a bit of jQuery to get the DOM node whose unique <code>id</code> is <code>map-canvas</code>. Whereas <code>$("#map-canvas")</code> returns a jQuery object (that has a whole bunch of functionality built-in), <code>$("#map-canvas").get(0)</code> returns the actual, underlying DOM node that jQuery is just wrapping.</p>
</div>
<div class="paragraph">
<p>Perhaps the most powerful line yet is the next one in which we assign <code>map</code> (that global variable) a value. With</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-k">new</span> <span class="tok-nx">google</span><span class="tok-p">.</span><span class="tok-nx">maps</span><span class="tok-p">.</span><span class="tok-nx">Map</span><span class="tok-p">(</span><span class="tok-nx">canvas</span><span class="tok-p">,</span> <span class="tok-nx">options</span><span class="tok-p">);</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>we&#8217;re telling the browser to instantiate a new map, injecting it into the DOM node specified by <code>canvas</code>), configured per <code>options</code>.</p>
</div>
<div class="paragraph">
<p>The line below that one, meanwhile, tells the browser to call <code>configure</code> (another function we&#8217;ve written) as soon as the map is loaded.</p>
</div>
<div class="sect4">
<h5 id="addmarker"><a class="link" href="#addmarker">addMarker</a></h5>
<div class="paragraph">
<p>Ah, a <code>TODO</code>. Ultimately, given a <code>place</code> (i.e., postal code and more), this function will need to add a marker (i.e., icon) to the map.</p>
</div>
</div>
<div class="sect4">
<h5 id="configure"><a class="link" href="#configure">configure</a></h5>
<div class="paragraph">
<p>This function, meanwhile, picks up where that anonymous function left off. Recall that <code>configure</code> is called as soon as the map has been loaded. Within this function we configure a number of "listeners," specifying what should happen when we "hear" certain events. For instance,</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-nx">google</span><span class="tok-p">.</span><span class="tok-nx">maps</span><span class="tok-p">.</span><span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">addListener</span><span class="tok-p">(</span><span class="tok-nx">map</span><span class="tok-p">,</span> <span class="tok-s2">&quot;dragend&quot;</span><span class="tok-p">,</span> <span class="tok-kd">function</span><span class="tok-p">()</span> <span class="tok-p">{</span>
    <span class="tok-nx">update</span><span class="tok-p">();</span>
<span class="tok-p">});</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>indicates that we want to listen for a <code>dragend</code> event on the map, calling the anonymous function provided when we hear it. That anonymous function, meanwhile, simply calls <code>update</code> (another function we&#8217;ll soon see). Per <a href="https://developers.google.com/maps/documentation/javascript/3.exp/reference#Map" class="bare">https://developers.google.com/maps/documentation/javascript/3.exp/reference#Map</a>, <code>dragend</code> is "fired" (i.e., broadcasted) "when the user stops dragging the map."</p>
</div>
<div class="paragraph">
<p>Similarly do we listen for <code>zoom_changed</code>, which is fired "when the map zoom property changes" (i.e., the user zooms in or out).</p>
</div>
<div class="paragraph">
<p>Below those listeners is our configuration of that typeahead plugin. Take another look at <a href="https://github.com/corejavascript/typeahead.js/blob/master/doc/jquery_typeahead.md" class="bare">https://github.com/corejavascript/typeahead.js/blob/master/doc/jquery_typeahead.md</a> if unsure what <code>highlight</code> and <code>minLength</code> do here. Most importantly, though, know that the value of <code>source</code> (i.e., <code>search</code>) is the function that the plugin will call as soon as the user starts typing so that the function can respond with an array of search results based on the user&#8217;s input. For instance, if the user types <code>foo</code> into that text box, the function should ultimately return an array of all places in your database that somehow match <code>foo</code>. How to perform those matches will ultimately be left to you! The value of <code>templates</code>, meanwhile, is an object with one key, <code>suggestion</code>, whose value is a "template" that will be used to format each entry in the plugin&#8217;s dropdown menu. That template is created by a call to <code>Handlebars.compile</code>, a method that comes with <a href="http://handlebarsjs.com/">Handlebars</a>, a templating language for JavaScript similar in spirit to Jinja for Python. Right now, that template is simply <code>&lt;div&gt;TODO&lt;/div&gt;</code>, which means that every entry in that dropdown will literally say <code>TODO</code>. Ultimately, you&#8217;ll want to change that value to something like</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-o">&lt;</span><span class="tok-nx">div</span><span class="tok-o">&gt;</span><span class="tok-p">{{</span><span class="tok-nx">place_name</span><span class="tok-p">}},</span> <span class="tok-p">{{</span><span class="tok-nx">admin_name1</span><span class="tok-p">}},</span> <span class="tok-p">{{</span><span class="tok-nx">postal_code</span><span class="tok-p">}}</span><span class="tok-o">&lt;</span><span class="tok-err">/div&gt;</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>so that the plugin dynamically inserts those values (<code>place_name</code>, <code>admin_name1</code>, and <code>postal_code</code>) or some others for you.</p>
</div>
<div class="paragraph">
<p>Next notice these lines, which are admittedly a bit cryptic at first glance:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-nx">$</span><span class="tok-p">(</span><span class="tok-s2">&quot;#q&quot;</span><span class="tok-p">).</span><span class="tok-nx">on</span><span class="tok-p">(</span><span class="tok-s2">&quot;typeahead:selected&quot;</span><span class="tok-p">,</span> <span class="tok-kd">function</span><span class="tok-p">(</span><span class="tok-nx">eventObject</span><span class="tok-p">,</span> <span class="tok-nx">suggestion</span><span class="tok-p">,</span> <span class="tok-nx">name</span><span class="tok-p">)</span> <span class="tok-p">{</span>
    <span class="tok-p">...</span>
    <span class="tok-nx">map</span><span class="tok-p">.</span><span class="tok-nx">setCenter</span><span class="tok-p">({</span><span class="tok-nx">lat</span><span class="tok-o">:</span> <span class="tok-nb">parseFloat</span><span class="tok-p">(</span><span class="tok-nx">suggestion</span><span class="tok-p">.</span><span class="tok-nx">latitude</span><span class="tok-p">),</span> <span class="tok-nx">lng</span><span class="tok-o">:</span> <span class="tok-nb">parseFloat</span><span class="tok-p">(</span><span class="tok-nx">suggestion</span><span class="tok-p">.</span><span class="tok-nx">longitude</span><span class="tok-p">)});</span>
    <span class="tok-p">...</span>
    <span class="tok-nx">update</span><span class="tok-p">();</span>
<span class="tok-p">});</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>These lines are saying that if the HTML element whose unique <code>id</code> is <code>q</code> fires an event called <code>typeahead:selected</code>, as will happen when the user selects an entry from the plugin&#8217;s dropdown menu, we want jQuery to call an anonymous function whose second argument, <code>suggestion</code>, will be an object that represents the entry selected. Within that object must be at least two properties: <code>latitude</code> and <code>longitude</code>. We&#8217;ll then call <code>setCenter</code> in order to re-center the map at those coordinates, after which we&#8217;ll call <code>update</code> to update any markers.</p>
</div>
<div class="paragraph">
<p>Below those lines, meanwhile, are these:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-nx">$</span><span class="tok-p">(</span><span class="tok-s2">&quot;#q&quot;</span><span class="tok-p">).</span><span class="tok-nx">focus</span><span class="tok-p">(</span><span class="tok-kd">function</span><span class="tok-p">(</span><span class="tok-nx">eventData</span><span class="tok-p">)</span> <span class="tok-p">{</span>
    <span class="tok-nx">info</span><span class="tok-p">.</span><span class="tok-nx">close</span><span class="tok-p">();</span>
<span class="tok-p">});</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>If you consult <a href="http://api.jquery.com/focus/" class="bare">http://api.jquery.com/focus/</a>, hopefully those lines will make sense?</p>
</div>
<div class="paragraph">
<p>Below those are these:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="js"><span></span><span class="tok-nb">document</span><span class="tok-p">.</span><span class="tok-nx">addEventListener</span><span class="tok-p">(</span><span class="tok-s2">&quot;contextmenu&quot;</span><span class="tok-p">,</span> <span class="tok-kd">function</span><span class="tok-p">(</span><span class="tok-nx">event</span><span class="tok-p">)</span> <span class="tok-p">{</span>
    <span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">returnValue</span> <span class="tok-o">=</span> <span class="tok-kc">true</span><span class="tok-p">;</span>
    <span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">stopPropagation</span> <span class="tok-o">&amp;&amp;</span> <span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">stopPropagation</span><span class="tok-p">();</span>
    <span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">cancelBubble</span> <span class="tok-o">&amp;&amp;</span> <span class="tok-nx">event</span><span class="tok-p">.</span><span class="tok-nx">cancelBubble</span><span class="tok-p">();</span>
<span class="tok-p">},</span> <span class="tok-kc">true</span><span class="tok-p">);</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Unfortunately, Google Maps disables ctrl- and right-clicks on maps, which interferes with using Chrome&#8217;s (amazingly useful) <strong>Inspect Element</strong> feature, so these lines re-enable those.</p>
</div>
<div class="paragraph">
<p>Last up in <code>configure</code> is a call to <code>update</code> (which we&#8217;ll soon look at) and a call to <code>focus</code>, this time with no arguments. See <a href="http://api.jquery.com/focus/" class="bare">http://api.jquery.com/focus/</a> for why!</p>
</div>
</div>
<div class="sect4">
<h5 id="removemarkers"><a class="link" href="#removemarkers">removeMarkers</a></h5>
<div class="paragraph">
<p>Hm, a <code>TODO</code>. Ultimately, this function will need to remove any and all markers from the map!</p>
</div>
</div>
<div class="sect4">
<h5 id="search"><a class="link" href="#search">search</a></h5>
<div class="paragraph">
<p>This function is called by the typeahead plugin every time the user changes the mashup&#8217;s text box, as by typing or deleting a character. The value of the text box (i.e., whatever the user has typed in total) is passed to <code>search</code> as <code>query</code>. And the plugin also passes to <code>search</code> two additional arguments, the last of which (<code>asyncResults</code>) is a "callback" function that <code>search</code> should call as soon as it&#8217;s done searching for matches. In other words, this passing in of <code>asyncResults</code> empowers <code>search</code> to be "asynchronous," whereby it will only call <code>asyncResults</code> as soon as it&#8217;s ready, without blocking any of the mashup&#8217;s other functionality. Accordingly, <code>search</code> uses jQuery&#8217;s <code>getJSON</code> method to contact <code>/search</code> asynchronously, passing in one parameter, <code>q</code>, the value of which is <code>query</code>. Once <code>/search</code> responds (however many milliseconds or seconds later), <code>asyncResults</code> will be called and passed <code>data</code>, whose value will be whatever JSON that <code>/search</code> has emitted. The plugin can then iterate over the places therein (assuming <code>/search</code> found matches) in order to update the plugin&#8217;s drop-down. Phew.</p>
</div>
</div>
<div class="sect4">
<h5 id="showinfo"><a class="link" href="#showinfo">showInfo</a></h5>
<div class="paragraph">
<p>This function opens the info window at a particular marker with particular content (i.e., HTML). Though if only one argument is supplied (<code>marker</code>), <code>showInfo</code> simply displays a spinning icon (which is just an animated GIF). Notice, though, how this function is creating a string of HTML dynamically, thereafter passing it to <code>setContent</code>. Perhaps keep that technique in mind elsewhere!</p>
</div>
</div>
<div class="sect4">
<h5 id="update"><a class="link" href="#update">update</a></h5>
<div class="paragraph">
<p>Last up is <code>update</code>, which first determines the map&#8217;s current bounds, the coordinates of its top-right (northeast) and bottom-left (southwest) corners. It then passes those coordinates to <code>/update</code> via a GET request (underneath the hood of <code>getJSON</code>) a la:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>GET /update?ne=37.45215513235332%2C-122.03830380859375&amp;q=&amp;sw=37.39503397352173%2C-122.28549619140625 HTTP/1.1</code></pre>
</div>
</div>
<div class="paragraph">
<p>The <code>%2C</code> are just commas that have been "URL-encoded." Realize that our use of commas is arbitary; we&#8217;re expecting <code>/update</code> to parse and extract latitudes and longitudes from these parameters. We could have simply passed in four distinct parameters, but we felt it was semantically cleaner to pass in just one parameter per corner.</p>
</div>
<div class="paragraph">
<p>As we&#8217;ll soon see, <code>/update</code> is designed to return a JSON array of places that fall within the map&#8217;s current bounds (i.e., cities within view). After all, with those two corners alone can you define a rectangle, which is exactly what the map is!</p>
</div>
<div class="paragraph">
<p>As soon as <code>/update</code> responds, the anonymous function passed to <code>done</code> is called and passed <code>data</code>, the value of which is the JSON emitted by <code>/update</code>. (Though if something goes wrong, <code>fail</code> is instead called.) That anonymous function first removes all markers from the map and then iteratively adds new markers, one for each place (i.e., city) in the JSON.</p>
</div>
<div class="paragraph">
<p>Phew and phew!</p>
</div>
</div>
</div>
<div class="sect3">
<h4 id="application-py"><a class="link" href="#application-py">application.py</a></h4>
<div class="paragraph">
<p>Now open up <code>application.py</code>, which contains four routes!</p>
</div>
<div class="sect4">
<h5 id="index"><a class="link" href="#index"><code>index</code></a></h5>
<div class="paragraph">
<p>All this route does is render <code>index.html</code>, the app&#8217;s sole template.</p>
</div>
</div>
<div class="sect4">
<h5 id="articles"><a class="link" href="#articles"><code>articles</code></a></h5>
<div class="paragraph">
<p>Not much in here yet, just a <code>TODO</code>!</p>
</div>
</div>
<div class="sect4">
<h5 id="search-2"><a class="link" href="#search-2"><code>search</code></a></h5>
<div class="paragraph">
<p>Not much in this route yet either, just another <code>TODO</code>!</p>
</div>
</div>
<div class="sect4">
<h5 id="update-2"><a class="link" href="#update-2"><code>update</code></a></h5>
<div class="paragraph">
<p>Ah, okay, here&#8217;s the "back end" that outputs a JSON array of up to 10 places (i.e., cities) that fall within the specified bounds (i.e., within the rectangle defined by those corners). You won&#8217;t need to make changes to this route, but do read through it line by line, Googling any function with which you&#8217;re not familiar.</p>
</div>
<div class="paragraph">
<p>And yes, this file&#8217;s SQL queries assume that the world is flat for simplicity.</p>
</div>
</div>
</div>
<div class="sect3">
<h4 id="helpers-py"><a class="link" href="#helpers-py"><code>helpers.py</code></a></h4>
<div class="paragraph">
<p>Finally, take a look at <code>helpers.py</code>. In this file we&#8217;ve defined just one function, <code>lookup</code>, which queries Google News for articles for a particular geography, falling back on The Onion if none are available.</p>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="mashup-db"><a class="link" href="#mashup-db"><code>mashup.db</code></a></h3>
<div class="paragraph">
<p>Per <code>readme.txt</code>, <code>US.txt</code> is quite like a CSV file except that its fields are delimited with <code>\t</code> (a tab character) instead of a comma. Conveniently, SQLite allows you to <a href="https://www.sqlite.org/cli.html#csv_import">import CSV files</a> and, as it turns out, TSV (tab-separated values) files as well. But you first need a table into which to import such a file.</p>
</div>
<div class="paragraph">
<p>Using phpLiteAdmin or <code>sqlite3</code>, create a table in <code>mashup.db</code> called <code>places</code> that has these twelve fields, in this order:</p>
</div>
<div class="olist arabic">
<ol class="arabic">
<li>
<p><code>country_code</code></p>
</li>
<li>
<p><code>postal_code</code></p>
</li>
<li>
<p><code>place_name</code></p>
</li>
<li>
<p><code>admin_name1</code></p>
</li>
<li>
<p><code>admin_code1</code></p>
</li>
<li>
<p><code>admin_name2</code></p>
</li>
<li>
<p><code>admin_code2</code></p>
</li>
<li>
<p><code>admin_name3</code></p>
</li>
<li>
<p><code>admin_code3</code></p>
</li>
<li>
<p><code>latitude</code></p>
</li>
<li>
<p><code>longitude</code></p>
</li>
<li>
<p><code>accuracy</code></p>
</li>
</ol>
</div>
<div class="paragraph">
<p>See <code>readme.txt</code> (or <code>US.txt</code> itself) for clues as to appropriate types for these fields. Don&#8217;t include an <code>id</code> field (else you can&#8217;t do what we&#8217;re about to do!).</p>
</div>
<div class="paragraph">
<p>Rather than <code>INSERT</code> the rows from <code>US.txt</code> into your newly created table, let&#8217;s now import them in bulk as follows:</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>$ sqlite3 mashup.db
.separator "\t"
.import US.txt places</code></pre>
</div>
</div>
<div class="paragraph">
<p>If you see any errors, odds are your schema for <code>places</code> isn&#8217;t quite right, in which case you&#8217;ll want to <code>ALTER</code> (or <code>DROP</code> and re-<code>CREATE</code>) it accordingly. To confirm that an import&#8217;s successful, execute</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>wc -l US.txt</code></pre>
</div>
</div>
<div class="paragraph">
<p>to count how many rows are in <code>US.txt</code>. (That command-line argument is a hyphen followed by a lowercase L.) Then execute a query like</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>SELECT COUNT(*) FROM places;</code></pre>
</div>
</div>
<div class="paragraph">
<p>in <code>sqlite3</code> or phpLiteAdmin. The counts should match!</p>
</div>
</div>
<div class="sect2">
<h3 id="application-py-2"><a class="link" href="#application-py-2"><code>application.py</code></a></h3>
<div class="sect3">
<h4 id="articles-2"><a class="link" href="#articles-2"><code>articles</code></a></h4>
<div class="paragraph">
<p>Complete the implementation of <code>/articles</code> in such a way that it outputs a JSON array of objects, each of which represents an article for <code>geo</code>, whereby <code>geo</code> is passed into <code>/articles</code> as a GET parameter, as in the staff solution, below.</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="http://mashup.cs50.net/articles?geo=02138" class="bare">http://mashup.cs50.net/articles?geo=02138</a></p>
</li>
<li>
<p><a href="http://mashup.cs50.net/articles?geo=06511" class="bare">http://mashup.cs50.net/articles?geo=06511</a></p>
</li>
<li>
<p><a href="http://mashup.cs50.net/articles?geo=90210" class="bare">http://mashup.cs50.net/articles?geo=90210</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Odds are you&#8217;ll want to call <code>lookup</code>! To test <code>/articles</code>, even before your text box is operational, simply visit URLs like</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>https://ide50-username.cs50.io/articles?geo=02138</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/articles?geo=06511</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/articles?geo=90210</code></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>and other such variants, where <code>username</code> is your own username, to see if you get back the JSON you expect.</p>
</div>
</div>
<div class="sect3">
<h4 id="search-3"><a class="link" href="#search-3"><code>search</code></a></h4>
<div class="paragraph">
<p>Complete the implementation of <code>/search</code> in such a way that it outputs a JSON array of objects, each of which represents a row from <code>places</code> that somehow matches the value of <code>q</code>, as in the staff solution below.</p>
</div>
<div class="ulist">
<ul>
<li>
<p><a href="http://mashup.cs50.net/search?q=02138" class="bare">http://mashup.cs50.net/search?q=02138</a></p>
</li>
<li>
<p><a href="http://mashup.cs50.net/search?q=Cambridge" class="bare">http://mashup.cs50.net/search?q=Cambridge</a></p>
</li>
<li>
<p><a href="http://mashup.cs50.net/search?q=06511" class="bare">http://mashup.cs50.net/search?q=06511</a></p>
</li>
<li>
<p><a href="http://mashup.cs50.net/search?q=New%20Haven" class="bare">http://mashup.cs50.net/search?q=New%20Haven</a></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>The value of <code>q</code>, passed into <code>/search</code> as a GET parameter, might be a city, state, and/or postal code. We leave it to you to decide what constitutes a match and, therefore, which rows to <code>SELECT</code>. It suffices to support searching by postal codes only, but try to support searching by city and/or state as well. Odds are you&#8217;ll find SQL&#8217;s <code>LIKE</code> keyword helpful. If feeling adventurous, you might like (but are not required) to experiment with SQLite&#8217;s support for <a href="https://www.sqlite.org/fts3.html">full-text searches</a>.</p>
</div>
<div class="paragraph">
<p>For instance, consider the query below.</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="sql"><span></span><span class="tok-n">db</span><span class="tok-p">.</span><span class="tok-k">execute</span><span class="tok-p">(</span><span class="tok-ss">&quot;SELECT * FROM places WHERE postal_code = :q&quot;</span><span class="tok-p">,</span> <span class="tok-n">q</span><span class="tok-o">=</span><span class="tok-n">request</span><span class="tok-p">.</span><span class="tok-n">args</span><span class="tok-p">.</span><span class="tok-k">get</span><span class="tok-p">(</span><span class="tok-ss">&quot;q&quot;</span><span class="tok-p">))</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Unfortunately, that query requires that a user&#8217;s input be exactly equal to a postal code (per the <code>=</code>), which isn&#8217;t all that compelling for autocomplete. How about this one instead? (Recall that <code>+</code> is Python&#8217;s concatenation operator.)</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="sql"><span></span><span class="tok-n">q</span> <span class="tok-o">=</span> <span class="tok-n">request</span><span class="tok-p">.</span><span class="tok-n">args</span><span class="tok-p">.</span><span class="tok-k">get</span><span class="tok-p">(</span><span class="tok-ss">&quot;q&quot;</span><span class="tok-p">)</span> <span class="tok-o">+</span> <span class="tok-ss">&quot;%&quot;</span>
<span class="tok-n">db</span><span class="tok-p">.</span><span class="tok-k">execute</span><span class="tok-p">(</span><span class="tok-ss">&quot;SELECT * FROM places WHERE postal_code LIKE :q&quot;</span><span class="tok-p">,</span> <span class="tok-n">q</span><span class="tok-o">=</span><span class="tok-n">q</span><span class="tok-p">)</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>Notice how this example appends <code>%</code> to the user&#8217;s input, which happens to be SQL&#8217;s "wildcard" character that means "match any number of characters." The effect is that this query will return rows whose postal codes match whatever the user typed followed by any number of other characters. In other words, any of <code>0</code>, <code>02</code>, <code>021</code>, <code>0213</code>, and <code>02138</code> might return rows, as might any of <code>0</code>, <code>06</code>, <code>065</code>, <code>0651</code>, and <code>06511</code>.</p>
</div>
<div class="paragraph">
<p>If you&#8217;d like to support searching by more than just postal codes, keep in mind that SQL supports <code>OR</code> and <code>AND</code>!</p>
</div>
<div class="paragraph">
<p>To test <code>/search</code>, even before your text box is operational, simply visit URLs like</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>https://ide50-username.cs50.io/search?q=02138</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=Cambridge+MA</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=Cambridge,+MA</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=Cambridge,+Massachusetts</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=Cambridge,+Massachusetts,+US</code></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>or</p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>https://ide50-username.cs50.io/search?q=06511</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=New%20Haven+CT</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=New%20Haven,+CT</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=New%20Haven,+Connecticut</code></p>
</li>
<li>
<p><code>https://ide50-username.cs50.io/search?q=New+Haven,+Connecticut,+US</code></p>
</li>
</ul>
</div>
<div class="paragraph">
<p>and other such variants, where <code>username</code> is your own username, to see if you get back the JSON you expect. Again, though, we leave it to you to decide just how supportive <code>/search</code> will be of such variants. The more flexible, though, the better! Try to implement features that you yourself would expect as a user!</p>
</div>
<div class="paragraph">
<p>Feel free to tinker with the staff&#8217;s solution at <a href="http://mashup.cs50.net/" class="bare">http://mashup.cs50.net/</a>, inspecting its HTTP requests via Chrome&#8217;s Network tab as needed, if unsure how your own code should work!</p>
</div>
</div>
</div>
<div class="sect2">
<h3 id="scripts-js-2"><a class="link" href="#scripts-js-2"><code>scripts.js</code></a></h3>
<div class="paragraph">
<p>First, toward the top of <code>scripts.js</code>, you&#8217;ll see an anonymous function, inside of which is a definition of <code>options</code>, an object, one of whose keys is <code>center</code>, the value of which is an object with two keys of its own, <code>lat</code>, and <code>lng</code>. Per the comment alongside that object, your mashup&#8217;s map is currently centered on Stanford, California. (D&#8217;oh.) Change the coordinates of your map&#8217;s center to Cambridge (42.3770, -71.1256) or New Haven (41.3184, -72.9318) or anywhere else! (Though be sure to choose coordinates in the US if you downloaded <code>US.txt</code>!) Once you save your changes and reload your map, you should find yourself there! Zoom out as needed to confirm visually.</p>
</div>
<div class="paragraph">
<p>As before, feel free to tinker with the staff&#8217;s solution at <a href="http://mashup.cs50.net/" class="bare">http://mashup.cs50.net/</a>, inspecting its HTTP requests via Chrome&#8217;s Network tab as needed, if unsure how your own code should work!</p>
</div>
<div class="sect3">
<h4 id="configure-2"><a class="link" href="#configure-2"><code>configure</code></a></h4>
<div class="paragraph">
<p>Now that <code>/search</code> and your text box are (hopefully!) working, modify the value of <code>suggestion</code> in <code>configure</code>, the function in <code>scripts.js</code>, so that it displays matches (i.e., <code>place_name</code>, <code>admin_name1</code>, and/or other fields) instead of <code>TODO</code>. Recall that a value like</p>
</div>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code data-lang="html"><span></span><span class="tok-p">&lt;</span><span class="tok-nt">div</span><span class="tok-p">&gt;</span>{{place_name}}, {{admin_name1}}, {{postal_code}}<span class="tok-p">&lt;/</span><span class="tok-nt">div</span><span class="tok-p">&gt;</span></code></pre>
</div>
</div>
<div class="paragraph">
<p>might do the trick.</p>
</div>
</div>
<div class="sect3">
<h4 id="addmarker-2"><a class="link" href="#addmarker-2"><code>addMarker</code></a></h4>
<div class="paragraph">
<p>Implement <code>addMarker</code> in <code>scripts.js</code> in such a way that it adds a marker for <code>place</code> on the map, where <code>place</code> is a JavaScript object that represents a row from <code>places</code>. See <a href="https://developers.google.com/maps/documentation/javascript/markers" class="bare">https://developers.google.com/maps/documentation/javascript/markers</a> for tips. Note that the latest (experimental) version of Google&#8217;s API allows markers to have <a href="https://developers.google.com/maps/documentation/javascript/3.exp/reference#MarkerOptions">labels</a>.</p>
</div>
<div class="paragraph">
<p>When a marker is clicked, it should trigger the mashup&#8217;s info window to open, anchored at that same marker, the contents of which should be an unordered list of links to article for that article&#8217;s location (unless <code>/articles</code> outputs an empty array)!</p>
</div>
<div class="paragraph">
<p>Not to worry if some of your markers (or labels) overlap others, assuming such is the result of imperfections in Google&#8217;s API or <code>US.txt</code> and not your own code!</p>
</div>
<div class="paragraph">
<p>If you&#8217;d like to customize your markers' icon, see <a href="https://developers.google.com/maps/documentation/javascript/markers#simple_icons" class="bare">https://developers.google.com/maps/documentation/javascript/markers#simple_icons</a>. For the URLs of icons built-into Google Maps, see <a href="http://www.lass.it/Web/viewer.aspx?id=4" class="bare">http://www.lass.it/Web/viewer.aspx?id=4</a>. For third-party icons, see <a href="https://mapicons.mapsmarker.com/" class="bare">https://mapicons.mapsmarker.com/</a>.</p>
</div>
</div>
<div class="sect3">
<h4 id="removemarkers-2"><a class="link" href="#removemarkers-2">removeMarkers</a></h4>
<div class="paragraph">
<p>Implement <code>removeMarkers</code> in such a way that it removes all markers from the map (and deletes them). Odds are you&#8217;ll need <code>addMarker</code> to modify that global variable called <code>markers</code> in order for <code>removeMarkers</code> to work its own magic!</p>
</div>
</div>
</div>
</div>
</div>

<div class="sect1">
<h2 id="hints"><a class="link" href="#hints">Hints</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>You&#8217;re welcome center your map on some country other than the United States, downloading <a href="http://download.geonames.org/export/zip/">some other ZIP file</a> instead of <code>US.zip</code>. See <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">Wikipedia</a> if unfamiliar with ISO 3166-1 alpha-2 codes.</p>
</li>
<li>
<p>Know that you can use <code>console.log</code> much like you might use <code>eprintf</code> in C to log errors for debugging&#8217;s sake. You may want to do so as well! Just realize that <code>console.log</code> will log messages to the browser&#8217;s console (i.e., the <strong>Console</strong> tab of Chrome&#8217;s developer tools), not to your terminal window. See <a href="https://developer.mozilla.org/en-US/docs/Web/API/Console.log" class="bare">https://developer.mozilla.org/en-US/docs/Web/API/Console.log</a> for tips.</p>
</li>
</ul>
</div>
</div>
</div>
<div class="sect1">
<h2 id="faqs"><a class="link" href="#faqs">FAQs</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="create-table-places-failed-duplicate-column-name"><a class="link" href="#create-table-places-failed-duplicate-column-name">CREATE TABLE places(&#8230;&#8203;) failed: duplicate column name</a></h3>
<div class="paragraph">
<p>If you see this message upon running <code>.import</code> in <code>sqlite3</code>, odds are you haven&#8217;t run <code>sqlite3</code> in the same directory as <code>mashup.db</code>. If so, exit <code>sqlite3</code> with <code>.exit</code>, <code>cd</code> to your <code>mashup</code> directory, and then re-run <code>sqlite3 mashup.db</code>.</p>
</div>
</div>
<div class="sect2">
<h3 id="importerror-no-module-named-application"><a class="link" href="#importerror-no-module-named-application">ImportError: No module named 'application'</a></h3>
<div class="paragraph">
<p>By default, <code>flask</code> looks for a file called <code>application.py</code> in your current working directory (because we&#8217;ve configured the value of <code>FLASK_APP</code>, an environment variable, to be <code>application.py</code>). If seeing this error, odds are you&#8217;ve run <code>flask</code> in the wrong directory!</p>
</div>
</div>
<div class="sect2">
<h3 id="oserror-errno-98-address-already-in-use"><a class="link" href="#oserror-errno-98-address-already-in-use">OSError: [Errno 98] Address already in use</a></h3>
<div class="paragraph">
<p>If, upon running <code>flask</code>, you see this error, odds are you (still) have <code>flask</code> running in another tab. Be sure to kill that other process, as with ctrl-c, before starting <code>flask</code> again. If you haven&#8217;t any such other tab, execute <code>fuser -k 8080/tcp</code> to kill any processes that are (still) listening on TCP port 8080.</p>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="changelog"><a class="link" href="#changelog">CHANGELOG</a></h2>
<div class="sectionbody">
<div class="ulist">
<ul>
<li>
<p>2018-06-03</p>
<div class="ulist">
<ul>
<li>
<p>Updated the distribution code, updated the Search function, removed the need for student to have own API key and added another Hint about console.log</p>
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

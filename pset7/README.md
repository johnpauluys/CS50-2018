<html>
<body>
<div id="content">
<h1>C$50 Finance</h1>
<div class="sect1">
<h2 id="tldr"><a class="link" href="#tldr">tl;dr</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>Implement a website via which users can "buy" and "sell" stocks.</p>
</div>
</div>
</div>
<div class="sect1">
<h2 id="background"><a class="link" href="#background">Background</a></h2>
<div class="sectionbody">
<div class="paragraph">
<p>If you&#8217;re not quite sure what it means to buy and sell stocks (i.e., shares of a company), head to <a href="http://www.investopedia.com/university/stocks/" class="bare">http://www.investopedia.com/university/stocks/</a> for a tutorial.</p>
</div>
<div class="paragraph">
<p>You&#8217;re about to implement C$50 Finance, a web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks' actual prices and portfolios' values, it will also let you buy (okay, "buy") and sell (okay, "sell") stocks by querying <a href="https://iextrading.com/developer/">IEX</a> for stocks' prices.</p>
</div>
<div class="paragraph">
<p>Indeed, IEX lets you download stock quotes via URLs like <a href="https://api.iextrading.com/1.0/stock/NFLX/quote" class="bare">https://api.iextrading.com/1.0/stock/NFLX/quote</a>. Notice how Netflix&#8217;s symbol (NFLX) is embedded in this URL; that&#8217;s how IEX knows whose data to return.</p>
</div>
<div class="paragraph">
<p>Let&#8217;s turn our attention now to the app&#8217;s distribution code!</p>
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
<pre class="pygments highlight"><code>$ wget <a href="http://cdn.cs50.net/2018/x/psets/7/finance/finance.zip" class="bare">http://cdn.cs50.net/2018/x/psets/7/finance/finance.zip</a>
$ unzip finance.zip
$ rm finance.zip
$ cd finance
$ ls
application.py  helpers.py        static/
finance.db      requirements.txt  templates/</code></pre>
</div>
</div>
</div>
<div class="sect2">
<h3 id="running"><a class="link" href="#running">Running</a></h3>
<div class="olist arabic">
<ol class="arabic">
<li>
<p>Start Flask&#8217;s built-in web server (within <code>finance/</code>):</p>
<div class="listingblock">
<div class="content">
<pre class="pygments highlight"><code>flask run</code></pre>
</div>
</div>
<div class="paragraph">
<p>Visit the URL outputted by <code>flask</code> to see the distribution code in action. You won&#8217;t be able to log in or register, though, just yet!</p>
</div>
</li>
<li>
<p>Via CS50&#8217;s file browser, double-click <strong>finance.db</strong> in order to open it with phpLiteAdmin. Notice how <code>finance.db</code> comes with a table called <code>users</code>. Take a look at its structure (i.e., schema). Notice how, by default, new users will receive $10,000 in cash. But there aren&#8217;t (yet!) any users (i.e., rows) therein to browse.</p>
<div class="paragraph">
<p>Here on out, if you&#8217;d prefer a command line, you&#8217;re welcome to use <code>sqlite3</code> instead of phpLiteAdmin.</p>
</div>
</li>
</ol>
</div>
</div>
<div class="sect2">
<h3 id="understanding"><a class="link" href="#understanding">Understanding</a></h3>
<div class="sect3">
<h4 id="application-py"><a class="link" href="#application-py"><code>application.py</code></a></h4>
<div class="paragraph">
<p>Open up <code>application.py</code>. Atop the file are a bunch of imports, among them CS50&#8217;s SQL module and a few helper functions. More on those soon.</p>
</div>
<div class="paragraph">
<p>After configuring <a href="http://flask.pocoo.org/">Flask</a>, notice how this file disables caching of responses (provided you&#8217;re in debugging mode, which you are by default on CS50 IDE), lest you make a change to some file but your browser not notice. Notice next how it configures <a href="http://jinja.pocoo.org/">Jinja</a> with a custom "filter," <code>usd</code>, a function (defined in <code>helpers.py</code>) that will make it easier to format values as US dollars (USD). It then further configures Flask to store <a href="http://flask.pocoo.org/docs/0.12/quickstart/#sessions">sessions</a> on the local filesystem (i.e., disk) as opposed to storing them inside of (digitally signed) cookies, which is Flask&#8217;s default. The file then configures CS50&#8217;s SQL module to use <code>finance.db</code>, a SQLite database whose contents we&#8217;ll soon see!</p>
</div>
<div class="paragraph">
<p>Thereafter are a whole bunch of routes, only two of which are fully implemented: <code>login</code> and <code>logout</code>. Read through the implementation of <code>login</code> first. Notice how it uses <code>db.execute</code> (from CS50&#8217;s library) to query <code>finance.db</code>. And notice how it uses <code>check_password_hash</code> to compare hashes of users' passwords. Finally, notice how <code>login</code> "remembers" that a user is logged in by storing his or her <code>user_id</code>, an INTEGER, in <code>session</code>. That way, any of this file&#8217;s routes can check which user, if any, is logged in. Meanwhile, notice how <code>logout</code> simply clears <code>session</code>, effectively logging a user out.</p>
</div>
<div class="paragraph">
<p>Notice how most routes are "decorated" with <code>@login_required</code> (a function defined in <code>helpers.py</code> too). That decorator ensures that, if a user tries to visit any of those routes, he or she will first be redirected to <code>login</code> so as to log in.</p>
</div>
<div class="paragraph">
<p>Notice too how most routes support GET and POST. Even so, most of them (for now!) simply return an "apology," since they&#8217;re not yet implemented.</p>
</div>
</div>
<div class="sect3">
<h4 id="helpers-py"><a class="link" href="#helpers-py"><code>helpers.py</code></a></h4>
<div class="paragraph">
<p>Next take a look at <code>helpers.py</code>. Ah, there&#8217;s the implementation of <code>apology</code>. Notice how it ultimately renders a template, <code>apology.html</code>. It also happens to define within itself another function, <code>escape</code>, that it simply uses to replace special characters in apologies. By defining <code>escape</code> inside of <code>apology</code>, we&#8217;ve scoped the former to the latter alone; no other functions will be able (or need) to call it.</p>
</div>
<div class="paragraph">
<p>Next in the file is <code>login_required</code>. No worries if this one&#8217;s a bit cryptic, but if you&#8217;ve ever wondered how a function can return another function, here&#8217;s an example!</p>
</div>
<div class="paragraph">
<p>Thereafter is <code>lookup</code>, a function that, given a <code>symbol</code> (e.g., NFLX), returns a stock quote for a company in the form of a <code>dict</code> with three keys: <code>name</code>, whose value is a <code>str</code>, the name of the company; <code>price</code>, whose value is a <code>float</code>; and <code>symbol</code>, whose value is a <code>str</code>, a canonicalized (uppercase) version of a stock&#8217;s symbol, irrespective of how that symbol was capitalized when passed into <code>lookup</code>.</p>
</div>
<div class="paragraph">
<p>Last in the file is <code>usd</code>, a short function that simply formats a <code>float</code> as USD (e.g., <code>1234.56</code> is formatted as <code>$1,234.56</code>).</p>
</div>
</div>
<div class="sect3">
<h4 id="requirements-txt"><a class="link" href="#requirements-txt"><code>requirements.txt</code></a></h4>
<div class="paragraph">
<p>Next take a quick look at <code>requirements.txt</code>. That file simply prescribes the packages on which this app will depend.</p>
</div>
</div>
<div class="sect3">
<h4 id="static"><a class="link" href="#static"><code>static/</code></a></h4>
<div class="paragraph">
<p>Glance too at <code>static/</code>, inside of which is <code>styles.css</code>. That&#8217;s where some initial CSS lives. You&#8217;re welcome to alter it as you see fit.</p>
</div>
</div>
<div class="sect3">
<h4 id="templates"><a class="link" href="#templates"><code>templates/</code></a></h4>
<div class="paragraph">
<p>Now look in <code>templates/</code>. In <code>login.html</code> is, essentially, just an HTML form, stylized with <a href="http://getbootstrap.com/">Bootstrap</a>. In <code>apology.html</code>, meanwhile, is a template for an apology. Recall that <code>apology</code> in <code>helpers.py</code> took two arguments: <code>message</code>, which was passed to <code>render_template</code> as the value of <code>bottom</code>, and, optionally, <code>code</code>, which was passed to <code>render_template</code> as the value of <code>top</code>. Notice in <code>apology.html</code> how those values are ultimately used! And <a href="https://github.com/jacebrowning/memegen">here&#8217;s why</a>. 0:-)</p>
</div>
<div class="paragraph">
<p>Last up is <code>layout.html</code>. It&#8217;s a bit bigger than usual, but that&#8217;s mostly because it comes with a fancy, mobile-friendly "navbar" (navigation bar), also based on Bootstrap. Notice how it defines a block, <code>main</code>, inside of which templates (including <code>apology.html</code> and <code>login.html</code>) shall go. It also includes support for Flask&#8217;s <a href="http://flask.pocoo.org/docs/0.12/patterns/flashing/">message flashing</a> so that you can relay messages from one route to another for the user to see.</p>
</div>
</div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="specification"><a class="link" href="#specification">Specification</a></h2>
<div class="sectionbody">
<div class="sect2">
<h3 id="register"><a class="link" href="#register"><code>register</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>register</code> in such a way that it allows a user to register for an account.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Require that a user input a username, implemented a text field whose <code>name</code> is <code>username</code>. Render an apology if the user&#8217;s input is blank or the username already exists.</p>
</li>
<li>
<p>Require that a user input a password, implemented as a text field whose <code>name</code> is <code>password</code>, and then that same password again, implemented as a text field whose <code>name</code> is <code>confirmation</code>. Render an apology if either input is blank or the passwords do not match.</p>
</li>
<li>
<p>Submit the user&#8217;s input via <code>POST</code> to <code>/register</code>.</p>
</li>
<li>
<p><code>INSERT</code> the new user into <code>users</code>, storing a hash of the user&#8217;s password, not the password itself. Hash the user&#8217;s password with <a href="http://werkzeug.pocoo.org/docs/0.12/utils/#werkzeug.security.generate_password_hash"><code>generate_password_hash</code></a>.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to create a new template (e.g., <code>register.html</code>) that&#8217;s quite similar to <code>login.html</code>.</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Once you&#8217;ve implemented <code>register</code> correctly, you should be able to register for an account and log in (since <code>login</code> and <code>logout</code> already work)! And you should be able to see your rows via phpLiteAdmin or <code>sqlite3</code>.</p>
</div>
</div>
<div class="sect2">
<h3 id="quote"><a class="link" href="#quote"><code>quote</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>quote</code> in such a way that it allows a user to look up a stock&#8217;s current price.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Require that a user input a stock&#8217;s symbol, implemented as a text field whose <code>name</code> is <code>symbol</code>.</p>
</li>
<li>
<p>Submit the user&#8217;s input via <code>POST</code> to <code>/quote</code>.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to create two new templates (e.g., <code>quote.html</code> and <code>quoted.html</code>). When a user visits <code>/quote</code> via GET, render one of those templates, inside of which should be an HTML form that submits to <code>/quote</code> via POST. In response to a POST, <code>quote</code> can render that second template, embedding within it one or more values from <code>lookup</code>.</p>
</li>
</ul>
</div>
</div>
<div class="sect2">
<h3 id="buy"><a class="link" href="#buy"><code>buy</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>buy</code> in such a way that it enables a user to buy stocks.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Require that a user input a stock&#8217;s symbol, implemented as a text field whose <code>name</code> is <code>symbol</code>. Render an apology if the input is blank or the symbol does not exist (as per the return value of <code>lookup</code>).</p>
</li>
<li>
<p>Require that a user input a number of shares, implemented as a text field whose <code>name</code> is <code>shares</code>. Render an apology if the input is not a positive integer.</p>
</li>
<li>
<p>Submit the user&#8217;s input via <code>POST</code> to <code>/buy</code>.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to call <code>lookup</code> to look up a stock&#8217;s current price.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to <code>SELECT</code> how much cash the user currently has in <code>users</code>.</p>
</li>
<li>
<p>Add one or more new tables to <code>finance.db</code> via which to keep track of the purchase. Store enough information so that you know who bought what at what price and when.</p>
<div class="ulist">
<ul>
<li>
<p>Use appropriate SQLite types.</p>
</li>
<li>
<p>Define <code>UNIQUE</code> indexes on any fields that should be unique.</p>
</li>
<li>
<p>Define (non-<code>UNIQUE</code>) indexes on any fields via which you will search (as via <code>SELECT</code> with <code>WHERE</code>).</p>
</li>
</ul>
</div>
</li>
<li>
<p>Render an apology, without completing a purchase, if the user cannot afford the number of shares at the current price.</p>
</li>
<li>
<p>You don&#8217;t need to worry about race conditions (or use transactions).</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>Once you&#8217;ve implemented <code>buy</code> correctly, you should be able to see users' purchases in your new table(s) via phpLiteAdmin or <code>sqlite3</code>.</p>
</div>
</div>
<div class="sect2">
<h3 id="index"><a class="link" href="#index"><code>index</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>index</code> in such a way that it displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user&#8217;s current cash balance along with a grand total (i.e., stocks' total value plus cash).</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Odds are you&#8217;ll want to execute multiple <code>SELECT</code>s. Depending on how you implement your table(s), you might find <a href="https://www.google.com/search?q=SQLite+GROUP+BY">GROUP BY</a>, <a href="https://www.google.com/search?q=SQLite+HAVING">HAVING</a>, <a href="https://www.google.com/search?q=SQLite+SUM">SUM</a>, and/or <a href="https://www.google.com/search?q=SQLite+WHERE">WHERE</a> of interest.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to call <code>lookup</code> for each stock.</p>
</li>
</ul>
</div>
</div>
<div class="sect2">
<h3 id="sell"><a class="link" href="#sell"><code>sell</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>sell</code> in such a way that it enables a user to sell shares of a stock (that he or she owns).</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Require that a user input a stock&#8217;s symbol, implemented as a <code>select</code> menu whose <code>name</code> is <code>symbol</code>. Render an apology if the user fails to select a stock or if (somehow, once submitted) the user does not own any shares of that stock.</p>
</li>
<li>
<p>Require that a user input a number of shares, implemented as a text field whose <code>name</code> is <code>shares</code>. Render an apology if the input is not a positive integer or if the user does not own that many shares of the stock.</p>
</li>
<li>
<p>Submit the user&#8217;s input via <code>POST</code> to <code>/sell</code>.</p>
</li>
<li>
<p>You don&#8217;t need to worry about race conditions (or use transactions).</p>
</li>
</ul>
</div>
</div>
<div class="sect2">
<h3 id="history"><a class="link" href="#history"><code>history</code></a></h3>
<div class="paragraph">
<p>Complete the implementation of <code>history</code> in such a way that it displays an HTML table summarizing all of a user&#8217;s transactions ever, listing row by row each and every buy and every sell.</p>
</div>
<div class="ulist">
<ul>
<li>
<p>For each row, make clear whether a stock was bought or sold and include the stock&#8217;s symbol, the (purchase or sale) price, the number of shares bought or sold, and the date and time at which the transaction occurred.</p>
</li>
<li>
<p>You might need to alter the table you created for <code>buy</code> or supplement it with an additional table. Try to minimize redundancies.</p>
</li>
</ul>
</div>
</div>
<div class="sect2">
<h3 id="personal-touch"><a class="link" href="#personal-touch">personal touch</a></h3>
<div class="paragraph">
<p>Implement at least one personal touch of your choice:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Allow users to change their passwords.</p>
</li>
<li>
<p>Allow users to add additional cash to their account.</p>
</li>
<li>
<p>Allow users to buy more shares or sell shares of stocks they already own via <code>index</code> itself, without having to type stocks' symbols manually.</p>
</li>
<li>
<p>Require users' passwords to have some number of letters, numbers, and/or symbols.</p>
</li>
<li>
<p>Implement some other feature of comparable scope.</p>
</li>
</ul>
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
<p>Within <code>cs50.SQL</code> is an <code>execute</code> method whose first argument should be a <code>str</code> of SQL. If that <code>str</code> contains named parameters to which values should be bound, those values can be provided as additional named parameters to <code>execute</code>. See the implementation of <code>login</code> for one such example. The return value of <code>execute</code> is as follows:</p>
<div class="openblock">
<div class="content">
<div class="ulist">
<ul>
<li>
<p>If <code>str</code> is a <code>SELECT</code>, then <code>execute</code> returns a <code>list</code> of zero or more <code>dict</code> objects, inside of which are keys and values representing a table&#8217;s fields and cells, respectively.</p>
</li>
<li>
<p>If <code>str</code> is an <code>INSERT</code>, and the table into which data was inserted contains an autoincrementing <code>PRIMARY KEY</code>, then <code>execute</code> returns the value of the newly inserted row&#8217;s primary key.</p>
</li>
<li>
<p>If <code>str</code> is a <code>DELETE</code> or an <code>UPDATE</code>, then <code>execute</code> returns the number of rows deleted or updated by <code>str</code>.</p>
</li>
</ul>
</div>
</div>
</div>
<div class="paragraph">
<p>If an <code>INSERT</code> or <code>UPDATE</code> would violate some constraint (e.g., a <code>UNIQUE</code> index), then <code>execute</code> returns <code>None</code>. In cases of error, <code>execute</code> raises a <code>RuntimeError</code>.</p>
</div>
</li>
<li>
<p>Recall that <code>cs50.SQL</code> will log to your terminal window any queries that you execute via <code>execute</code> (so that you can confirm whether they&#8217;re as intended).</p>
</li>
<li>
<p>Be sure to use named bind parameters (i.e., a <a href="https://www.python.org/dev/peps/pep-0249/#paramstyle">paramstyle</a> of <code>named</code>) when calling CS50&#8217;s <code>execute</code> method, a la <code>WHERE name=:name</code>. Do <strong>not</strong> use f-strings, <a href="https://docs.python.org/3.1/library/functions.html#format"><code>format</code></a>, or <code>+</code> (i.e., concatenation), lest you risk a SQL injection attack.</p>
</li>
<li>
<p>If (and only if) already comfortable with SQL, you&#8217;re welcome to use <a href="http://docs.sqlalchemy.org/en/latest/index.html">SQLAlchemy Core</a> or <a href="http://flask-sqlalchemy.pocoo.org/">Flask-SQLAlchemy</a> (i.e., <a href="http://docs.sqlalchemy.org/en/latest/index.html">SQLAlchemy ORM</a>) instead of <code>cs50.SQL</code>.</p>
</li>
<li>
<p>You&#8217;re welcome to add additional static files to <code>static/</code>.</p>
</li>
<li>
<p>Odds are you&#8217;ll want to consult <a href="http://jinja.pocoo.org/docs/dev/">Jinja&#8217;s documentation</a> when implementing your templates.</p>
</li>
<li>
<p>It is <strong>reasonable</strong> to ask others to try out (and try to trigger errors in) your site. Via <strong>Share</strong> in CS50 IDE&#8217;s top-right corner can you share your <strong>Application</strong> by making it <strong>Public</strong>. Take care not to share your <strong>Editor</strong>, which would provide access to your Python code and SQLite database.</p>
</li>
<li>
<p>You&#8217;re welcome to alter the aesthetics of the sites, as via</p>
<div class="ulist">
<ul>
<li>
<p><a href="https://bootswatch.com/4-alpha/" class="bare">https://bootswatch.com/4-alpha/</a>,</p>
</li>
<li>
<p><a href="https://getbootstrap.com/docs/4.0/content/" class="bare">https://getbootstrap.com/docs/4.0/content/</a>,</p>
</li>
<li>
<p><a href="https://getbootstrap.com/docs/4.0/components/" class="bare">https://getbootstrap.com/docs/4.0/components/</a>, and/or</p>
</li>
<li>
<p><a href="https://memegen.link/api/templates" class="bare">https://memegen.link/api/templates</a>.</p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</div>
</div>
<div class="sect1">
<h2 id="faqs"><a class="link" href="#faqs">FAQs</a></h2>
<div class="sectionbody">
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
<div class="sect2">
<h3 id="check50-ran-into-an-error-while-running-checks"><a class="link" href="#check50-ran-into-an-error-while-running-checks">check50 ran into an error while running checks!</a></h3>
<div class="paragraph">
<p>If, upon running <code>check50</code>, you see this error, odds are you have a bug in your code somewhere! Open up the CS50.me produced by <code>check50</code> to see a detailed traceback to help you debug!</p>
</div>
</div>
</div>
</div>
</div>
</body>
</html>

Title: Regular Expressions Cookbook Detailed Solutions in Eight Programming Languages  By Jan Goyvaerts, Steven Levithan
Date: 2009/06/15 00:00:00 GMT-5
Modified: 2009/06/15 00:00:00 GMT-5
Authors: Tony Cappellini
Category: BookReview
Tags: BookReview
Slug: RegularExpressionsCookbookDetailedSolutionsinEightProgrammingLanguagesByJanGoyvaerts_StevenLevithan__TonyCappellini
Summary: I was glad to hear another book on Regular Expressions was in the making, I couldn’t wait for a review copy. I have been a user of Jan Goyvaerts’ regex software tools for just over a year now even though I had often-encountered the websites authored by him, while googling for Regular Expression resources. In one of his blog entries, I came across a notice of this forthcoming book, and emailed O’Reilly that I would like to be a reviewer. 


<p><img class="image-left" src="../images/2009/RegexCookbook.gif/image_preview" alt="Regular Expressions Cookbook" />For me, Regular Expressions 
have always been a curse because I only use them only a few times a 
year. I never get enough exposure to the point where I can memorize 
them, let a lone master them. A cookbook on Regular Expressions is just 
the thing I’ve been waiting for.</p>
<p>Mr. Goyvaerts is recognized 
as a regular expression expert and maintains a blog at <a href="http://www.regexguru.com/" target="_blank"><u>http://www.regexguru.com/</u></a>. There are many useful tidbits there, 
I recommend following his blog regularly, if you want to keep up your 
regex chops. <a href="http://www.regular-expressions.info/" target="_blank"><u>http://www.regular-expressions.info/</u></a> is yet another site authored by Mr. 
Goyvaerts, which also contains a wealth of information on regexes. Prior 
to getting this book, I had downloaded the regex tutorial in PDF format 
a few months back, and would assume this document may have led to the 
development of the cookbook.</p>
<p>One of the more interesting 
aspects of the authors’ background is that he has become quite well-versed 
on regexes in many different programming languages. His regex software 
tools offer regex support for many languages and this book also follows 
suit. In typical cookbook fashion, each chapter cites a problem and 
solution. This book goes further and shows you differences between many <em>
flavors </em>of regular expressions. .NET, Java, JavaScript, PCRE, Perl, 
Python, and Ruby are the most commonly used and thus are the languages 
covered in the recipes in this book. Additionally, the recipes 
discuss variations of each problem/solution pair, and are often cross-referenced 
with other solutions within the book. There are even “gotchas” emblazoned 
with a bear trap icon describing particularly easy-to-stumble-on problem 
areas. What more could you ask for?</p>
<p>Upon receiving the book, I 
was pleased with the size of the book. The index ends on page 493. 
Browsing the table of contents reveals <em>over</em> 100 Regular Expression 
recipes which are logically and well organized into 8 chapters.</p>
<p>The first chapter gives a brief 
introduction and history into Regular Expressions, as well as references 
to many regular expression tools. This is a perfect way for someone 
who is completely new to regular expressions to get started understanding 
them. Having the right tool to help you construct the right regex is 
extremely valuable. Regex Buddy was the first program I used from Mr. 
Goyvaerts Company, and have referred it to colleagues and friends. It 
will definitely help eliminate some of the frustration of learning regular 
expressions. Many times I have thought that the name “Regular 
Expressions” is inappropriate for the strings of gibberish that so 
many of us labor to get right. Where did the name come from? It should 
be no surprise that this book also explains the ‘History of the Term 
Regular Expression’</p>
<p>Chapter Two covers “Regular 
Expression Skills” and is full of many recipes covering much-needed 
basics of regular expressions. Having looked over the titles for each 
recipe they are all very practical, well-explained and not contrived. 
You <em>will</em> find use for many of these recipes in your day-day programming 
tasks.</p>
<p>Chapters 4-8 are full of Regular 
Expressions to solve real-world problems, and the solutions span the 
many different regex flavors mentioned earlier.</p>
<p>If there were one recipe I 
would have preferred to see in this book, it would be a regex to find 
or skip C/C++ code inside of C comments. Since C comments can span multiple 
lines, there are probably many pitfalls here just waiting for a casual 
regex user like myself.</p>
<p>One feature I’d like to see 
from the publisher is that the source code be made available for download. 
Regular Expressions can be very complicated and it would be very easy 
to mistype one, thus creating other problems. Downloadable source code 
would help to eliminate this.</p>
<p>This is an example of a recipe 
I could have used many times in the past.</p>
<p><strong>Problem</strong> #5.7, Page 300.</p>
<p>“Find Words Near Each Other.</p>
<p>You want to emulate a NEAR 
search using a regular expression. For readers unfamiliar with the term, 
some search tools that use Boolean operators such as NOT and OR also 
have a special operator called NEAR. Searching for “word1 NEAR word2” 
finds <u>word1</u> and <u>word2</u> in any order, as long as they occur 
within a certain distance of each other.</p>
<p><strong>Solution </strong>
(the reader <strong>should</strong> substitute word1 and word2 with their terms 
of interest. This solution allows up to five words to separate word1 
and word2)</p>
<p>\b(?:word1\W+(?:\w+\W+){0,5}?word2|word2\W+(?:\w+\W+){0,5}?word1)\b</p>
<p><strong>Regex 
options:</strong> Case insensitive</p>
<p><strong>Regex 
Flavors:</strong> .NET, Java, JavaScript, PCRE, Perl, Python, Ruby”</p>
<p>Having my last name mispronounced 
since I was old enough to remember, I was curious how Mr. Goyvaerts 
pronounces his last name. Well, there’s even a webpage for that too,</p>
<p><a href="http://www.just-great-software.com/aboutjg.html" target="_blank"><u>http://www.just-great-software.com/aboutjg.html</u></a>, as well as an introduction on Mr. 
Goyvaerts’ background. I’ve found these to be informative and recommend 
his blogs as supplements to his book.</p>
<p>Overall, I’m very satisfied 
with Regular Expressions Cookbook, and recommend it to everyone just 
learning or brushing up on their regular expression skills. Armed with 
this book, and some of the software tools mentioned in Chapter 1, you’ll 
be ready to tackle an upcoming programming assignment using a Regular 
Expression or two.</p>


Title: R In A Nutshell by Joseph Adler. Reviewed by Raj Jammalamadaka
Date: 2010/07/13 00:30:00 GMT-5
Modified: 2010/07/13 00:30:00 GMT-5
Authors: baypiggie_member
Category: BookReview
Tags: BookReview
Slug: RInANutshellbyJosephAdler_ReviewedbyRajJammalamadaka__baypiggie_member
Summary: This book is a very good introduction to the R programming language. R is a free, general purpose programming language(with a strong support for doing statistics). The language has its idiosyncrasies. For example, the assignment operator is denoted by a reverse arrow (x<-2); this book does a pretty good job of explaining all these in detail. Once you get past these details, you will find that R is a pretty versatile language.


<p><img class="image-left" src="../images/2010/r_nutshell_cover.gif/image_preview" alt="R In a Nutshell cover image" /></p>
<p>Let us take an example (source: <a class="external-link" href="http://www.r-bloggers.com/stock-analysis-using-r/">http://www.r-bloggers.com/stock-analysis-using-r/</a>). The following code installs the quantmod package and then displays the stock of Apple along with Bollinger Bands (<a class="external-link" href="http://www.bollingerbands.com/">http://www.bollingerbands.com/</a>).</p>
<p><br />install.packages("quantmod") # installs the package quantmod<br />library(quantmod) # loads the package<br />getSymbols("AAPL") # load Apple's data<br />chartSeries(AAPL) # Create financial charts<br />addBBands() # Add the Bollinger Bands.</p>
<p></p>
<p></p>
<p></p>
<p align="left">The graph below was created using the steps above.</p>
<p><img class="image-inline" src="../images/2010/r_nutshel_graph.png/image_preview" alt="R In A Nutshell - Graph" /></p>
<p><br />One of the best parts of R is huge support of libraries for doing commercial grade statistics and the plots/graphs produced by R are of high quality.<br />Though I didn't get a chance to try it out, there is a package called RPy which is a Python interface to the R programming language. More details can be found here: http://rpy.sourceforge.net/<br /><br />If you are mathematically inclined, definitely check this book out. Once you learn R, you can use it anywhere/anytime without ever paying a license fee.</p>


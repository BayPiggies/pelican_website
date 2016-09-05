Title: The iPhone Developer's Cookbook: Building Applications with the iPhone SDK by Erica Sadun
Date: 2009/03/15 21:00:00 GMT-5
Modified: 2009/03/15 21:00:00 GMT-5
Authors: William Deegan
Category: BookReview
Tags: BookReview
Slug: TheiPhoneDeveloper'sCookbook:BuildingApplicationswiththeiPhoneSDKbyEricaSadun__WilliamDeegan
Summary: Even before I finally got an iphone 3G, I was very curious about programming it and when the iphone App store took off, well that just sweetened the pot...


<p><img class="image-left" src="../images/2009/iphoneDevCookbook.jpeg/image_preview" alt="IphoneCookbook" />First off let me warn you that this review will be a bit different from others on this site, and different from my previous reviews. It's taking me much longer to make my way through this book than I had planned. So I'll be adding content as I complete each section. (Skip to the bottom if you want to see my conclusion on this book)</p>
<p class="callout">Chapter 1</p>
<p>If you've never programmed in objective-C like me, then you'll likely have to take a break for station identification while you find another resource (apple has some decent docs online about objective-c) to familiarize yourself with the syntax and semantics of objective-C, which are different enough that I couldn't really understand the sample code in chapter one without it.</p>
<p>O.k. so after the intermission where I read enough docs to understand the sample code, it was off to apple's website to download and install the iPhone SDK and XCode. Note that the 2.2 version of SDK is slightly different than the version used to write the book with. I'll try and make some notes about where they are different enough to be noteworthy.</p>
<p>Also, if you don't own a mac (or a hackintosh), then you better take another break to go purchase one (as I did), because you won't be programming with Xcode on any other platform.</p>
<p>O.k. so you've got your spanking new mac, loaded with xcode and the iPhone SDK, now you're ready to work through the expected "Hello world" iphone application, and run it in a simulator. (Nope you can't load it onto your (non-jailbroken) iPhone without joining apples iPhone developer program $99/year or $299/year depending). You'll also learn about how to do basic debugging in this chapter. You'll learn about the various profiling tools (though not use them yet) for power, speed, memory.</p>
<p>Finally chapter one will walk you through joining the developer program, registering your iPhone (or iPod touch) as development hardware and then connecting it to XCode.</p>
<p>So one thing which was tricky is that your better off making your App ID with the reverse domain wildcard com.yourdomain.\* the .\* is the key part. Then make sure you name your bundle id com.yourdomain.anything. The error messaging when you get this wrong is not helpful at all.</p>
<p>One very important item to note, when you're trying to create a Distribution provision, read all the way to the end of the first chapter, (so read <strong>Compiling for Distribution</strong> and the whole <strong>Ad Hoc Distribution</strong> section) or you will waste a lot of time trying to figure out why you fail to load your new distribution ready app onto your iPhone (or iTouch).</p>
<p></p>
<p>Well I finally completed the book, and started reading a much better book (at least for learning iPhone programming, review forthcoming).</p>
<p>So let me make the following recommendation, if you're not a Mac OSX carbon experienced programmer who's just looking for tricks and tweaks, and cookbookish info, don't get this book for your introductory to iPhone programming. Beginning iPhone Development (By APRESS) is much better book for that purpose.</p>
<p></p>


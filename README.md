Twitmote
========

Turn your Twitter account into a remote control service for your computer!

About
-----
Twitmote is a service that runs on your computer and periodically checks for Direct Messages on a Twitter account of your choice.  If the Direct Message meets one of the criteria you set up, any command can be triggered on your computer.

This was originally a Perl project called "KTRC: Kyle's Twitter Remote Control."  I wrote it back in December of 2008 before I had a data plan on my phone but still wanted to stay connected.  I knew Twitter had a pretty solid (and free!) text message interface and API, so I realized I could connect my phone to my computer (and thus, the Internet) with just a bit of work!  The first milestone was the ability to play and pause Winamp via text.  Later, I got Halo 3 stats delivered via a return Direct Message.

Now the project has been rewritten in Python and I use it from time-to-time on my Mac to execute anything I would normally type into Terminal.  Perhaps my favorite command is Apple's text-to-speech command, `say`.  I have a Twitter account that I use exclusively for this purpose, and because only those that I follow can Direct Message me, I don't need to worry about malicious messages.  (Additional security can be implemented on the server with ease, though.)  I just have my bot set to follow me.

Important Note
--------------
As of June 2010, this no longer works due to Twitter's API switching to OAuth for authentication.  Pull requests implementing a fix are welcome!

---
title: Updating to Nextcloud client 3.6.1 broke sync
date: 2022-11-01 17:41:00 - 500
categories: [nextcloud, troubleshooting]
tag: [nextcloud, server, proxy] # All lowercase
layout: post
---

Nextcloud, I try to treat you right. I try to keep you happy and healthy and updated. But when I do you return the favor with things like this.

I use the Snap Desktop client on my Ubuntun desktop to sync Nextcloud locally. It had been asking for an update for awhile, so I refreshed the Snap package to version 3.6.1 and was greeted with this.

*The polling URL does not start with HTTPS despite the login URL starting with HTTPS. Login will not be possible because this might be a security issue.* 

I found the solution from this Internet Hero who both had a question and then a day later [returned with an answer to his own question and posted it](https://help.nextcloud.com/t/the-polling-url-does-not-start-with-https-despite-the-login-url-started-with-https/137576/2)


Add these two lines to your Nextcloud server config file. I added them to the bottom of the file, make sure to include the trailing commas on each line.

```
  'overwrite.cli.url' => 'https://domain.ltd',
  'overwriteprotocol' => 'https',
```

Now the Desktop Sync Clients are working again and no longer prompting me to login to the browser, then failing to do anything.
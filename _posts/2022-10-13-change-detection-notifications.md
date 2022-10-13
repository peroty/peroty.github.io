---
title: Configure Dreamhost mail servers for Apprise notifications
date: 2022-10-13 14:26:00 - 500
categories: [email, smtp, notifications] 
tag: [changedetection, notification, email] # All lowercase
layout: post
---

# Change Detection

I've been working on getting the [Change Detection](https://github.com/dgtlmoon/changedetection.io) project installed and setup with email notifications. Part of my job is keeping track of Webex changes and updates across their various platforms and APIs. I am signed up for as many things as they offer, but sometimes they make changes, removing features and changing how things work without notice. It's my plan to use this to keep on top of those changes, as they happen.

This led to my struggle in getting email notifications setup. If I want to use a standard email service like hotmail, that was very simple to setup using the [apprise wiki email notification docs](https://github.com/caronc/apprise/wiki/Notify_email). However, Dreamhots is another beast.

Dreamhost is a struggle to get the emails working because it requires specifying the smtp server as a different domain from my email domain and setting the username as the full email address (user@domain.tld).

It took a lot of trial and error but eventually stumbling across this comment in an issue thread. [@ symbol in email username · Issue #513 · caronc/apprise](https://github.com/caronc/apprise/issues/513)

> Another variation you can try is:
> mailtos://nattaylor.com?password=password&user=nat@nattaylor.com&smtp=smtp.migadu.com

My working example for my alerts email, password redacted.

```
mailtos://peroty.com?password=PASSWORD&user=alerts@peroty.com&smtp=smtp.dreamhost.com
```

The format I need to use is:

```
mailtos://EXAMPLE.COM?password=PASSWORDg&user=USER@DOMAIN.TLD&smtp=smtp.DOMAIN.TLD
```
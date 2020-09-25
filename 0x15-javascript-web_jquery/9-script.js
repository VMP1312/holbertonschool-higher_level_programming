#!/usr/bin/node
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, info => $('#hello').text(info.hello));

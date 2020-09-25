#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, info => $('#character').text(info.name));

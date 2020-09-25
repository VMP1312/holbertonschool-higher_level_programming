#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (info) {
  $('.result').html(info);
  let cnt = 0;
  for (cnt = 0; cnt < info.count; cnt++) {
    $('#list_movies').add('<li>' + info.results[cnt].title + '</li>').appendTo('#list_movies');
  }
});

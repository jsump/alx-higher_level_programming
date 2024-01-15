$(document).ready(function () {
  $('#fetch_movies').click(function () {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      success: function (data) {
        data.results.forEach(function (movie) {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      }
    });
  });
});

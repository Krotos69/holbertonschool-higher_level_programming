// Fetch all Star Wars films and list their titles in #list_movies

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');

    data.results.forEach(movie => {
      const item = document.createElement('li');
      item.textContent = movie.title;
      list.appendChild(item);
    });
  });

// When the user clicks the #toggle_header element,
// toggle the header class between "red" and "green"

document.querySelector('#toggle_header').addEventListener('click', () => {
  const header = document.querySelector('header');

  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});

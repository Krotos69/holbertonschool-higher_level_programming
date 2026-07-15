// When the user clicks the #red_header element,
// add the class "red" to the <header> element

document.querySelector('#red_header').addEventListener('click', () => {
  document.querySelector('header').classList.add('red');
});

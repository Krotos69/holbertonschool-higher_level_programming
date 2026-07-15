// When the user clicks the #red_header element,
// update the <header> text color to red (#FF0000)

document.querySelector('#red_header').addEventListener('click', () => {
  document.querySelector('header').style.color = '#FF0000';
});

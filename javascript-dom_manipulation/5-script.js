// When the user clicks the #update_header element,
// update the <header> text to "New Header!!!"

document.querySelector('#update_header').addEventListener('click', () => {
  document.querySelector('header').textContent = 'New Header!!!';
});

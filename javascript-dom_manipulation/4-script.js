// When the user clicks the #add_item element,
// add a new <li>Item</li> to the <ul> with class "my_list"

document.querySelector('#add_item').addEventListener('click', () => {
  const list = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});

document.addEventListener('DOMContentLoaded', () => {
  const list = $('ul.my_list');
  $('div#add_item').on('click', (e) => {
    list.append('<li>Item</li>');
  });
  $('div#remove_item').on('click', (e) => {
    $('ul.my_list li:last-child').remove();
  });
  $('div#clear_list').on('click', (e) => {
    list.text('');
  });
});

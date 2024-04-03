$(document).ready(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (result) {
      $('div#hello').text(result.hello);
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  $('input#btn_translate').on('click', (e) => {
    const language = $('input#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${language}`,
      success: function (result) {
        $('div#hello').text(result.hello);
      }
    });
  });
});

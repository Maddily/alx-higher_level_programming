$(document).ready(() => {
  /**
   * Fetches and prints 'Hello' in a language chosen by a user.
   */
  function translateHello () {
    const language = $('input#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${language}`,
      success: function (result) {
        $('div#hello').text(result.hello);
      }
    });
  }

  $('input#btn_translate').on('click', translateHello);

  $('input#language_code').keyup((e) => {
    if (e.key === 'Enter') {
      translateHello();
    }
  });
});

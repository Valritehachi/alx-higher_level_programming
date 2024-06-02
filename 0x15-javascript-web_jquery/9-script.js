// Add an event listener to the document that will trigger
$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').append(data.hello);
    }
  });
});

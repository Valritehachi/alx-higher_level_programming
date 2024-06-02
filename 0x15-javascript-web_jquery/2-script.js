// Add an event listener to the document that will trigger
$(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').css({ color: '#FF0000' });
  });
});

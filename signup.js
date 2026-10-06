/* Newsletter sign-up (Buttondown). Set BUTTONDOWN_USER to the account's username once it exists;
   until then the form explains that the list is opening soon. Buttondown adds no tracking. */
(function () {
  var BUTTONDOWN_USER = 'mkbaines';
  document.querySelectorAll('form.bd').forEach(function (f) {
    var msg = f.querySelector('.msg');
    if (BUTTONDOWN_USER) {
      f.action = 'https://buttondown.com/api/emails/embed-subscribe/' + BUTTONDOWN_USER;
      f.method = 'post';
      f.target = '_blank';
      return;
    }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      msg.textContent = 'The list opens very soon. Until then, write to mkb.info@proton.me and you will be added the day it opens.';
    });
  });
})();

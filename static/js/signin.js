document.addEventListener('DOMContentLoaded', () => {
  const formElm = document.getElementById(`signin-form`);
  formElm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    Client.sign_in(formData).then(resp => {
      console.log(resp);
      if (resp.error) {
        utils.flash_message(resp.message, 'is-danger');
        return;
      }

      utils.flash_message(resp.message, 'is-success');
      setTimeout(() => {
        const route = `/users/${resp.username}`;
        window.location.href = route;
      }, 2000);
    });
  });
});

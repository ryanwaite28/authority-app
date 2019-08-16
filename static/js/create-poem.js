document.addEventListener('DOMContentLoaded', () => {
  const formElm = document.getElementById(`create-form`);
  const inputs = formElm.elements;

  inputs['poem-icon'].addEventListener('change', () => {
    const file = inputs['poem-icon'].files[0];
    if (!file) {
      return;
    }
    document.getElementById('poem-filename').innerText = file.name;
  });

  formElm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    Client.create_poem(formData).then(resp => {
      console.log(resp);
      if (resp.error) {
        utils.flash_message(resp.message, 'is-danger');
        return;
      }

      utils.flash_message(resp.message, 'is-success');
      setTimeout(() => {
        const route = `/poems/${resp.poem.id}`;
        window.location.href = route;
      }, 1000);
    });
  });
});

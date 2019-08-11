document.addEventListener('DOMContentLoaded', () => {
  const formElm = document.getElementById(`create-form`);
  formElm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    Client.create_story(formData).then(resp => {
      console.log(resp);
      if (resp.error) {
        utils.flash_message(resp.message, 'is-danger');
        return;
      }

      utils.flash_message(resp.message, 'is-success');
      setTimeout(() => {
        const route = `/stories/${resp.story.id}`;
        window.location.href = route;
      }, 1000);
    });
  });
});

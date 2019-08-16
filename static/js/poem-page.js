document.addEventListener('DOMContentLoaded', () => {
  let you, user, poem;
  let poemBoxComponent;
  const storyBoxElm = document.getElementById('poem-box');

  const poem_id = parseInt(window.location.pathname.split('/').pop(), 10);
  const get_you_promise = Client.check_session();
  const get_poem_promise = Client.get_poem_full_by_id(poem_id);

  const init = () => {
  poemBoxComponent = Components.create_poem_full_card(poem);
    m.mount(storyBoxElm, poemBoxComponent);
  };

  Promise.all([get_you_promise, get_poem_promise])
  .then(values => {
    console.log(values);
    you = values[0].user;
    poem = values[1].poem;
    user = poem.owner;
    init();
  });
});

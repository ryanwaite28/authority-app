document.addEventListener('DOMContentLoaded', () => {
  
  let users = [];
  let poems = [];
  let stories = [];

  const usersBoxElm = document.getElementById('users-box');
  const poemsBoxElm = document.getElementById('poems-box');
  const storiesBoxElm = document.getElementById('stories-box');

  Promise.all([
    Client.get_random_users(),
    Client.get_random_poems(),
    Client.get_random_stories(),
  ]).then(values => {
    console.log(values);

    users = values[0].users;
    poems = values[1].poems;
    stories = values[2].stories;

    const usersListComponent = Components.create_user_card_compact_list(users);
    const poemsListComponent = Components.create_poem_card_compact_list(poems);
    const storiesListComponent = Components.create_story_card_compact_list(stories);

    m.mount(usersBoxElm, usersListComponent);
    m.mount(poemsBoxElm, poemsListComponent);
    m.mount(storiesBoxElm, storiesListComponent);
  });

});

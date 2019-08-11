document.addEventListener('DOMContentLoaded', () => {
  let you, user, story;
  let storyBoxComponent;
  const storyBoxElm = document.getElementById('story-box');

  const story_id = parseInt(window.location.pathname.split('/').pop(), 10);
  const get_you_promise = Client.check_session();
  const get_story_promise = Client.get_story_full_by_id(story_id);

  const init = () => {
    storyBoxComponent = Components.create_story_full_card(story);
    m.mount(storyBoxElm, storyBoxComponent);
  };

  Promise.all([get_you_promise, get_story_promise])
  .then(values => {
    console.log(values);
    you = values[0].user;
    story = values[1].story;
    user = story.owner;
    init();
  });
});

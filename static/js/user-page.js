document.addEventListener('DOMContentLoaded', () => {
  let you, user, isYourPage;
  let userMainBoxComponent;
  const userMainBoxElm = document.getElementById('user-main-box');
  const userInfoBoxElm = document.getElementById('user-info-box');

  const username = window.location.pathname.split('/').pop();
  const get_you_promise = Client.check_session();
  const get_user_promise = Client.get_user_profile_by_username(username);

  const init = () => {
    isYourPage = you.id === user.id;
    userMainBoxComponent = Components.create_user_profile_card(user);
    m.mount(userMainBoxElm, userMainBoxComponent);
  };

  Promise.all([get_you_promise, get_user_promise])
  .then(values => {
    you = values[0].user || {};
    user = values[1].user || {};
    init();
  });
});

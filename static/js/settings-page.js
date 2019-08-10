document.addEventListener('DOMContentLoaded', () => {
  let you;
  let userMainBoxComponent;

  const userMainBoxElm = document.getElementById('user-main-box');
  const updateAccountForm = document.getElementById('update-account-form');
  const inputs = updateAccountForm.elements;

  const init = () => {
    render();
    console.log(inputs, you);
    
    inputs['displayname'].value = you.displayname;
    inputs['username'].value = you.username;
    inputs['email'].value = you.email;
    inputs['weblink'].value = you.weblink;
    inputs['bio'].value = you.bio;
    if (you.is_private) {
      inputs['visibility'][1].checked = true;
    } else {
      inputs['visibility'][0].checked = true;
    }

    inputs['profile-icon'].addEventListener('change', () => {
      const file = inputs['profile-icon'].files[0];
      if (!file) {
        return;
      }
      document.getElementById('icon-filename').innerText = file.name;
    });
    inputs['profile-wallpaper'].addEventListener('change', () => {
      const file = inputs['profile-wallpaper'].files[0];
      if (!file) {
        return;
      }
      document.getElementById('wallpaper-filename').innerText = file.name;
    });
  };

  const render = () => {
    userMainBoxComponent = Components.create_user_profile_card(you);
    m.mount(userMainBoxElm, userMainBoxComponent);
  };

  const clearForm = () => {
    inputs['profile-icon'].value = null;
    inputs['profile-wallpaper'].value = null;
    inputs['old_password'].value = null;
    inputs['password'].value = null;
    inputs['password_confirm'].value = null;
    document.getElementById('icon-filename').innerText = '';
    document.getElementById('wallpaper-filename').innerText = '';
  };

  // update_account
  updateAccountForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    Client.update_account(formData).then(resp => {
      console.log(resp);
      if (resp.error) {
        utils.flash_message(resp.message, 'is-danger');
        return;
      }
      you = resp.user;
      utils.flash_message(resp.message, 'is-success');
      render();
      clearForm();
    });
  });

  Client.check_session().then(resp => {
    you = resp.user;
    init();
  });
});

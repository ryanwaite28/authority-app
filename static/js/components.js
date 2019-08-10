const Components = (function(){
  function create_user_card (user) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
          m('div', { class: 'card-image' }, [
            m('figure', { class: 'image is-4by3' }, [
              m('img', { class: '', src: user.wallpaper_link }),
            ]),
          ]),
          m('div', { class: 'card-content' }, [
            m('div', { class: 'media' }, [
              m('div', { class: 'media-left' }, [
                m('figure', { class: 'image is-48x48' }, [
                  m('img', { class: '', src: user.icon_link }),
                ]),
              ]),
              m('div', { class: 'media-content' }, [
                m('p', { class: 'title is-4' }, user.displayname),
                m('p', { class: 'subtitle is-6' }, [
                  m('a', { href: `/users/${user.username}` }, `@${user.username}`),
                ]),
              ]),
            ]),
            m('div', { class: 'content' }, (user.bio || '...')),
          ]),
          m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/poems`, class: 'card-footer-item' }, 'Poems'),
            m('a', { href: `/users/${user.username}/stories`, class: 'card-footer-item' }, 'Stories'),
            m('a', { href: `/users/${user.username}/books`, class: 'card-footer-item' }, 'Books'),
          ]),
        ]);
      }
    };
    return component;
  }

  function create_user_profile_card (user) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
          m('div', { class: 'card-image' }, [
            m('figure', { class: 'image is-4by3' }, [
              m('img', { class: '', src: user.wallpaper_link }),
            ]),
          ]),
          m('div', { class: 'card-content' }, [
            m('div', { class: 'media' }, [
              m('div', { class: 'media-left' }, [
                m('figure', { class: 'image is-48x48' }, [
                  m('img', { class: '', src: user.icon_link }),
                ]),
              ]),
              m('div', { class: 'media-content' }, [
                m('p', { class: 'title is-4' }, user.displayname),
                m('p', { class: 'subtitle is-6' }, [
                  m('a', { href: `/users/${user.username}` }, `@${user.username}`),
                ]),
              ]),
            ]),
            m('div', { class: 'content' }, [
              m('p', { class: 'is-size-5' }, (user.bio || '...')),
              m('p', { class: '' }, `Following: ${user.following_count}`),
              m('p', { class: '' }, `Followers: ${user.followers_count}`),
              m('p', { class: '' }, `Reviews: ${user.reviews_count}`),
              m('p', { class: '' }, `Poems: ${user.poems_count}`),
              m('p', { class: '' }, `Stories: ${user.stories_count}`),
              m('p', { class: '' }, `Books: ${user.books_count}`),
            ]),
          ]),
          m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/poems`, class: 'card-footer-item' }, 'Poems'),
            m('a', { href: `/users/${user.username}/stories`, class: 'card-footer-item' }, 'Stories'),
            m('a', { href: `/users/${user.username}/books`, class: 'card-footer-item' }, 'Books'),
          ]),
        ]);
      }
    };
    return component;
  }

  // 

  return Object.freeze({
    create_user_card,
    create_user_profile_card,
  });

})();
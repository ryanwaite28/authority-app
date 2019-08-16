const Components = (function(){
  function create_user_card (user) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
          m('div', { class: 'card-image' }, [
            m('figure', { class: 'image is-5by3' }, [
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
          ]),
          m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/poems`, class: 'card-footer-item' }, 'Poems'),
            m('a', { href: `/users/${user.username}/stories`, class: 'card-footer-item' }, 'Stories'),
            m('a', { href: `/users/${user.username}/books`, class: 'card-footer-item' }, 'Books'),
          ]),
           m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/reviews`, class: 'card-footer-item' }, 'Reviews'),
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
            m('figure', { class: 'image is-5by3' }, [
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
              m('p', { class: 'is-size-6' }, (user.tags || '...')),
              m('div', { class: 'columns' }, [
                m('div', { class: 'column' }, [
                  m('p', { class: '' }, `Following: ${user.following_count}`),
                  m('p', { class: '' }, `Followers: ${user.followers_count}`),
                  m('p', { class: '' }, `Reviews: ${user.reviews_count}`),
                ]),
                m('div', { class: 'column' }, [
                  m('p', { class: '' }, `Poems: ${user.poems_count}`),
                  m('p', { class: '' }, `Stories: ${user.stories_count}`),
                  m('p', { class: '' }, `Books: ${user.books_count}`),
                ]),
              ]),
            ]),
          ]),
          m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/poems`, class: 'card-footer-item' }, 'Poems'),
            m('a', { href: `/users/${user.username}/stories`, class: 'card-footer-item' }, 'Stories'),
            m('a', { href: `/users/${user.username}/books`, class: 'card-footer-item' }, 'Books'),
          ]),
          m('footer', { class: 'card-footer' }, [
            m('a', { href: `/users/${user.username}/reviews`, class: 'card-footer-item' }, 'Reviews'),
          ]),
        ]);
      }
    };
    return component;
  }

  function create_poem_full_card (poem) {
    const cardChildren = [
      m('div', { class: 'card-content' }, [
        m('div', { class: 'media' }, [
          m('div', { class: 'media-left' }, [
            m('figure', { class: 'image is-48x48' }, [
              m('img', { class: '', src: poem.owner.icon_link }),
            ]),
          ]),
          m('div', { class: 'media-content' }, [
            m('p', { class: 'title is-4' }, poem.owner.displayname),
            m('p', { class: 'subtitle is-6' }, [
              m('a', { href: `/users/${poem.owner.username}` }, `@${poem.owner.username}`),
            ]),
          ]),
        ]),
        m('div', { class: 'content' }, [
          m('p', { class: 'is-size-3' }, poem.title),
          m('p', { class: '' }, poem.body),
          m('p', { class: '' }, poem.tags),
          m('p', { class: '' }, poem.date_created),
          m('br'),
          m('div', { class: 'columns' }, [
            m('div', { class: 'column' }, [
              m('p', { class: '' }, `Likes: ${poem.likes_count}`),
              m('p', { class: '' }, `Dislikes: ${poem.dislikes_count}`),
              m('p', { class: '' }, `Comments: ${poem.comments_count}`),
              m('p', { class: '' }, `Reviews: ${poem.reviews_count}`),
            ]),
          ]),
        ]),
      ])
    ];

    if (poem.image_link) {
      const cardImage = 
        m('div', { class: 'card-image' }, [
          m('figure', { class: 'image is-4by3' }, [
            m('img', { class: '', src: poem.image_link }),
          ]),
        ]);
      cardChildren.unshift(cardImage);
    }

    const component = {
      view: () => {
        return m('div', { class: 'card' }, cardChildren);
      }
    };
    return component;
  }
  
  function create_story_full_card (story) {
    const cardChildren = [
      m('div', { class: 'card-content' }, [
        m('div', { class: 'media' }, [
          m('div', { class: 'media-left' }, [
            m('figure', { class: 'image is-48x48' }, [
              m('img', { class: '', src: story.owner.icon_link }),
            ]),
          ]),
          m('div', { class: 'media-content' }, [
            m('p', { class: 'title is-4' }, story.owner.displayname),
            m('p', { class: 'subtitle is-6' }, [
              m('a', { href: `/users/${story.owner.username}` }, `@${story.owner.username}`),
            ]),
          ]),
        ]),
        m('div', { class: 'content' }, [
          m('p', { class: 'is-size-3' }, story.title),
          m('p', { class: '' }, story.body),
          m('p', { class: '' }, story.tags),
          m('p', { class: '' }, story.date_created),
          m('br'),
          m('div', { class: 'columns' }, [
            m('div', { class: 'column' }, [
              m('p', { class: '' }, `Likes: ${story.likes_count}`),
              m('p', { class: '' }, `Dislikes: ${story.dislikes_count}`),
              m('p', { class: '' }, `Comments: ${story.comments_count}`),
              m('p', { class: '' }, `Reviews: ${story.reviews_count}`),
            ]),
          ]),
        ]),
      ])
    ];

    if (story.image_link) {
      const cardImage = 
        m('div', { class: 'card-image' }, [
          m('figure', { class: 'image is-4by3' }, [
            m('img', { class: '', src: story.image_link }),
          ]),
        ]);
      cardChildren.unshift(cardImage);
    }

    const component = {
      view: () => {
        return m('div', { class: 'card' }, cardChildren);
      }
    };
    return component;
  }

  function create_user_card_compact (user) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
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
          ]),
        ]);
      }
    };
    return component;
  }

  function create_user_card_compact_list (users) {
    const list = users.map(user => create_user_card_compact(user).view());
    const component = {
      view: () => {
        return m('div', { class: 'user-cards-compact-container' }, [
          m('p', { class: 'title is-4 spacer-1 text-center' }, 'Users'),
          m('div', { class: 'user-cards-compact-list' }, list),
        ]);
      }
    };
    return component;
  }

  function create_poem_card_compact (poem) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
          m('div', { class: 'card-content' }, [
            m('div', { class: 'media' }, [
              m('div', { class: 'media-left' }, [
                m('figure', { class: 'image is-48x48' }, [
                  m('img', { class: '', src: poem.owner.icon_link }),
                ]),
              ]),
              m('div', { class: 'media-content' }, [
                m('p', { class: 'title is-4' }, poem.owner.displayname),
                m('p', { class: 'subtitle is-6' }, [
                  m('a', { href: `/users/${poem.owner.username}` }, `@${poem.owner.username}`),
                ]),
              ]),
            ]),
            m('div', { class: 'content' }, [
              m('p', { class: 'subtitle is-3' }, [
                m('a', { href: `/poems/${poem.id}` }, `${poem.title}...`),
              ]),
              m('p', { class: '' }, poem.date_created),
            ]),
          ]),
        ]);
      }
    };
    return component;
  }

  function create_poem_card_compact_list (poems) {
    const list = poems.map(poem => create_poem_card_compact(poem).view());
    const component = {
      view: () => {
        return m('div', { class: 'poem-cards-compact-container' }, [
          m('p', { class: 'title is-4 spacer-1 text-center' }, 'Poems'),
          m('div', { class: 'poem-cards-compact-list' }, list),
        ]);
      }
    };
    return component;
  }

  function create_story_card_compact (story) {
    const component = {
      view: () => {
        return m('div', { class: 'card' }, [
          m('div', { class: 'card-content' }, [
            m('div', { class: 'media' }, [
              m('div', { class: 'media-left' }, [
                m('figure', { class: 'image is-48x48' }, [
                  m('img', { class: '', src: story.owner.icon_link }),
                ]),
              ]),
              m('div', { class: 'media-content' }, [
                m('p', { class: 'title is-4' }, story.owner.displayname),
                m('p', { class: 'subtitle is-6' }, [
                  m('a', { href: `/users/${story.owner.username}` }, `@${story.owner.username}`),
                ]),
              ]),
            ]),
            m('div', { class: 'content' }, [
              m('p', { class: 'subtitle is-3' }, [
                m('a', { href: `/stories/${story.id}` }, `${story.title}...`),
              ]),
              m('p', { class: '' }, story.date_created),
            ]),
          ]),
        ]);
      }
    };
    return component;
  }

  function create_story_card_compact_list (stories) {
    const list = stories.map(story => create_story_card_compact(story).view());
    const component = {
      view: () => {
        return m('div', { class: 'story-cards-compact-container' }, [
          m('p', { class: 'title is-4 spacer-1 text-center' }, 'Stories'),
          m('div', { class: 'story-cards-compact-list' }, list),
        ]);
      }
    };
    return component;
  }

  // 

  return Object.freeze({
    create_user_card,
    create_user_profile_card,
    create_poem_full_card,
    create_story_full_card,
    create_user_card_compact,
    create_user_card_compact_list,
    create_poem_card_compact,
    create_poem_card_compact_list,
    create_story_card_compact,
    create_story_card_compact_list,
  });

})();
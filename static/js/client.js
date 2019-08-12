const Client = (function(){
  const send_request = function (route, method, data, content_type) {
    const obj = {
      method: method || "GET",
      credentials: 'include',
      headers: {
        "Accept": "application/json"
      }
    }
    if (method !== 'GET') {
      obj.credentials = 'include';
    }
    if(data) {
      if(data.constructor === Object) {
        obj.body = JSON.stringify(data);
        obj.headers["Content-Type"] = content_type || "application/json";
      }
      if(data.constructor === FormData) {
        obj.body = data;
      }
    }

    return fetch(route, obj).then((resp) => resp.json()).then(json => {
      // console.time('recursive date modify...');
      utils.formatAllDateProperties(json, 'date_created');
      // console.timeEnd('recursive date modify...');

      return json;
    });
  };

  const sign_in = function(data) {
    return send_request("/sign_in", "PUT", data, null);
  };

  const sign_up = function(data) {
    return send_request("/sign_up", "POST", data, null);
  };

  const get_user_by_username = function (username) {
    return send_request(`/get_user_by_username/${username}`, "GET", null, null).then(json => {
      return json;
    });
  };

  const get_user_by_id = function (id) {
    return send_request(`/get_user_by_id/${id}`, "GET", null, null).then(json => {
      return json;
    });
  };

  const get_user_profile_by_username = function (username) {
    return send_request(`/get_user_profile_by_username/${username}`, "GET", null, null).then(json => {
      return json;
    });
  };

  const get_user_profile_by_id = function (id) {
    return send_request(`/get_user_profile_by_id/${id}`, "GET", null, null).then(json => {
      return json;
    });
  };

  const check_session = function () {
    return send_request(`/check_session`, "GET", null, null).then(json => {
      return json;
    });
  };

  const update_account = function(data) {
    return send_request("/update_account", "PUT", data, null).then(json => {
      return json;
    });
  };

  const create_poem = function(data) {
    return send_request("/create_poem", "POST", data, null).then(json => {
      return json;
    });
  };

  const create_story = function(data) {
    return send_request("/create_story", "POST", data, null).then(json => {
      return json;
    });
  };

  const create_book = function(data) {
    return send_request("/create_book", "POST", data, null).then(json => {
      return json;
    });
  };

  const get_story_full_by_id = function(story_id) {
    return send_request(`/get_story_full_by_id/${story_id}`, "GET", null, null).then(json => {
      return json;
    });
  };

  // export
  return Object.freeze({
    send_request,
    sign_in,
    sign_up,
    check_session,
    get_user_by_username,
    get_user_by_id,
    get_user_profile_by_username,
    get_user_profile_by_id,
    update_account,
    create_poem,
    create_story,
    create_book,
    get_story_full_by_id,
  });
})();

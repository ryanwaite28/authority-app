const utils = (function() {
  const isObjectLiteral = function (obj) {
    if (typeof (obj) === 'object') {
      if (obj === null) {
        return false;
      }
      if (obj.constructor === Object) {
        return true;
      }
      return false;
    }
    return false;
  };

  const date_formatter = function (date) {
    // format --- December 23, 2017 - 10:40 PM
    // console.log(date);
    const date_created = moment(date).format('MMMM D, YYYY - h:mm A');
    return date_created;
  };

  const formatAllDateProperties = function (obj, dateProp) {
    if (isObjectLiteral(obj)) {
      const keys = Object.keys(obj);
      for (const key of keys) {
        if (typeof (obj[key]) === 'string') {
          if (key === dateProp) {
            obj[key] = date_formatter(obj[key]);
          }
        }
        if (typeof (obj[key]) === 'object') {
          formatAllDateProperties(obj[key], dateProp);
        }
      }
    } else if (Array.isArray(obj)) {
      for (const item of obj) {
        formatAllDateProperties(item, dateProp);
      }
    }
  };

  const flash_message = function(message, alertType, duration = 3) {
    duration = parseInt(String(duration + '000'), 10);
    message = message.trim();
    const id = (Math.random().toString(36).substr(2, 34) + Date.now());

    const el = window.document.createElement('div');
    el.innerHTML = `
    <div id="${id}" class="notification${alertType && ' ' + alertType || ''} ghost transition m-space-1">
      <p><strong>${message}</strong></p>
    </div>
    `;

    const messageBox = window.document.getElementById('message_box');
    messageBox.appendChild(el);
    const msgBox = window.document.getElementById(id);

    setTimeout(() => {
      msgBox.classList.remove('ghost');
      setTimeout(() => {
        msgBox.classList.add('ghost');
        setTimeout(() => {
          el.remove();
        }, 100);
      }, duration);
    }, 100);
  };

  const enable_buttons = function () {
    document.querySelectorAll('button').forEach(button => {
      button.removeAttribute('disabled');
    });
  };

  const disable_buttons = function () {
    document.querySelectorAll('button').forEach(button => {
      button.setAttribute('disabled', 'true');
    });
  };

  // export
  return Object.freeze({
    isObjectLiteral,
    date_formatter,
    formatAllDateProperties,
    flash_message,
    enable_buttons,
    disable_buttons,
  });
})();
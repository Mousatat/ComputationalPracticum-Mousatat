let page_parameters = {
    page_1: {
    parameters: [
        {id: 'x0_field', name: 'x0'},
        {id: 'X_field', name: 'X'},
        {id: 'y0_field', name: 'y0'},
        {id: 'steps_field', name: 'steps'}
    ],
    visibility_params: [
        {id: 'exact', name: 'Y exact'},
        {id: 'euler', name: 'Y Euler'},
        {id: 'improved', name: 'Y Improved Euler'},
        {id: 'runge_kutta', name: 'Y Runge Kutta'}
    ],
    onUpdate: function (page, params) { eel.onUpdatePage1(params); }
  },
  page_2: {
    parameters: [
        {id: 'x0_field', name: 'x0'},
        {id: 'X_field', name: 'X'},
        {id: 'y0_field', name: 'y0'},
        {id: 'steps_field', name: 'steps'},
    ],
    visibility_params: [
        {id: 'euler', name: 'Y Euler'},
        {id: 'improved', name: 'Y Improved Euler'},
        {id: 'runge_kutta', name: 'Y Runge Kutta'}
    ],
    onUpdate: function (page, params) { eel.onUpdatePage2(params); }
  },
  page_3: {
    parameters: [
        {id: 'n0_field', name: 'n0'},
        {id: 'N_field', name: 'N'},
    ],
    visibility_params: [
        {id: 'euler', name: 'Y Euler'},
        {id: 'improved', name: 'Y Improved Euler'},
        {id: 'runge_kutta', name: 'Y Runge Kutta'}
    ],
    onUpdate: function (page, params) { eel.onUpdatePage3(params); }
  }
};

let $tabs = function (target) {
  let
    _elemTabs = (typeof target === 'string' ? document.querySelector(target) : target),
    _showTab = function (tabsLinkTarget) {
      let tabsLinkActive = tabsLinkTarget.parentElement.querySelector('.tabs__link_active');
      if (tabsLinkTarget === tabsLinkActive) { return; }
      if (tabsLinkActive !== null) {
        tabsLinkActive.classList.remove('tabs__link_active');
      }
      tabsLinkTarget.classList.add('tabs__link_active');
      document.dispatchEvent(new CustomEvent('tab.show', { detail: _elemTabs }));
    };

  _elemTabs.addEventListener('click', function(e) {
    let target = e.target.closest('.tabs__link');
    if (!target) { return; }
    e.preventDefault();
    _showTab(target);

    let visibility_tab = document.getElementById('visibility_set'),
        field_tab = document.getElementById('field_set'),
        tab_num = target.id,
        page;
    if (tab_num === '1') {
        page = page_parameters.page_1;
    } else if (tab_num === '2') {
        page = page_parameters.page_2;
    } else if (tab_num === '3') {
        page = page_parameters.page_3;
    }
    let parent = visibility_tab.parentNode;
    visibility_tab.remove();
    field_tab.remove();
    visibility_tab = document.createElement('fieldset');
    field_tab = document.createElement('fieldset');
    visibility_tab.setAttribute('id', 'visibility_set');
    field_tab.setAttribute('id', 'field_set');
    parent.append(field_tab, visibility_tab);

    let legend = document.createElement('legend');
    legend.append('Parameters');
    field_tab.append(legend);
    legend = document.createElement('legend');
    legend.append('Visibility');
    visibility_tab.append(legend);

    for (let i = 0; i < page.visibility_params.length; i++) {
        // Visibility parameters
        let div = document.createElement('div'),
            input = document.createElement('input'),
            label = document.createElement('label');
        input.setAttribute('checked', 'checked');
        input.setAttribute('type', 'checkbox');
        input.setAttribute('name', 'interest');
        input.setAttribute('id', page.visibility_params[i].id);
        input.setAttribute('value', page.visibility_params[i].id);
        label.setAttribute('for', page.visibility_params[i].id);
        label.append(page.visibility_params[i].name);
        div.append(input, label);
        visibility_tab.append(div);
    }
    for (let i = 0; i < page.parameters.length; i++) {
      // Field parameters
      let div = document.createElement('div'),
          input = document.createElement('input'),
          label = document.createElement('label');
      input.setAttribute('type', 'number');
      input.setAttribute('placeholder', 'Enter ' + page.parameters[i].name + ':');
      input.setAttribute('class', 'fields_param');
      input.setAttribute('required', '');
      input.setAttribute('id', page.parameters[i].id);
      label.setAttribute('class', 'fields_label');
      label.setAttribute('for', page.parameters[i].id);
      label.append(page.parameters[i].name + ':');
      div.append(label, input);
      div.setAttribute('class', 'fields_param_div');
      field_tab.append(div);
    }
    page.onUpdate(tab_num);
  });
};

$tabs('.tabs');
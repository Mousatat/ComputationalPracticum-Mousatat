eel.expose(updateImage);
function updateImage() {
    console.log('Updated: ' + new Date().toLocaleString());
    let image = document.getElementById('graph');
    image.setAttribute('src', 'img/graph.png');
}

function btnUpdate() {
    let page_number = document.getElementsByClassName('tabs__link_active')[0].id,
        page,
        fields = {};
    if (page_number === '1')
        page = page_parameters.page_1;
    else if (page_number === '2')
        page = page_parameters.page_2;
    else if (page_number === '3')
        page = page_parameters.page_3;
    for (let i = 0; i < page.parameters.length; i++) {
        fields[page.parameters[i].id] = document.getElementById(page.parameters[i].id).value;
    }
    for (let i = 0; i < page.visibility_params.length; i++) {
        fields[page.visibility_params[i].id] = document.getElementById(page.visibility_params[i].id).checked;
    }
    page.onUpdate(page_number, fields);
}
async function add_card(name, quantity) {
}

async function add_price(name, price) {
}

async function load_card() {
    return await fetch("/get_card")
        .then(async function (response) {
            return await response.json();
        })
        .then(function (text) {
            return text["name"];
        });
}

async function load_history() {
    return await fetch("/get_history")
        .then(async function (response) {
            return await response.json();
        })
        .then(function (text) {
            return text["name"];
        });
}

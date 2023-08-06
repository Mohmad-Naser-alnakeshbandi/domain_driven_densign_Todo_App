console.log("it work!")

const xhr = new XMLHttpRequest();


function add_a_todo() {
    console.log("add an item")
    const todo_text_input = document.getElementById('todo_text_input').value;

    // Set up the AJAX request
    xhr.open('POST', '/todos', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Send the AJAX request with the JSON data
    xhr.send(JSON.stringify({
        "content": todo_text_input,
        "status": "Not started"
    }));

    document.getElementById("todo_form").submit()
}

function delete_a_todo(id) {
    console.log("delete an item")
    // Set up the AJAX request
    xhr.open('Delete', '/todos', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    // Send the AJAX request with the JSON data
    xhr.send(JSON.stringify({
        "id": id
    }));
        document.getElementById("todo_form").submit()

}


function change_todo_status(id) {
    console.log("change the status of an item")
    new_status = document.getElementById("todo_status").value
    // Set up the AJAX request
    xhr.open('PUT', '/todos/' + id, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    // Send the AJAX request with the JSON data
    xhr.send(JSON.stringify({
        "status": new_status
    }));
}
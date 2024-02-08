let users = JSON.parse(localStorage.getItem('users')) || [];

function signUp() {
    let username = document.getElementById('newUsername').value;
    let password = document.getElementById('newPassword').value;

    let user = {
        username: username,
        password: password
    };

    users.push(user);
    localStorage.setItem('users', JSON.stringify(users));
}

function signIn() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    let user = users.find(u => u.username === username && u.password === password);

    if (user) {
        alert('Successfully signed in!');
    } else {
        alert('Invalid username or password!');
    }
}
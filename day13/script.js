function random(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

document.getElementById('teleportButton').addEventListener('mouseover', function() {
    this.style.top = Math.random() * (window.innerHeight - this.offsetHeight) + 'px';
    this.style.left = Math.random() * (window.innerWidth - this.offsetWidth) + 'px';
    this.innerHTML=random(['I can teleport', 'Try again', 'I am here', 'I am there', 'I am everywhere', 'Keep trying',
        'all your efforts will be in vain', 'you can\'t beat a computer', 'I am the best', 'your reactions are too slow',
        'you are an idiot', 'I am too quick', 'slowpoke', 'you suck', 'you are a loser', 'you are a failure', 'you are a fool',
        'you are a moron', 'you are useless', 'you are a waste of space', 'you are a waste of time', 'you are a waste of life'])
});
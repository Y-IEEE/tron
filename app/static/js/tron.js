const WIDTH = 64,
      HEIGHT = 32;

const canvas = document.getElementById('tron');
canvas.height = window.innerHeight;
canvas.width  = window.innerWidth;
const ctx = canvas.getContext('2d');

fetch('/api/board')
.then((response) => {
    return response.json();
})
.then((colors) {
    console.log(colors);
});

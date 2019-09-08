const WIDTH = 64,
      HEIGHT = 32,
      PIXEL_SIZE = 10;

const canvas = document.getElementById('tron');
canvas.height = PIXEL_SIZE * HEIGHT;
canvas.width  = PIXEL_SIZE * WIDTH;
const ctx = canvas.getContext('2d');

fetch('/api/board')
.then((response) => {
    return response.json();
})
.then((colors) => {
    for (let row = 0; row < colors.length; row++) {
        for (let col = 0; col < colors[row].length; col++) {
            ctx.fillStyle = '#' + colors[row][col];
            ctx.fillRect(PIXEL_SIZE * row, PIXEL_SIZE * col, PIXEL_SIZE, PIXEL_SIZE);
        }
    }
});

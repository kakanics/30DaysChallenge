const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
app.use(cors()); // Enable CORS

const server = http.createServer(app);
const io = socketIo(server, {
    cors: {
        origin: "*", // Allow all origins
        methods: ["GET", "POST"]
    }
});

io.on('connection', (socket) => {
        console.log('New client connected');

        socket.on('message', (message) => {
                console.log('Message Received: ' + message);
                io.emit('message', 'Hello, this is the chatbot responding to your message: ' + message);
        });

        socket.on('disconnect', () => {
                console.log('Client disconnected');
        });
});

server.listen(4000, () => console.log('Listening on port 4000'));
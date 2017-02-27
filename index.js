const express           = require('express')
const http              = require('http')
const config            = require('config')
const path              = require('path')
const io                = require('socket.io')
const os                = require('os')
const _                 = require('lodash')

const log               = require('./lib/log')

const app    = express()
const server = http.Server(app)
const sio    = io(server)

var port = config.server.port || 3000
var host = config.server.host || 'localhost'

// setting all the static path
app.use(express.static('./public'))
app.use('/vendor/bootstrap',          express.static(path.join(__dirname, 'node_modules/bootstrap/dist')))
app.use('/vendor/jquery',             express.static(path.join(__dirname, 'node_modules/jquery/dist')))
app.use('/vendor/babel',              express.static(path.join(__dirname, 'node_modules/babel-standalone')))
app.use('/vendor/react',              express.static(path.join(__dirname, 'node_modules/react/dist')))
app.use('/vendor/react-dom',          express.static(path.join(__dirname, 'node_modules/react-dom/dist')))
app.use('/vendor/socket.io-client',   express.static(path.join(__dirname, 'node_modules/socket.io-client/dist')))
app.use('/vendor/lodash',             express.static(path.join(__dirname, 'node_modules/lodash')))

// set up the main route
app.get('/', (req, res) => {
	res.sendFile(path.join(__dirname, 'views/index.html'))
})

//Get the correct network interface to listen on:
var networkifs = os.networkInterfaces();
//log.info('Network Ifs',networkifs);

if (networkifs.eth0){
	//log.info('Using ', networkifs.eth0[0].address);
	host = networkifs.eth0[0].address;
}

// start the webserver
server.listen(port, host, () => {
	log.info(`Listening on http://${host}:${port}. Party time!`)
})

// listen for incoming websockets
var sockets = []
sio.on('connection', (socket) => {
	log.info('A new client connected')

	sockets.push(socket)

	socket.on('disconect', () => {
		// remove socket from sockets
		sockets.splice(sockets.indexOf(socket), 1)
	})

	// send the state to front-end
	socket.emit('state', "Hoi")

	// setInterval(() => {
	// 	socket.emit('state', "Hoi")
	// }, 1000)

})
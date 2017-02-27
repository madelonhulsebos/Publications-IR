const _       = require('lodash')
const winston = require('winston')

let level = 'info'
if (_.includes(['true', '1'], process.env.DEBUG)) {
	level = 'debug'
} 

const log = new winston.Logger({
	transports: [
		new winston.transports.Console({ colorize: true, level: level })
	]
})

module.exports = log
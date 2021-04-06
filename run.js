// Start my Discord on NodeJS xD 
const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'unk.ping') {
    msg.reply('Pong!');
  }
  if (msg.content === 'unk.help') {
      msg.reply('Help');
  }
});

client.login('token');
#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // get api from cmd line arg

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // print error if request fails
  } else {
    const todos = JSON.parse(body);
    const tasksDoneByUser = todos.reduce((acc, todo) => {
      if (todo.completed) {
        if (acc[todo.userId]) {
          acc[todo.userId]++;
        } else {
          acc[todo.userId] = 1;
        }
      }
      return acc;
    }, {});

    console.log(tasksDoneByUser);
    }
});

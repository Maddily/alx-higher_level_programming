#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const completedTasks = {};

// Compute  the number of tasks completed by user id.
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (userId in completedTasks) {
        completedTasks[userId]++;
      } else {
        completedTasks[userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});

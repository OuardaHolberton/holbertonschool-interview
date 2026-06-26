#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  function printCharacters(index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);

      printCharacters(index + 1);
    });
  }

  printCharacters(0);
});

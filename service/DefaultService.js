'use strict';


/**
 * Sample endpoint: Returns the shit summary for a particular player
 *
 * summonerName String ID of the user
 * region String Region of the player
 * returns Player
 **/
exports.getPlayer = function(summonerName,region) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "name",
  "games" : [ {
    "kills" : 0,
    "assists" : 0,
    "stats" : [ {
      "secondary" : "secondary",
      "primary" : "primary"
    }, {
      "secondary" : "secondary",
      "primary" : "primary"
    } ],
    "deaths" : 0,
    "champion" : {
      "name" : "name",
      "backspashUrl" : "http://example.com/aeiou"
    }
  }, {
    "kills" : 0,
    "assists" : 0,
    "stats" : [ {
      "secondary" : "secondary",
      "primary" : "primary"
    }, {
      "secondary" : "secondary",
      "primary" : "primary"
    } ],
    "deaths" : 0,
    "champion" : {
      "name" : "name",
      "backspashUrl" : "http://example.com/aeiou"
    }
  } ],
  "region" : "region"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


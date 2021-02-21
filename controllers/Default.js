'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.getPlayer = function getPlayer (req, res, next, summonerName, region) {
  Default.getPlayer(summonerName, region)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

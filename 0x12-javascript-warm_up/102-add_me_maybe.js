#!/usr/bin/node
/**
 * This module exports function called function that calls function
 * so you can call function while calling function (and incremcnting)
 *
 * Prototype: function (x, theFunction)
 * @NB: You are not allowed to use var
 */
exports.addMeMaybe = function (n, theFunction) {
  if (typeof theFunction === 'function') {
    theFunction.call(this, n + 1);
  }
};

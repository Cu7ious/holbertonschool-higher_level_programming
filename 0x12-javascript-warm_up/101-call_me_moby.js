#!/usr/bin/node
/**
 * This module exports function called function that calls function
 * so you can call function while calling function
 *
 * Prototype: function (x, theFunction)
 * @NB: You are not allowed to use var
 */
module.exports = {
  callMeMoby: function (x, theFunction) {
    while (x) {
      if (typeof theFunction === 'function') {
        theFunction.call();
        --x;
      }
    }
  }
};

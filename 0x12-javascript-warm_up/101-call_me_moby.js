#!/usr/bin/node
/**
 * This module exports function called function that calls function
 * so you can call function while calling function
 *
 * Prototype: function (x, theFunction)
 * @NB: You are not allowed to use var
 */
exports.callMeMoby = function (x, theFunction) {
  if (isNaN(Number(x))) {
    return NaN;
  }

  while (x > 0) {
    if (typeof theFunction === 'function') {
      theFunction.call();
      --x;
    } else {
      return;
    }
  }
};

#!/usr/bin/node

/**
 * Rectangle - creates object of type Rectangle
 * @width: rectangle width
 * @height: rectangle height
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

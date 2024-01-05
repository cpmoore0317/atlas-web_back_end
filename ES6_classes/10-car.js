// cpmoore0317

const brandSymbol = Symbol("brand");
const motorSymbol = Symbol("motor");
const colorSymbol = Symbol("color");

export default class Car {
  constructor(brand, motor, color) {
    this[brandSymbol] = brand;
    this[motorSymbol] = motor;
    this[colorSymbol] = color;
  }

  get brand() {
    return this[brandSymbol];
  }

  get motor() {
    return this[motorSymbol];
  }

  get color() {
    return this[colorSymbol];
  }

  cloneCar() {
    const { brand, motor, color } = this;
    return new this.constructor(brand, motor, color);
  }
}

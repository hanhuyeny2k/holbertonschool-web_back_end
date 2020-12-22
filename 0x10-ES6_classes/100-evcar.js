import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const car = super.cloneCar();
    car._range = this._range;
    Object.setPrototypeOf(car, new Car());
    return car;
  }
}

// cpmoore0317
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateName(name);
    this._length = this.validateLength(length);
    this._students = this.validateStudents(students);
  }

  // Getter for name
  get name() {
    return this._name;
  }

  // Setter for name with validation
  set name(newName) {
    this._name = this.validateName(newName);
  }

  // Getter for length
  get length() {
    return this._length;
  }

  // Setter for length with validation
  set length(newLength) {
    this._length = this.validateLength(newLength);
  }

  // Getter for students
  get students() {
    return this._students;
  }

  // Setter for students with validation
  set students(newStudents) {
    this._students = this.validateStudents(newStudents);
  }

  // Validation function for name attribute
  validateName(value) {
    if (typeof value === "string") {
      return value;
    } else {
      throw new TypeError("Name must be a string");
    }
  }

  // Validation function for length attribute
  validateLength(value) {
    if (typeof value === "number") {
      return value;
    } else {
      throw new TypeError("Length must be a number");
    }
  }

  // Validation function for students attribute
  validateStudents(value) {
    if (
      Array.isArray(value) &&
      value.every((item) => typeof item === "string")
    ) {
      return value;
    } else {
      throw new TypeError("Students must be an array of strings");
    }
  }
}

// 4-user-promise.js

export default function signUpUser(firstName, lastName) {
  return Promise.resolve({
    // eslint-disable-next-line object-shorthand
    firstName: firstName,
    // eslint-disable-next-line object-shorthand
    lastName: lastName,
  });
}

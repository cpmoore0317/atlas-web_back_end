// cpmoore0317

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => {
    return results.map((result) => ({
      status: result.status, // Status of the promise ('fulfilled' or 'rejected')
      value: result.value, // Value or error returned by the promise
    }));
  });
}

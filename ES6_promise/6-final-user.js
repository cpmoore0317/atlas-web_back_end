// 6-final-user.js

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName,
  lastName,
  fileName,
) {
  try {
    const results = await Promise.allSettled([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ]);

    return results.map((result) => ({
      status: result.status === 'fulfilled' ? 'fulfilled' : 'rejected',
      value:
        result.status === 'fulfilled' ? result.value : result.reason.toString(),
    }));
  } catch (error) {
    return [
      {
        status: 'rejected',
        value: error.toString(),
      },
    ];
  }
}

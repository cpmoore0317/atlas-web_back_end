// 0-promise.js

export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;

      if (success) {
        resolve('Api response data');
      } else {
        reject(new Error('Error fetching data from API'));
      }
    }, 1000);
  });
}

// cpmoore0317

export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (succes) {
      resolve({ status: 200, body: 'Success' });
      console.log('Got a response from the API');
    } else {
      reject(new Error());
      console.log('Got a response from the API');
    }
  });
}

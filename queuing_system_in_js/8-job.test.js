import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a new Kue queue for each test
    queue = kue.createQueue();
    
    // Enter test mode to prevent processing jobs automatically
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    // Create a non-array job
    const job = { phoneNumber: '4153518780', message: 'Test message' };

    // Expect an error to be thrown
    expect(() => createPushNotificationsJobs(job, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    // Define an array of jobs
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Check the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Iterate over each job in the queue
    queue.testMode.jobs.forEach((job, index) => {
      // Check job data matches the expected input
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(jobs[index]);
    });
  });

  // Add more tests as needed for other scenarios

});

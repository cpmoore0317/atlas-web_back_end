// 8-api/api.test.js

const request = require('request');
const { expect } = require('chai');
const app = require('./api');

describe('Index page', () => {
    let server;
    before((done) => {
        server = app.listen(7865, done);
    });

    after((done) => {
        server.close(done);
    });

    it('should return status code 200', (done) => {
        request.get('http://localhost:7865', (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return the correct message', (done) => {
        request.get('http://localhost:7865', (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});

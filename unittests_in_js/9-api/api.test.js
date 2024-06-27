// 9-api/api.test.js

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

describe('Cart page', () => {
    let server;
    before((done) => {
        server = app.listen(7865, done);
    });

    after((done) => {
        server.close(done);
    });

    it('should return status code 200 when :id is a number', (done) => {
        request.get('http://localhost:7865/cart/12', (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('should return status code 404 when :id is not a number', (done) => {
        request.get('http://localhost:7865/cart/hello', (error, response, body) => {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});

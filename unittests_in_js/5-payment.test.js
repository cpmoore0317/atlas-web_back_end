// 5-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
    let spy;

    beforeEach(() => {
        spy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        spy.restore();
    });

    it('should log the correct message and be called once for 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });

    it('should log the correct message and be called once for 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);
        expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
        expect(spy.calledOnce).to.be.true;
    });
});

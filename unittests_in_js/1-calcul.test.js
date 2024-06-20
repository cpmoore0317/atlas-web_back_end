// 1-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should add rounded numbers when type is SUM', function() {
            assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
            assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
            assert.strictEqual(calculateNumber('SUM', 1.2, 3), 4);
            assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
            assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
        });
    });
    describe('SUBTRACT', () => {
        it('should subtract rounded numbers when type is SUBTRACT', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
        });
    });
    describe('DIVIDE', () => {
        it('should divide rounded numbers when type is DIVIDE', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.324);
            assert.strictEqual(calculateNumber('DIVIDE', 1.5, 0), 'Error');
        });
    });
});
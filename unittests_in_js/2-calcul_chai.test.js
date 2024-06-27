// 2-calcul_chai.test.js

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should add rounded numbers when type is SUM', function() {
            expect(calculateNumber('SUM', 1, 3)).to.equal(4);
            expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
            expect(calculateNumber('SUM', 1.2, 3)).to.equal(4);
            expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
            expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
        });
    });
    describe('SUBTRACT', () => {
        it('should subtract rounded numbers when type is SUBTRACT', function() {
            expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
        });
    });
    describe('DIVIDE', () => {
        it('should divide rounded numbers when type is DIVIDE', function() {
            expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.be.closeTo(0.324, 0.001);
            expect(calculateNumber('DIVIDE', 1.5, 0)).to.equal('Error');
        });
    });
});

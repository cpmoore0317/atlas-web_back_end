const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return rounded sum for SUM', function() {
      expect(calculateNumber('SUM', 6.2, 11.8)).to.equal(18);
    });
  });
  describe('SUBTRACT', function() {
    it('should return rounded difference for SUBTRACT', function() {
      expect(calculateNumber('SUBTRACT', 15.8, 6.2)).to.equal(10);
    });
  });
  describe('DIVIDE', function() {
    it('should return rounded division for DIVIDE', function() {
      expect(calculateNumber('DIVIDE', 9.3, 2.7)).to.equal(3);
    });
    it('should return Error for DIVIDE when b is 0', function() {
      expect(calculateNumber('DIVIDE', 56.9, 0)).to.equal('Error');
    });
  });
});

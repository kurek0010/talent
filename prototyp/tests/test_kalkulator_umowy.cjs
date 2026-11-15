const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const {parseAmount, calculate, loanInstallments, invoice, loan} = require('../src/kalkulator_umowy.js');

const html = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf8');
const data = /<script type="application\/json" id="contract-rates">([^<]+)<\/script>/.exec(html);
const rates = JSON.parse(data[1]);

function amounts(input) {
  const {nominal, cpi, talent} = calculate(
    rates, parseAmount(input.amount), input.start, input.end
  );
  return {nominal, cpi, talent};
}

test('faktura roczna jest waloryzowana według miesięcznych odczytów', () => {
  assert.deepEqual(amounts(invoice), {nominal: 10000000n, cpi: 11681492n, talent: 11427561n});
});

test('pożyczka odróżnia płatność jednorazową od sumy czterech rat', () => {
  assert.deepEqual(amounts(loan), {nominal: 1000000n, cpi: 996999n, talent: 1003200n});
  assert.deepEqual(loanInstallments(rates), {nominal: 1000000n, cpi: 997000n, talent: 1002612n});
});

test('daty z tego samego miesiąca dają te same odczyty i kwotę', () => {
  assert.deepEqual(amounts({amount: '1 234,56', start: '2022-02-01', end: '2022-02-28'}),
    {nominal: 123456n, cpi: 123456n, talent: 123456n});
});

test('kalkulator odrzuca brak odczytu i nieprawidłowe daty', () => {
  const newest = new Date(Object.keys(rates).sort().at(-1) + '-01');
  newest.setUTCMonth(newest.getUTCMonth() + 1);
  const nextMonth = newest.toISOString().slice(0, 10);
  assert.throws(() => calculate(rates, 10000n, '1995-12-31', nextMonth),
    {message: `Brak odczytu miesięcznego za 1995-12 i ${nextMonth.slice(0, 7)}.`});
  assert.throws(() => calculate(rates, 10000n, '2022-02-01', '2022-02-29'), /pełne daty/);
  assert.throws(() => calculate(rates, 10000n, '2022-01-02', '2022-01-01'), /poprzedzać/);
  const gap = Object.assign({}, rates);
  delete gap['2022-06'];
  assert.throws(() => calculate(gap, 10000n, '2022-05-30', '2022-06-01'), /2022-06/);
});

test('ułamek grosza jest zaokrąglany jednokrotnie, połówki w górę', () => {
  const example = {'2024-01': [8, 8], '2024-02': [10, 6]};
  const result = calculate(example, parseAmount('0,02'), '2024-01-01', '2024-02-01');
  assert.equal(result.cpi, 3n);
  assert.equal(result.talent, 2n);
  assert.equal(parseAmount('9 007 199 254 740 993,01'), 900719925474099301n);
});

test('przyjmuje polski i kropkowy zapis kwot oraz odrzuca błędne formaty', () => {
  assert.equal(parseAmount('1\u202f042,50'), 104250n);
  assert.equal(parseAmount('1042.5'), 104250n);
  for (const text of ['0', '-1', '12 34,00', '100.001', '1e3', '']) {
    assert.throws(() => parseAmount(text));
  }
});

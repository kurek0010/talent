// Osobna sekcja strony, działająca również bez wykresu i jego biblioteki.
(() => {
  const invoice = {amount: '100000', start: '2021-12-31', end: '2022-12-31'};
  const loan = {amount: '10000', start: '2026-05-31', end: '2026-09-30'};
  const loanPaymentDates = ['2026-06-30', '2026-07-31', '2026-08-31', loan.end];

  function parseAmount(value) {
    const parts = value.trim().match(/^(\d+|\d{1,3}(?:[ \u00a0\u202f]\d{3})+)(?:[,.](\d{1,2}))?$/);
    if (!parts) throw new Error('Wpisz kwotę w PLN, np. 10 000,00.');
    const units = BigInt(parts[1].replace(/\D/g, ''));
    const amount = units * 100n + BigInt((parts[2] || '').padEnd(2, '0'));
    if (amount === 0n) throw new Error('Kwota początkowa musi być większa od zera.');
    return amount;
  }

  function isDate(value) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
    const parsed = new Date(value);
    return !Number.isNaN(parsed.getTime()) && parsed.toISOString().slice(0, 10) === value;
  }

  // Dokładna arytmetyka w groszach, jeden raz na każdą płatność.
  function indexedAmount(amount, from, to) {
    const numerator = amount * BigInt(to);
    const denominator = BigInt(from);
    return (2n * numerator + denominator) / (2n * denominator);
  }

  function calculate(rates, amount, start, end) {
    if (!isDate(start) || !isDate(end)) throw new Error('Podaj obie pełne daty.');
    if (start > end) throw new Error('Data rozliczenia nie może poprzedzać daty początkowej.');

    const startMonth = start.slice(0, 7);
    const endMonth = end.slice(0, 7);
    const from = rates[startMonth];
    const to = rates[endMonth];
    if (!from || !to) {
      const missing = [...new Set([startMonth, endMonth].filter(month => !rates[month]))];
      throw new Error(`Brak odczytu miesięcznego za ${missing.join(' i ')}.`);
    }

    return {
      nominal: amount,
      cpi: indexedAmount(amount, from[0], to[0]),
      talent: indexedAmount(amount, from[1], to[1]),
      from,
      to,
      startMonth,
      endMonth,
    };
  }

  function loanInstallments(rates) {
    return loanPaymentDates.reduce((sum, date) => {
      const row = calculate(rates, 250000n, loan.start, date);
      return {
        nominal: sum.nominal + row.nominal,
        cpi: sum.cpi + row.cpi,
        talent: sum.talent + row.talent,
      };
    }, {nominal: 0n, cpi: 0n, talent: 0n});
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {parseAmount, calculate, loanInstallments, invoice, loan};
    return;
  }

  const form = document.getElementById('contract-form');
  const rates = JSON.parse(document.getElementById('contract-rates').textContent);
  const fields = form.elements;
  const status = document.getElementById('contract-status');
  const result = document.getElementById('contract-result');
  const loanNote = document.getElementById('contract-loan-note');
  const currency = new Intl.NumberFormat('pl-PL', {
    style: 'currency', currency: 'PLN', useGrouping: 'always',
  });
  const index = new Intl.NumberFormat('pl-PL', {minimumFractionDigits: 3, maximumFractionDigits: 3});

  function formatPLN(cents) {
    const fraction = String(cents % 100n).padStart(2, '0');
    return currency.formatToParts(cents / 100n).map(
      part => part.type === 'fraction' ? fraction : part.value
    ).join('');
  }

  function render() {
    result.hidden = true;
    loanNote.hidden = true;
    let row;
    const start = fields.start.value;
    const end = fields.end.value;
    try {
      row = calculate(rates, parseAmount(fields.amount.value), start, end);
    } catch (error) {
      status.textContent = error.message;
      return;
    }

    for (const method of ['nominal', 'cpi', 'talent']) {
      document.getElementById(`contract-${method}`).textContent = formatPLN(row[method]);
    }
    for (const [position, method] of ['cpi', 'talent'].entries()) {
      document.getElementById(`contract-${method}-readings`).textContent =
        `${index.format(row.from[position] / 1000)} → ${index.format(row.to[position] / 1000)} pkt`;
    }
    status.textContent = `Odczyty za ${row.startMonth} i ${row.endMonth}.`;
    result.hidden = false;

    if (row.nominal === 1000000n && start === loan.start && end === loan.end
        && loanPaymentDates.every(date => rates[date.slice(0, 7)])) {
      const installments = loanInstallments(rates);
      loanNote.textContent = 'Suma czterech rat od czerwca do września 2026 r., po 2 500 zł przed waloryzacją.'
        + ` Nominał ${formatPLN(installments.nominal)}, CPI ${formatPLN(installments.cpi)},`
        + ` Talent ${formatPLN(installments.talent)}.`;
      loanNote.hidden = false;
    }
  }

  form.addEventListener('submit', event => {
    event.preventDefault();
    render();
  });
  form.addEventListener('input', () => {
    status.textContent = '';
    result.hidden = true;
  });

  for (const button of form.querySelectorAll('[data-contract-example]')) {
    button.addEventListener('click', () => {
      const example = button.dataset.contractExample === 'invoice' ? invoice : loan;
      fields.amount.value = example.amount;
      fields.start.value = example.start;
      fields.end.value = example.end;
      render();
    });
  }
})();

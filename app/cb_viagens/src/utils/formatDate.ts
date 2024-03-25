const days: Record<number, string> = {
  0: 'Dom',
  1: 'Seg',
  2: 'Ter',
  3: 'Qua',
  4: 'Qui',
  5: 'Sex',
  6: 'Sab'
}

const months: Record<number, string> = {
  0: 'Janeiro',
  1: 'Fevereiro',
  2: 'Março',
  3: 'Abril',
  4: 'Maio',
  5: 'Junho',
  6: 'Julho',
  7: 'Agosto',
  8: 'Setembro',
  9: 'Outubro',
  10: 'Novembro',
  11: 'Dezembro'
}

export function formatDate(date: Date) {
  const day = days[date.getDay()]
  const dateNum = date.getDate()
  const month = months[date.getMonth()]

  return `${day}, ${dateNum} de ${month.substring(0, 3)}`
}

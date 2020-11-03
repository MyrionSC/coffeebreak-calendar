$(document).ready(() => {
    const todayISO = new Date(Date.now()).toISOString().split('T')[0]
    const currentDayContainer = $(`.day-container[data-date-iso='${todayISO}']`)
    currentDayContainer.addClass('active')
})
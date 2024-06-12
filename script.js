// script.js
document.addEventListener("DOMContentLoaded", function () {
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    const prevButton = document.getElementById("prev");
    const nextButton = document.getElementById("next");

    let currentDate = new Date();

    function renderCalendar(date) {
        const year = date.getFullYear();
        const month = date.getMonth();
        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const lastDateOfMonth = new Date(year, month + 1, 0).getDate();
        const lastDateOfPrevMonth = new Date(year, month, 0).getDate();

        const monthNames = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ];

        monthYear.innerText = `${monthNames[month]} ${year}`;

        calendarDays.innerHTML = "";

        // Previous month
        for (let i = firstDayOfMonth; i > 0; i--) {
            calendarDays.innerHTML += `<div class="empty">${lastDateOfPrevMonth - i + 1}</div>`;
        }

        // Current month
        for (let i = 1; i <= lastDateOfMonth; i++) {
            calendarDays.innerHTML += `<div>${i}</div>`;
        }

        // Next month
        const totalDays = firstDayOfMonth + lastDateOfMonth;
        const remainingDays = 42 - totalDays;
        // 42 is the days in 6 weeks (6*7), so we always display 6 weeks.
        // This way our calendar remains the same size and format, to it wont fuck up the rest of the html
        for (let i = 1; i <= remainingDays; i++) {
            calendarDays.innerHTML += `<div class="empty">${i}</div>`;
        }
    }

    prevButton.addEventListener("click", function () {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextButton.addEventListener("click", function () {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    renderCalendar(currentDate);
});

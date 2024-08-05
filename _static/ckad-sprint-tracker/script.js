document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.day-button');

    const boostMessages = [
        "Awesome!",
        "Great job!",
        "Keep it up!",
        "You're doing amazing!",
        "Fantastic!",
        "You're on fire!",
        "Keep pushing forward!",
        "Nice work!",
        "You're unstoppable!",
        "Excellent!",
        "Way to go!",
        "You're crushing it!",
        "Keep the momentum!",
        "You're a star!",
        "Amazing progress!"
    ];

    function saveProgress() {
        const progress = {};
        buttons.forEach(button => {
            const day = button.getAttribute('data-day');
            const completed = button.classList.contains('completed');
            progress[day] = completed ? button.textContent : '';
        });
        localStorage.setItem('sprintProgress', JSON.stringify(progress));
    }

    function loadProgress() {
        const savedProgress = JSON.parse(localStorage.getItem('sprintProgress'));
        if (savedProgress) {
            buttons.forEach(button => {
                const day = button.getAttribute('data-day');
                if (savedProgress[day]) {
                    button.classList.add('completed');
                    button.textContent = savedProgress[day];
                }
            });
        }
    }

    loadProgress();

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.toggle('completed');

            if (this.classList.contains('completed')) {
                if (this.getAttribute('data-day') == '15') {
                    this.textContent = 'Good luck on the exam!';
                    confetti({
                        particleCount: 200,
                        spread: 60,
                        origin: { y: 0.6 }
                    });
                } else {
                    const randomMessage = boostMessages[Math.floor(Math.random() * boostMessages.length)];
                    this.textContent = randomMessage;
                }
            } else {
                const dayNumber = this.getAttribute('data-day');
                this.textContent = 'Day ' + dayNumber;
            }

            saveProgress();
        });
    });
});

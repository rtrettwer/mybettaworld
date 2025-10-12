// Interaktive Features für den Betta-Blog
document.addEventListener('DOMContentLoaded', function() {

    // Sales Gallery Filter - Verbesserte Version
    const filterBtns = document.querySelectorAll('.filter-btn');
    const fishCards = document.querySelectorAll('.fish-card');

    // Initial: alle Karten sichtbar machen
    fishCards.forEach(card => {
        card.style.display = 'block';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
    });

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Aktive Klasse umschalten
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filter = this.dataset.filter;
            console.log('Filter clicked:', filter); // Debug

            fishCards.forEach(card => {
                const cardCategory = card.dataset.category;
                console.log('Card category:', cardCategory, 'Filter:', filter); // Debug

                if (filter === 'all' || cardCategory === filter) {
                    // Karte anzeigen
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    // Karte verstecken
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Interest Button Handler
    const interestBtns = document.querySelectorAll('.interest-btn');
    interestBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            if (!this.disabled) {
                const fishCard = this.closest('.fish-card');
                const fishName = fishCard.querySelector('h4').textContent;

                // Hier kannst du später ein Kontaktformular oder E-Mail-Link einfügen
                alert(`Interesse an "${fishName}" angemeldet! Ich werde mich bei dir melden.`);

                // Optional: Button temporär deaktivieren
                this.textContent = 'Interesse gemeldet ✓';
                this.style.background = '#4caf50';

                setTimeout(() => {
                    this.textContent = 'Interesse anmelden';
                    this.style.background = '';
                }, 3000);
            }
        });
    });

    // Smooth scrolling für interne Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.tank-card, .fish-card, .parameter-card, .stat-widget').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    console.log('🐠 Betta-Blog interaktive Features geladen!');
});

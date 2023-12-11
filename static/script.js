
    function createStar() {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + 'vw';
        star.style.animationDuration = Math.random() * 3 + 2 + 's';
        document.body.appendChild(star);

        setTimeout(() => {
            star.remove();
        }, 5000);
    }

    function createLightning() {
        const lightning = document.createElement('div');
        lightning.className = 'lightning';
        lightning.style.left = Math.random() * 100 + 'vw';
        lightning.style.animationDuration = '0.2s';
        document.body.appendChild(lightning);

        setTimeout(() => {
            lightning.remove();
        }, 200);
    }

    setInterval(createStar, 150);
    setInterval(createLightning, 4000);

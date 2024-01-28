var canvas = document.getElementById("canvas");
      var ctx = canvas.getContext("2d");

      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      var particles = [];
      var mouse = { x: 0, y: 0 };

      function Particle() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 5 + 1;
        this.speedX = Math.random() * 3 - 1.5;
        this.speedY = Math.random() * 3 - 1.5;
        this.maxSize = this.size;
        this.life = 0;
        this.maxLife = Math.random() * 500 + 400; // lifespan of 5 to 9.67 seconds
      }

      Particle.prototype.update = function () {
        this.x += this.speedX;
        this.y += this.speedY;
        var speedLimit = 0.5;
        if (Math.abs(this.speedX) > speedLimit) {
          this.speedX = this.speedX > 0 ? speedLimit : -speedLimit;
        }
        if (Math.abs(this.speedY) > speedLimit) {
          this.speedY = this.speedY > 0 ? speedLimit : -speedLimit;
        }
        this.life++;

        // reduce size over time
        if (this.life < this.maxLife) {
          this.size = this.maxSize * (1 - this.life / this.maxLife);
          if (this.size < 4) this.size = 4;
        } else {
          this.size = 0;
        }
      };

      Particle.prototype.draw = function () {
        ctx.fillStyle = "rgba(173, 216, 230, 1)";
        ctx.strokeStyle = "rgba(173, 216, 230, 0.8)";

        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.closePath();
        ctx.fill();
      };

      function createParticle() {
        particles.push(new Particle());
      }

      function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (var i = 0; i < particles.length; i++) {
          var dx = particles[i].x - mouse.x;
          var dy = particles[i].y - mouse.y;
          var dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 50) {
            var forceDirectionX = dx / dist;
            var forceDirectionY = dy / dist;

            var maxForce = 5; // Increase this value to increase the force

            particles[i].speedX += forceDirectionX * maxForce;
            particles[i].speedY += forceDirectionY * maxForce;

            if (particles[i].speedX > maxForce) particles[i].speedX = maxForce;
            if (particles[i].speedX < -maxForce)
              particles[i].speedX = -maxForce;
            if (particles[i].speedY > maxForce) particles[i].speedY = maxForce;
            if (particles[i].speedY < -maxForce)
              particles[i].speedY = -maxForce;
          }
          particles[i].update();
          particles[i].draw();

          if (particles[i].size <= 0.2) {
            particles.splice(i, 1);
            i--;
          }
        }
        for (var i = 0; i < particles.length; i++) {
          for (var j = i + 1; j < particles.length; j++) {
            var dx = particles[i].x - particles[j].x;
            var dy = particles[i].y - particles[j].y;
            var dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < 100) {
              ctx.beginPath();
              ctx.moveTo(particles[i].x, particles[i].y);
              ctx.lineTo(particles[j].x, particles[j].y);
              ctx.strokeStyle = "rgba(173, 216, 230, 0.5)";
              ctx.stroke();
            }
          }
        }

        if (Math.random() < 0.15) {
          // 15% chance to spawn a particle each frame
          createParticle();
        }

        requestAnimationFrame(animateParticles);
      }

      for (var i = 0; i < 50; i++) {
        createParticle();
      }

      canvas.addEventListener("mousemove", function (e) {
        mouse.x = e.x;
        mouse.y = e.y;
      });

      animateParticles();
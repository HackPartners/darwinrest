$(document).ready(function(){

// particles js

// calculate a ratio to be used in particle count, distance to 
// connect, etc. 
var ratio = Math.sqrt($(window).width() * $(window).height()) / 1120.0;
loadParticles(ratio);

});

function scrollTo(selector) {
  $("html, body").animate({
    scrollTop: $(selector).offset().top
  }, 500);
}

function loadParticles(ratio) {
  // number of particles
  var MAX_PARTICLES = 150;
  // distances needed to form a line
  var MAX_DISTANCE = 100;
  var MAX_MOUSE_DISTANCE = 300;
  // size of particles
  var MAX_SIZE = 3;
  // speed
  var MAX_SPEED = 3;

  particlesJS('particles-js', {
    particles: {
      color: '#fff',
      color_random: false,
      shape: 'triangle', // "circle", "edge" or "triangle"
      opacity: {
        opacity: 1,
        anim: {
          enable: true,
          speed: Math.floor(ratio * MAX_SPEED),
          opacity_min: 0,
          sync: false
        }
      },
      size: Math.floor(ratio * MAX_SIZE),
      size_random: true,
      nb: Math.floor(ratio * MAX_PARTICLES),
      line_linked: {
        enable_auto: true,
        distance: Math.floor(ratio * MAX_DISTANCE),
        color: '#fff',
        opacity: 1,
        width: 1,
        condensed_mode: {
          enable: false,
          rotateX: 600,
          rotateY: 600
        }
      },
      anim: {
        enable: true,
        speed: 1
      }
    },
    interactivity: {
      enable: true,
      mouse: {
        distance: Math.floor(ratio * MAX_MOUSE_DISTANCE)
      },
      detect_on: 'window', // "canvas" or "window"
      mode: 'grab', // "grab" of false
      line_linked: {
        opacity: .5
      },
      events: {
        onclick: {
          enable: true,
          mode: 'push', // "push" or "remove"
          nb: Math.floor(ratio * MAX_SIZE)
        },
        onresize: {
          enable: true,
          mode: 'out', // "out" or "bounce"
          density_auto: false,
          density_area: 100 // nb_particles = particles.nb * (canvas width *  canvas height / 1000) / density_area
        }
      }
    },
    /* Retina Display Support */
    retina_detect: true
  });
}


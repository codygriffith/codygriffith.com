<script context="module" lang="ts">
  export const prerender = true;
</script>

<script lang="ts">
  import MyWork from "./MyWork.svelte";

  import { onDestroy, onMount } from "svelte";

  import Counter from "$lib/Counter.svelte";
  import Particles from "svelte-particles";
  import { loadFull } from "tsparticles";
  import { scale } from "svelte/transition";

  let show = false;
  let interval;

  onMount(() => {
    interval = setInterval(() => {
      show = !show;
    }, 2000);
  });

  onDestroy(() => {
    if (interval) {
      clearInterval(interval);
    }
  });

  let particlesUrl = "http://foo.bar/particles.json";

  let particlesConfig = {
    interactivity: {
      events: {
        onClick: {
          enable: true,
          mode: "push",
        },
        onHover: {
          mode: "repulse",
        },
      },
      modes: {
        bubble: {
          distance: 400,
          duration: 2,
          opacity: 0.8,
          size: 40,
          divs: {
            distance: 200,
            duration: 0.4,
            mix: false,
            selectors: [],
          },
        },
        grab: {
          distance: 400,
        },
        push: {
          groups: ["z5000", "z7500", "z2500", "z1000"],
        },
        repulse: {
          divs: {
            distance: 200,
            duration: 0.4,
            factor: 100,
            speed: 1,
            maxSpeed: 50,
            easing: "ease-out-quad",
            selectors: [],
          },
        },
      },
    },
    particles: {
      color: {
        animation: {
          h: {
            speed: 20,
          },
        },
      },
      groups: {
        z5000: {
          number: {
            value: 70,
          },
          zIndex: {
            value: 50,
          },
        },
        z7500: {
          number: {
            value: 30,
          },
          zIndex: {
            value: 75,
          },
        },
        z2500: {
          number: {
            value: 50,
          },
          zIndex: {
            value: 25,
          },
        },
        z1000: {
          number: {
            value: 40,
          },
          zIndex: {
            value: 10,
          },
        },
      },
      links: {
        color: {
          value: "#ffffff",
        },
        opacity: 0.4,
      },
      move: {
        angle: {
          value: 10,
        },
        attract: {
          rotate: {
            x: 600,
            y: 1200,
          },
        },
        direction: "top",
        enable: true,
        path: {},
        outModes: {
          bottom: "out",
          left: "out",
          right: "out",
          top: "out",
        },
        speed: 1,
        spin: {},
      },
      number: {
        value: 100,
      },
      opacity: {
        animation: {
          speed: 3,
          minimumValue: 0.1,
        },
      },
      size: {
        animation: {},
      },
      zIndex: {
        value: 5,
        opacityRate: 0.5,
      },
    },
  };

  let onParticlesLoaded = (event) => {
    const particlesContainer = event.detail.particles;

    // you can use particlesContainer to call all the Container class
    // (from the core library) methods like play, pause, refresh, start, stop
  };

  let particlesInit = async (engine) => {
    // you can use main to customize the tsParticles instance adding presets or custom shapes
    // this loads the tsparticles package bundle, it's the easiest method for getting everything ready
    // starting from v2 you can add only the features you need reducing the bundle size
    await loadFull(engine);
  };

  import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'

</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
  <div class="welcome">
    <img src="hopeful_headshot.png" alt="Welcome" />

    <!-- <Counter /> -->
    <h2>Cody Griffith</h2>

    <p>
      I am a front end web developer with 7 years of experience freelancing for
      small to medium businesses, but at this point i'm looking to move to more
      of a development focused role. Recently, I have been working on a
      full-stack saas app called Contidly - a tool for tracking and
      automatically qualifying potential clients.
    </p>
  </div>
  <!-- {#if show} -->
  <a use:scrollTo={{ref: 'myWork', duration: 1000}} class="animate_bounce">
    <svg class="w-6 h-6 text-violet-500" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
      <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
    </svg>
  </a>
  <!-- {/if} -->
</section>
<Particles
  id="tsparticles"
  options={particlesConfig}
  on:particlesLoaded={onParticlesLoaded}
  {particlesInit}
/>

<MyWork />

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
    position: relative;
    height: 100vh;
  }

  .animate_bounce {
    animation: bounce 1s infinite;
    justify-content: center;
    display: flex;
    position: absolute;
    bottom: 2%;
    width: 2vw;
  }

  .animate_bounce svg{
    margin: auto;
    color: rgba(255, 255, 255, 0.196);
  }

  @keyframes bounce {
    0%,
    100% {
      transform: translateY(-25%);
      animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
    }
    50% {
      transform: translateY(0);
      animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
    }
  }

  h1 {
    width: 100%;
  }
  .particles_layer1 {
    position: absolute;
    z-index: 100;
    opacity: 0.2;
  }

  .welcome {
    display: block;
    /* position: relative; */
    /* width: 100%; */
    padding-top: 5%;
    height: 95vh;
    padding-top: 2.5vw;
    display: flex;
    flex-direction: column;
    /* width: 80%; */
    padding-right: 2vw;
    justify-content: center;
    margin-left: 10%;
    width: 50%;
    align-self: start;
    /* padding: 0 0 calc(100% * 495 / 2048) 0; */
  }

  .welcome p {
    font-size: 1vw;
  }

  .welcome img {
    position: absolute;
    /* width: 100%; */
    height: 80%;
    /* top: 0; */
    bottom: 0;
    right: 10%;
    /* margin-top: 10%; */
    display: block;
    z-index: 10;
  }

  .welcome h2 {
    font-size: 3vw;
    margin-block-end: 0;
  }

  .welcome p {
    margin-left: 0.25vw;
  }

  .welcome video {
    position: absolute;
    left: 0;
    top: 0;
    z-index: -10;
    height: 100vh;
  }
</style>

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

<section class="relative flex flex-col items-center">
  <div class="welcome flex flex-col justify-center self-start h-[100vw] lg:h-[95vh] w-7/12 lg:w-3/5 pt-12 pr-6 ml-4 lg:ml-16 mb-[-5vw] md:mb-0">
    <img src="hopeful_headshot.png" alt="Welcome" class="absolute w-8/12 mr-[-18vw] md:mr-0 lg:w-4/12 bottom-0 right-[1vw] lg:right-[5vw] z-10" />

    <!-- <Counter /> -->
    <h2 class="text-2xl mb-2 md:text-6xl md:mb-6">Cody Griffith</h2>

    <p class="text-sm md:text-lg 2xl:text-xl ml-1 z-10">
      I am a front end web developer with 7 years of experience freelancing for
      small to medium businesses, but at this point i'm looking to move to more
      of a development focused role. Recently, I have been working on a
      full-stack saas app called Contidly - a tool for tracking and
      automatically qualifying potential clients.
    </p>
  </div>
  <!-- {#if show} -->

  <span class="inline-block animate-bounce rounded-full p-4 text-white text-sm">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a use:scrollTo={{ref: 'myWork', duration: 1000}} class="animate_bounce">
      <svg class="w-6 h-6 text-gray-500" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
        <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </a>
</span>

  
  <!-- {/if} -->
</section>
<Particles
  id="tsparticles"
  options={particlesConfig}
  on:particlesLoaded={onParticlesLoaded}
  {particlesInit}
/>

<MyWork />

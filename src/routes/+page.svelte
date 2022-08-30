

<script lang="ts">
  import MyWork from "$lib/MyWork.svelte";

  import { onDestroy, onMount } from "svelte";

  import particlesConfig from "$lib/particlesConfig.json";
  import Particles from "svelte-particles";
  import { loadFull } from "tsparticles";
  import { scale } from "svelte/transition";
  import type { Engine } from "tsparticles-engine";

  let particlesInit = async (engine: Engine) => {
    // you can use main to customize the tsParticles instance adding presets or custom shapes
    // this loads the tsparticles package bundle, it's the easiest method for getting everything ready
    // starting from v2 you can add only the features you need reducing the bundle size
    await loadFull(engine);
  };

  import { scrollTo, scrollRef, scrollTop } from "svelte-scrolling";
</script>

<svelte:head>
  <title>Cody Griffith | Web Developer</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="relative flex flex-col items-center md:h-[100vh] lg:h-[100vh]">
  <div class="welcome flex h-full flex-col justify-center py-12 md:py-0 self-start w-7/12 lg:w-3/5 pt-[20vw] pr-6 ml-4 lg:ml-16 mb-[-5vw] md:mb-0">
    <img src="hopeful_headshot.png" alt="Welcome" class="absolute w-8/12 md:w-[44vw] md:mb-[-12vw] lg:mb-0 mr-[-18vw] md:mr-0 lg:w-4/12 bottom-0 right-[1vw] lg:right-[5vw] z-10" />

    <!-- <Counter /> -->
    <h2 class="text-2xl mb-2 md:text-4xl lg:text-6xl md:mb-6">Cody Griffith</h2>

    <p class="text-[3.75vw] md:text-lg 2xl:text-xl ml-1 z-10">I am a front end web developer with 7 years of experience freelancing for small to medium businesses and at this point i'm looking to move to more of a development focused role. Recently, I have been working on a full-stack saas app called Contidly - a tool for tracking and automatically qualifying potential clients.</p>

    <div class="flex">
      <a target="_blank" class="mr-4 md:mr-8 my-4 w-6 md:w-8" href="https://github.com/codygriffith">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" class="iconify iconify--iconoir">
          <g fill="none" stroke="#ffffffb3" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
            ><path d="M16 22.027v-2.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7a5.44 5.44 0 0 0-1.5-3.75a5.07 5.07 0 0 0-.09-3.77s-1.18-.35-3.91 1.48a13.38 13.38 0 0 0-7 0c-2.73-1.83-3.91-1.48-3.91-1.48A5.07 5.07 0 0 0 5 5.797a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7a3.37 3.37 0 0 0-.94 2.58v2.87" />
            <path d="M9 20.027c-3 .973-5.5 0-7-3" />
          </g>
        </svg>
      </a>

      <a target="_blank" class="mr-4 md:mr-8 my-4 w-6 md:w-8" href="https://www.linkedin.com/in/cody-g/">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20" class="iconify iconify--dashicons">
          <path fill="#ffffffb3" d="M2.5 18h3V6.9h-3V18zM4 2c-1 0-1.8.8-1.8 1.8S3 5.6 4 5.6s1.8-.8 1.8-1.8S5 2 4 2zm6.6 6.6V6.9h-3V18h3v-5.7c0-3.2 4.1-3.4 4.1 0V18h3v-6.8c0-5.4-5.7-5.2-7.1-2.6z" />
        </svg>
      </a>
    </div>
  </div>
  <!-- {#if show} -->

  <span class="inline-block animate-bounce rounded-full p-4 text-white text-sm absolute bottom-0">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a use:scrollTo={{ ref: "myWork", duration: 1000 }} class="animate_bounce">
      <svg class="w-6 h-6 text-gray-500" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
        <path d="M19 14l-7 7m0 0l-7-7m7 7V3" />
      </svg>
    </a>
  </span>

  <!-- {/if} -->
</section>
<Particles id="tsparticles" options={particlesConfig} {particlesInit} />

<MyWork />

<script context="module" lang="ts">
  export const prerender = true;
</script>

<script lang="ts">
  import MyWork from "./MyWork.svelte";

  import { onDestroy, onMount } from "svelte";

  import Counter from "$lib/Counter.svelte";
  import particlesConfig from "$lib/particlesConfig.json"
  import Particles from "svelte-particles";
  import { loadFull } from "tsparticles";
  import { scale } from "svelte/transition";


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
  {particlesInit}
/>

<MyWork />

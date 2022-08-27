<script context="module">
	import { browser, dev } from '$app/env';

	// we don't need any JS on this page, though we'll load
	// it in dev so that we get hot module replacement...
	export const hydrate = dev;

	// ...but if the client-side router is already loaded
	// (i.e. we came here from elsewhere in the app), use it
	export const router = browser;

	// since there's no dynamic data here, we can prerender
	// it so that it gets served as a static asset in prod
	export const prerender = true;
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="w-full h-full">

<iframe title="Resume for Cody Griffith" src="resume.pdf" width="100%" height="100%" class="frame"></iframe>

<footer></footer>


</div>

<style>
	.frame {
  display: block;
  width: 100vw;
  height: 95vh;
  max-width: 100%;
  margin: 0;
  padding: 0;
  border: 0 none;
  box-sizing: border-box;
}

/* :global(header) {
    position: unset !important;
} */
</style>




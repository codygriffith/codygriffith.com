<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import Scroller from '@sveltejs/svelte-scroller';

    let count = 0;
	let index = 0;
	let offset = 0;
	let progress = 0.0;
	let top = 0.1;
	let threshold = 0.5;
	let bottom = 0.9;
</script>

<section>
    <h1>Hello</h1>
    <Scroller
    {top}
    {threshold}
    {bottom}
    bind:count
    bind:index
    bind:offset
    bind:progress
	>
    <div slot="background">
        <p>current section: <strong>{index + 1}/{count}</strong></p>
        <progress value="{count ? (index + 1) / count : 0}"></progress>
        
        <p>offset in current section</p>
        <progress value={offset || 0}></progress>
        
        <p>total progress</p>
        <progress value={progress || 0}></progress>
    </div>
    
    <div slot="foreground">
        <section>section 1</section>
        <section>section 2</section>
        <section>section 3</section>
        <section>section 4</section>
        <section>section 5</section>
    </div>
</Scroller>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 1;
		position: relative;
		/* height: 100vh; */
        background-color: rgba(0, 0, 0, 0.705);
	}

    section div {
        /* width: 100%; */
    }

    [slot="background"]{
        border: none !important;
    }

    :global(svelte-scroller-outer) {
		width: 100%;
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
		height: 100vh;
		padding-top: 2.5vw;
		display: flex;
		flex-direction: column;
		width: 80%;
		justify-content: center;
		/* padding: 0 0 calc(100% * 495 / 2048) 0; */
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

	.welcome h2{
		font-size: 3vw;
		margin-block-end: 0;
	}

	.welcome p{
		margin-left: .25vw;
	}

	.welcome video {
		position: absolute;
		left: 0;
		top: 0;
		z-index: -10;
		height: 100vh;
	}




















    .demo {
		padding: 0 100px 0 0;
	}
	
	[slot="background"] {
		background-color: rgba(255,62,0,0.05);
		border-top: 2px solid #ff3e00;
		border-bottom: 2px solid #ff3e00;
		font-size: 1.4em;
		overflow: hidden;
		padding: 1em;
	}
	
	[slot="background"] p {
		margin: 0;
	}
	
	[slot="foreground"] {
		pointer-events: none;
	}
	
	[slot="foreground"] section {
		pointer-events: all;
	}
	
	section {
		height: 80vh;
        background-color: rgba(0, 0, 0, 0.705);
		color: white;
		padding: 1em;
		margin: 0 0 2em 0;
	}
</style>


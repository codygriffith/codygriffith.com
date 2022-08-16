<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import Scroller from "@sveltejs/svelte-scroller";
	import { slide } from 'svelte/transition';


	let count = 0;
	let index = 0;
	let offset = 0;
	let progress = 0.0;
	let top = 0.1;
	let threshold = 0.75;
	let bottom = 0.9;

	let items = [
		{ name: "Contidly", url: "https://contidly.com", summary: "Saas webapp for automatically qualifying leads and tracking interactions." },
		{ name: "Pathlight", url: "https://pathlight.dev", summary: "Public API for auditing a web address using Google Lighthouse and dashboard for displaying and viewing results." },
	];

	import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'

</script>

<section class="main" id="myWork" use:scrollRef={'myWork'}>
	<h1 class="title">My Projects</h1>
	<Scroller
		{top}
		{threshold}
		{bottom}
		bind:count
		bind:index
		bind:offset
		bind:progress
	>
		<!-- <div slot="background">
			<p>current section: <strong>{index + 1}/{count}</strong></p>
			<progress value={count ? (index + 1) / count : 0} />

			<p>offset in current section</p>
			<progress value={offset || 0} />

			<p>total progress</p>
			<progress value={progress || 0} />
		</div> -->

		<div slot="foreground">
			{#each items as item, i}
				<!-- content here -->
				<section>
					{#if i <= index && count != 0}
						<div class="textual" transition:slide|local="{{ duration: 2000 }}">
							<h1>{item.name}</h1>
							<p class="summary">{item.summary}</p>
							<!-- <p>{i}</p> -->

							<!-- content here -->
						</div>
					{/if}
					<!-- <iframe src="http://localhost:8888"></iframe> -->
					<div class="desktop_render">
						<iframe
							src={item.url}
							width="62%"
							height="84%"
							style="-webkit-transform:scale(0.5);-moz-transform-scale(0.5);"
						/>
						<img src="laptop-png-grey.png" alt="" />
					</div>
					<div class="mobile_render">
						<iframe
							src={item.url}
							width="15.3%"
							height="63%"
							style="-webkit-transform:scale(0.59);-moz-transform-scale(0.59);"
						/>
						<img src="phone.png" alt="" />
					</div>
				</section>
			{/each}
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
		overflow: hidden;
		/* height: 100vh; */
		/* background-color: rgba(0, 0, 0, 0.705); */
	}

	.main .title {
		/* background-color: black; */
	}

	.textual .summary {
		font-size: 1vw;
	}

	section div {
		/* width: 100%; */
	}

	[slot="background"] {
		border: none !important;
		background: none !important;
	}

	.desktop_render {
		width: 100%;
		justify-content: end;
		display: flex;
		height: 100%;
		position: relative;
		align-items: center;
		margin-right: 15%;
		/* background-image: url("laptop-png.png"); */
		/* overflow: hidden; */
	}
	.mobile_render {
		justify-content: end;
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		margin-top: 15%;
		/* margin-right: -10%; */
		/* overflow: hidden; */
	}

	.textual {
		position: absolute;
		margin-left: 5%;
		left: 0;
		width: 40% !important;
		margin-top: -5vw;
		/* text-shadow: #ff3e00 .1vw .1vw; */
	}

	.textual h1 {
		font-size: 2vw;
		margin-block-start: 0;
		margin-block-end: 0;
	}

	.desktop_render img {
		/* position: absolute; */
		height: 70%;
		/* justify-self: center; */
	}

	.desktop_render iframe {
		margin-top: -9.1%;
		margin-right: -10.55%;
		z-index: 200;
		position: absolute;
	}

	.mobile_render img {
		position: absolute;
		width: 10%;
		margin-right: 8vw;
		margin-top: 6vw;
		z-index: 220;
	}

	.mobile_render iframe {
		margin-top: 2.4vw;
		margin-right: 5.45vw;
		z-index: 230;
		border: none !important;
	}

	:global(svelte-scroller-outer) {
		width: 100%;
	}

	:global(svelte-scroller-background-container) {
		/* z-index: 100 !important; */
	}

	:global(svelte-scroller-background) {
		height: 80vh !important;
		display: flex !important;
		align-items: center;
	}

	.main {
		background-color: rgba(0, 0, 0, 0.705);
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

	.demo {
		padding: 0 100px 0 0;
	}

	[slot="background"] {
		/* background-color: rgba(255,62,0,0.05); */
		border-top: 2px solid #ff3e00;
		border-bottom: 2px solid #ff3e00;
		font-size: 1.4em;
		overflow: hidden;
		padding: 1em;
		/* z-index: 100; */
	}

	[slot="background"] p {
		margin: 0;
		/* z-index: 100; */
	}

	[slot="foreground"] {
		pointer-events: none;

	}

	[slot="foreground"] .textual {
		/* pointer-events: none; */
		width: 100%;
	}

	[slot="foreground"] iframe {
		background-color: white;
	}

	[slot="foreground"] section {
		pointer-events: all;
		background: #1c1c1c23;
	}

	[slot="foreground"] h1 {
		width: fit-content;
	}

	section {
		height: 80vh;
		color: white;
		padding: 1em;
		margin: 0 0 2em 0;
	}
</style>

<svelte:head>
	<title>Cody Griffith | Resume</title>
	<meta
		name="description"
		content="Resume of Cody Griffith, front end web developer in Columbus, GA — full-stack JavaScript and TypeScript, SvelteKit, React and Cloudflare Workers."
	/>
</svelte:head>

<iframe title="Resume for Cody Griffith" src="resume.pdf" class="frame"></iframe>

<!-- Phone browsers only render the first page of an embedded PDF, so they get a link
     to the file itself instead. -->
<a class="open-pdf" href="resume.pdf" target="_blank" rel="noopener">
	Open resume.pdf in a new tab
</a>

<style>
	.frame {
		display: block;
		width: 100%;
		height: 95vh;
		margin: 0;
		padding: 0;
		border: 0 none;
		box-sizing: border-box;
	}

	.open-pdf {
		display: block;
		padding: 1rem;
		text-align: center;
	}

	@media (min-width: 768px) {
		.open-pdf {
			display: none;
		}
	}
</style>




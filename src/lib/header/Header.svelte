<script>
	import { page } from '$app/stores';
	import logo from './svelte-logo.svg';
</script>

<header class:fixed={$page.url.pathname != '/resume'}>

	<nav>
		<div>
			<a href="/" class="text-xl font-bold">
				<!-- <img src={logo} alt="SvelteKit" /> -->
				Cody Griffith
			</a>
		</div>
		<div>
			<ul>
				<!-- <li class:active={$page.url.pathname === '/'}><a sveltekit:prefetch href="/">Home</a></li> -->
				<!-- <li class:active={$page.url.pathname === '/about'}>
					<a sveltekit:prefetch href="/about">About</a>
				</li> -->
				<!-- <li class:active={$page.url.pathname === '/todos'}>
					<a sveltekit:prefetch href="/todos">Todos</a>
				</li> -->
				<li class:active={$page.url.pathname === '/resume'} class="font-semibold">
					<a sveltekit:prefetch href="/resume">Resume</a>
				</li>
			</ul>
			
		</div>
	</nav>

	<div class="corner">
		<!-- TODO put something else here? github link? -->
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: center;
		background-color: black;
		/* position: fixed; */
		width: 100%;
		z-index: 200;
	}

	.corner {
		width: 3em;
		height: 3em;
	}


	nav {
		display: flex;
		justify-content: space-between;
		/* --background: black; */
		width: 91%;
		z-index: 200;
		position: absolute;
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
		margin: 1em;
	}

	li.active::before {
		--size: 1px;
		content: '';
		width: 95%;
		height: 0;
		position: absolute;
		top: 0;
		/* left: calc(50% - var(--size)); */
		/* border: var(--size) solid transparent; */
		border: var(--size) solid var(--accent-color);
	}

	nav a {
		display: flex;
		flex-direction: row;
		height: 100%;
		align-items: center;
		/* margin: 0 1em; */
		color: var(--heading-color);
		/* font-weight: 700; */
		/* font-size: 1rem; */
		/* text-transform: uppercase; */
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--accent-color);
	}
</style>

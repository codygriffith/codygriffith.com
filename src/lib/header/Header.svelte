<script>
	import { page } from "$app/stores";
</script>

<header class:fixed={$page.url.pathname != "/resume"}>
	<nav class="text-white">
		<div>
			<a href="/" class="text-xl font-bold">Cody Griffith</a>
		</div>
		<div>
			<ul>
				<li
					class:active={$page.url.pathname === "/resume"}
					class="font-semibold"
				>
					<a href="/resume">Resume</a>
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
	}

	li {
		position: relative;
		height: 100%;
		margin: 1em;
	}

	li.active::before {
		content: "";
		width: 95%;
		height: 0;
		position: absolute;
		top: 0;
		border: 1px solid var(--accent-color);
	}

	nav a {
		display: flex;
		flex-direction: row;
		height: 100%;
		align-items: center;
		color: var(--heading-color);
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--accent-color);
	}
</style>

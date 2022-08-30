<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	import { page } from '$app/stores';

	import '../app.css';
</script>

<Header />

<main class="overflow-hidden">
	<slot />
</main>

{#if !($page.url.pathname === '/resume')}
	<footer>
		<!-- content here -->
		<p>©2022 Cody Griffith</p>
	</footer>
{/if}

<style>
	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		width: 100%;
		box-sizing: border-box;
		position: relative;
		/* height: 100vh; */
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 40px;
	}

	@media (min-width: 480px) {
		footer {
			padding: 40px 0;
		}
	}
</style>

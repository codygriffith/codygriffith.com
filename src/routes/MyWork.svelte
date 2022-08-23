<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import Scroller from "@sveltejs/svelte-scroller";
	import { slide } from "svelte/transition";

	let count = 0;
	let index = 0;
	let offset = 0;
	let progress = 0.2;
	let top = 0.1;
	let threshold = 0.85;
	let bottom = 0.9;

	let items = [
		{ name: "Contidly", url: "https://contidly.com", summary: "Saas webapp for automatically qualifying leads and tracking interactions.", tags: ["netlify", "stripe", "tailwindcss", "svelte"] },
		{ name: "Pathlight", url: "https://pathlight.dev", summary: "Public API for auditing a web address using Google Lighthouse and dashboard for displaying and viewing results.", tags: ["netlify", "tailwindcss", "svelte", "AWS"] },
	];

	import { scrollTo, scrollRef, scrollTop } from "svelte-scrolling";
</script>

<section class="main" id="myWork" use:scrollRef={"myWork"}>
	<h1 class="title text-base md:text-2xl mt-8 mb-4">My Projects</h1>
	<Scroller {top} {threshold} {bottom} bind:count bind:index bind:offset bind:progress>
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
				<section class="flex md:flex-col justify-center relative">
					{#if i <= index && count != 0}
						<div class="textual mt-8 w-full md:w-3/6 z-[100]" transition:slide={{ duration: 2000 }}>
							<h1 class="text-3xl md:text-5xl">{item.name}</h1>
							<p class="summary text-based my-2 pr-6">{item.summary}</p>

							<div class="w-auto flex mt-5">
								<!-- Netlify -->
								<!-- {item.tags[0]} -->
								{#if item.tags.includes("netlify")}
									<a href="https://www.netlify.com/" class="hover:transform w-auto mr-4 mt-1" target="_blank">
										<svg stroke="currentColor" fill="currentColor" stroke-width="0" role="img" viewBox="0 0 24 24" color="#15847D" style="color:#15847D" height="2.25rem" width="2.25rem" xmlns="http://www.w3.org/2000/svg">
											<path
												d="M16.934 8.519a1.044 1.044 0 0 1 .303.23l2.349-1.045-2.192-2.171-.491 2.954zM12.06 6.546a1.305 1.305 0 0 1 .209.574l3.497 1.482a1.044 1.044 0 0 1 .355-.177l.574-3.55-2.13-2.234-2.505 3.852v.053zm11.933 5.491l-3.748-3.748-2.548 1.044 6.264 2.662s.053.042.032.042zm-.627.606l-6.013-2.569a1.044 1.044 0 0 1-.7.407l-.647 3.957a1.044 1.044 0 0 1 .303.731l3.633.762 3.33-3.31v-.062zM15.4 9.25L12.132 7.86a1.2 1.2 0 0 1-1.044.543h-.199L8.185 12.58l7.225-3.132v.01a.887.887 0 0 1 0-.167.052.052 0 0 0-.01-.041zm3.967 7.308l-3.195-.658a1.096 1.096 0 0 1-.46.344l-.761 4.72 4.437-4.396s-.01.02-.021.02zm-4.469-.324a1.044 1.044 0 0 1-.616-.71l-5.95-1.222-.084.136 5.398 7.81.323-.324.919-5.67s.031.022.01.011zm-6.441-2.652l5.878 1.211a1.044 1.044 0 0 1 .824-.522l.637-3.894-.135-.115-7.308 3.132a1.817 1.817 0 0 1 .104.188zm-2.464.981l-.125-.125-2.537 1.044 1.232 1.222 1.399-2.172zm1.67.397a1.368 1.368 0 0 1-.563.125 1.389 1.389 0 0 1-.45-.073l-1.544 2.245 6.765 6.702 1.19-1.18zm-.95-2.641a1.702 1.702 0 0 1 .314 0 1.378 1.378 0 0 1 .344 0l2.735-4.25a1.19 1.19 0 0 1-.334-.824 1.242 1.242 0 0 1 0-.271l-3.32-1.535-2.672 2.6zm.303-7.402l3.237 1.378a1.242 1.242 0 0 1 .835-.282 1.357 1.357 0 0 1 .397.063l2.526-3.947L11.923.041 7.016 4.854s-.01.052 0 .063zm-1.21 8.164a1.566 1.566 0 0 1 .24-.334L3.278 8.613 0 11.797l5.804 1.284zm-.262.7L.533 12.735l2.203 2.235 2.777-1.18z"
											/>
										</svg>
									</a>
									<!-- content here -->
								{/if}
								{#if item.tags.includes("stripe")}
									<a href="https://stripe.com/" class="hover:transform scale-120 mr-4" target="_blank">
										<!-- <div class="h-14 w-14 rounded-full flex items-center justify-center bg-gray-700 shadow-md cursor-pointer hover:shadow-lg hover:bg-gray-600 hover:shadow-lg transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110"> -->
										<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 640 512" color="white" style="color:white" height="3rem" width="3rem" xmlns="http://www.w3.org/2000/svg">
											<path
												d="M165 144.7l-43.3 9.2-.2 142.4c0 26.3 19.8 43.3 46.1 43.3 14.6 0 25.3-2.7 31.2-5.9v-33.8c-5.7 2.3-33.7 10.5-33.7-15.7V221h33.7v-37.8h-33.7zm89.1 51.6l-2.7-13.1H213v153.2h44.3V233.3c10.5-13.8 28.2-11.1 33.9-9.3v-40.8c-6-2.1-26.7-6-37.1 13.1zm92.3-72.3l-44.6 9.5v36.2l44.6-9.5zM44.9 228.3c0-6.9 5.8-9.6 15.1-9.7 13.5 0 30.7 4.1 44.2 11.4v-41.8c-14.7-5.8-29.4-8.1-44.1-8.1-36 0-60 18.8-60 50.2 0 49.2 67.5 41.2 67.5 62.4 0 8.2-7.1 10.9-17 10.9-14.7 0-33.7-6.1-48.6-14.2v40c16.5 7.1 33.2 10.1 48.5 10.1 36.9 0 62.3-15.8 62.3-47.8 0-52.9-67.9-43.4-67.9-63.4zM640 261.6c0-45.5-22-81.4-64.2-81.4s-67.9 35.9-67.9 81.1c0 53.5 30.3 78.2 73.5 78.2 21.2 0 37.1-4.8 49.2-11.5v-33.4c-12.1 6.1-26 9.8-43.6 9.8-17.3 0-32.5-6.1-34.5-26.9h86.9c.2-2.3.6-11.6.6-15.9zm-87.9-16.8c0-20 12.3-28.4 23.4-28.4 10.9 0 22.5 8.4 22.5 28.4zm-112.9-64.6c-17.4 0-28.6 8.2-34.8 13.9l-2.3-11H363v204.8l44.4-9.4.1-50.2c6.4 4.7 15.9 11.2 31.4 11.2 31.8 0 60.8-23.2 60.8-79.6.1-51.6-29.3-79.7-60.5-79.7zm-10.6 122.5c-10.4 0-16.6-3.8-20.9-8.4l-.3-66c4.6-5.1 11-8.8 21.2-8.8 16.2 0 27.4 18.2 27.4 41.4.1 23.9-10.9 41.8-27.4 41.8zm-126.7 33.7h44.6V183.2h-44.6z"
											/>
										</svg>
										<!-- </div> -->
									</a>
								{/if}

								{#if item.tags.includes("tailwindcss")}
									<a href="https://tailwindcss.com/" class="hover:transform scale-120 w-[12%] md:w-[4%] mt-3 mr-4" target="_blank">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 54 33"><g clip-path="url(#prefix__clip0)"><path fill="#38bdf8" fill-rule="evenodd" d="M27 0c-7.2 0-11.7 3.6-13.5 10.8 2.7-3.6 5.85-4.95 9.45-4.05 2.054.513 3.522 2.004 5.147 3.653C30.744 13.09 33.808 16.2 40.5 16.2c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C36.756 3.11 33.692 0 27 0zM13.5 16.2C6.3 16.2 1.8 19.8 0 27c2.7-3.6 5.85-4.95 9.45-4.05 2.054.514 3.522 2.004 5.147 3.653C17.244 29.29 20.308 32.4 27 32.4c7.2 0 11.7-3.6 13.5-10.8-2.7 3.6-5.85 4.95-9.45 4.05-2.054-.513-3.522-2.004-5.147-3.653C23.256 19.31 20.192 16.2 13.5 16.2z" clip-rule="evenodd" /></g><defs><clipPath id="prefix__clip0"><path fill="#fff" d="M0 0h54v32.4H0z" /></clipPath></defs></svg>
									</a>
								{/if}

								{#if item.tags.includes("svelte")}
									<a href="https://svelte.dev/" class="hover:transform scale-120 w-[8%] md:w-[3%] mr-4" target="_blank">
										<svg width="100%" height="100%" viewBox="0 0 148 178" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
											<g transform="matrix(1,0,0,1,-34.2524,-29.2672)">
												<g id="a" transform="matrix(1.584,0,0,1.584,34.228,29.267)">
													<path d="M87.269,14.819C76.869,-0.066 56.328,-4.478 41.477,4.984L15.4,21.608C8.277,26.087 3.363,33.369 1.876,41.651C0.632,48.551 1.726,55.673 4.984,61.882C2.751,65.269 1.228,69.073 0.507,73.065C-0.993,81.506 0.972,90.205 5.955,97.181C16.355,112.068 36.897,116.481 51.746,107.016L77.829,90.392C84.951,85.913 89.862,78.63 91.347,70.349C92.593,63.449 91.501,56.327 88.247,50.117C90.478,46.73 92,42.926 92.721,38.935C94.223,30.494 92.258,21.795 87.274,14.819" style="fill:rgb(255,62,0);fill-rule:nonzero;" />
													<path
														d="M38.929,98.582C30.541,100.762 21.632,97.46 16.692,90.339C13.696,86.144 12.514,80.914 13.416,75.839C13.567,75.014 13.775,74.2 14.039,73.404L14.53,71.904L15.867,72.885C18.952,75.153 22.402,76.878 26.067,77.985L27.036,78.279L26.947,79.247C26.829,80.622 27.203,81.996 28,83.122C29.488,85.269 32.172,86.265 34.7,85.607C35.266,85.457 35.805,85.22 36.3,84.907L62.382,68.281C63.672,67.469 64.562,66.15 64.833,64.65C65.103,63.12 64.747,61.544 63.845,60.279C62.357,58.132 59.673,57.136 57.145,57.792C56.579,57.943 56.04,58.179 55.545,58.492L45.592,64.837C43.954,65.878 42.167,66.662 40.292,67.163C31.904,69.344 22.995,66.041 18.055,58.92C15.058,54.726 13.876,49.495 14.778,44.42C15.674,39.44 18.63,35.062 22.915,32.37L49,15.747C50.638,14.705 52.425,13.919 54.3,13.418C62.688,11.238 71.597,14.54 76.537,21.661C79.533,25.855 80.715,31.086 79.814,36.161C79.662,36.986 79.453,37.799 79.19,38.596L78.699,40.096L77.363,39.117C74.278,36.849 70.829,35.124 67.163,34.017L66.193,33.723L66.283,32.755C66.4,31.379 66.028,30.005 65.231,28.877C63.743,26.731 61.059,25.735 58.531,26.392C57.965,26.542 57.426,26.779 56.931,27.092L30.842,43.719C29.552,44.53 28.662,45.849 28.393,47.349C28.122,48.879 28.477,50.456 29.379,51.721C30.867,53.867 33.551,54.864 36.079,54.208C36.645,54.057 37.184,53.821 37.679,53.508L47.631,47.166C49.268,46.124 51.056,45.338 52.931,44.838C61.319,42.658 70.227,45.96 75.167,53.081C78.164,57.275 79.346,62.506 78.444,67.581C77.55,72.561 74.596,76.94 70.314,79.635L44.229,96.253C42.592,97.295 40.804,98.081 38.929,98.582"
														style="fill:white;fill-rule:nonzero;"
													/>
												</g>
											</g>
										</svg>
									</a>
								{/if}
								{#if item.tags.includes("AWS")}

								<a href="https://aws.amazon.com/" class="hover:transform scale-120 w-[4%] mr-4 mt-2" target="_blank">
									<svg width="100%" height="100%" viewBox="0 0 301 180" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
										<g transform="matrix(1,0,0,1,-1.66798,-1.1)">
											<g>
												<path d="M86.4,66.4C86.4,70.1 86.8,73.1 87.5,75.3C88.3,77.5 89.3,79.9 90.7,82.5C91.2,83.3 91.4,84.1 91.4,84.8C91.4,85.8 90.8,86.8 89.5,87.8L83.2,92C82.3,92.6 81.4,92.9 80.6,92.9C79.6,92.9 78.6,92.4 77.6,91.5C76.2,90 75,88.4 74,86.8C73,85.1 72,83.2 70.9,80.9C63.1,90.1 53.3,94.7 41.5,94.7C33.1,94.7 26.4,92.3 21.5,87.5C16.6,82.7 14.1,76.3 14.1,68.3C14.1,59.8 17.1,52.9 23.2,47.7C29.3,42.5 37.4,39.9 47.7,39.9C51.1,39.9 54.6,40.2 58.3,40.7C62,41.2 65.8,42 69.8,42.9L69.8,35.6C69.8,28 68.2,22.7 65.1,19.6C61.9,16.5 56.5,15 48.8,15C45.3,15 41.7,15.4 38,16.3C34.3,17.2 30.7,18.3 27.2,19.7C25.6,20.4 24.4,20.8 23.7,21C23,21.2 22.5,21.3 22.1,21.3C20.7,21.3 20,20.3 20,18.2L20,13.3C20,11.7 20.2,10.5 20.7,9.8C21.2,9.1 22.1,8.4 23.5,7.7C27,5.9 31.2,4.4 36.1,3.2C41,1.9 46.2,1.3 51.7,1.3C63.6,1.3 72.3,4 77.9,9.4C83.4,14.8 86.2,23 86.2,34L86.2,66.4L86.4,66.4ZM45.8,81.6C49.1,81.6 52.5,81 56.1,79.8C59.7,78.6 62.9,76.4 65.6,73.4C67.2,71.5 68.4,69.4 69,67C69.6,64.6 70,61.7 70,58.3L70,54.1C67.1,53.4 64,52.8 60.8,52.4C57.6,52 54.5,51.8 51.4,51.8C44.7,51.8 39.8,53.1 36.5,55.8C33.2,58.5 31.6,62.3 31.6,67.3C31.6,72 32.8,75.5 35.3,77.9C37.7,80.4 41.2,81.6 45.8,81.6ZM126.1,92.4C124.3,92.4 123.1,92.1 122.3,91.4C121.5,90.8 120.8,89.4 120.2,87.5L96.7,10.2C96.1,8.2 95.8,6.9 95.8,6.2C95.8,4.6 96.6,3.7 98.2,3.7L108,3.7C109.9,3.7 111.2,4 111.9,4.7C112.7,5.3 113.3,6.7 113.9,8.6L130.7,74.8L146.3,8.6C146.8,6.6 147.4,5.3 148.2,4.7C149,4.1 150.4,3.7 152.2,3.7L160.2,3.7C162.1,3.7 163.4,4 164.2,4.7C165,5.3 165.7,6.7 166.1,8.6L181.9,75.6L199.2,8.6C199.8,6.6 200.5,5.3 201.2,4.7C202,4.1 203.3,3.7 205.1,3.7L214.4,3.7C216,3.7 216.9,4.5 216.9,6.2C216.9,6.7 216.8,7.2 216.7,7.8C216.6,8.4 216.4,9.2 216,10.3L191.9,87.6C191.3,89.6 190.6,90.9 189.8,91.5C189,92.1 187.7,92.5 186,92.5L177.4,92.5C175.5,92.5 174.2,92.2 173.4,91.5C172.6,90.8 171.9,89.5 171.5,87.5L156,23L140.6,87.4C140.1,89.4 139.5,90.7 138.7,91.4C137.9,92.1 136.5,92.4 134.7,92.4L126.1,92.4ZM254.6,95.1C249.4,95.1 244.2,94.5 239.2,93.3C234.2,92.1 230.3,90.8 227.7,89.3C226.1,88.4 225,87.4 224.6,86.5C224.2,85.6 224,84.6 224,83.7L224,78.6C224,76.5 224.8,75.5 226.3,75.5C226.9,75.5 227.5,75.6 228.1,75.8C228.7,76 229.6,76.4 230.6,76.8C234,78.3 237.7,79.5 241.6,80.3C245.6,81.1 249.5,81.5 253.5,81.5C259.8,81.5 264.7,80.4 268.1,78.2C271.5,76 273.3,72.8 273.3,68.7C273.3,65.9 272.4,63.6 270.6,61.7C268.8,59.8 265.4,58.1 260.5,56.5L246,52C238.7,49.7 233.3,46.3 230,41.8C226.7,37.4 225,32.5 225,27.3C225,23.1 225.9,19.4 227.7,16.2C229.5,13 231.9,10.2 234.9,8C237.9,5.7 241.3,4 245.3,2.8C249.3,1.6 253.5,1.1 257.9,1.1C260.1,1.1 262.4,1.2 264.6,1.5C266.9,1.8 269,2.2 271.1,2.6C273.1,3.1 275,3.6 276.8,4.2C278.6,4.8 280,5.4 281,6C282.4,6.8 283.4,7.6 284,8.5C284.6,9.3 284.9,10.4 284.9,11.8L284.9,16.5C284.9,18.6 284.1,19.7 282.6,19.7C281.8,19.7 280.5,19.3 278.8,18.5C273.1,15.9 266.7,14.6 259.6,14.6C253.9,14.6 249.4,15.5 246.3,17.4C243.2,19.3 241.6,22.2 241.6,26.3C241.6,29.1 242.6,31.5 244.6,33.4C246.6,35.3 250.3,37.2 255.6,38.9L269.8,43.4C277,45.7 282.2,48.9 285.3,53C288.4,57.1 289.9,61.8 289.9,67C289.9,71.3 289,75.2 287.3,78.6C285.5,82 283.1,85 280,87.4C276.9,89.9 273.2,91.7 268.9,93C264.4,94.4 259.7,95.1 254.6,95.1Z" style="fill:rgb(214,214,214);fill-rule:nonzero;"/>
												<g>
													<path d="M273.5,143.7C240.6,168 192.8,180.9 151.7,180.9C94.1,180.9 42.2,159.6 3,124.2C-0.1,121.4 2.7,117.6 6.4,119.8C48.8,144.4 101.1,159.3 155.2,159.3C191.7,159.3 231.8,151.7 268.7,136.1C274.2,133.6 278.9,139.7 273.5,143.7Z" style="fill:rgb(255,153,0);"/>
													<path d="M287.2,128.1C283,122.7 259.4,125.5 248.7,126.8C245.5,127.2 245,124.4 247.9,122.3C266.7,109.1 297.6,112.9 301.2,117.3C304.8,121.8 300.2,152.7 282.6,167.5C279.9,169.8 277.3,168.6 278.5,165.6C282.5,155.7 291.4,133.4 287.2,128.1Z" style="fill:rgb(255,153,0);"/>
												</g>
											</g>
										</g>
									</svg>
								</a>
								{/if}

							</div>
							<!-- <p>{i}</p> -->

							<!-- content here -->
						</div>
					{:else if count == undefined}
						<p>count undefined</p>
					{/if}

					<!-- <iframe src="http://localhost:8888"></iframe> -->
					<div class="desktop_render">
						<iframe class="md:mt-[-10vw] md:mr-[-10.7vw] md:w-[64vw] md:h-[36vw] mt-[-16vw] mr-[-17.25vw] h-[59vw] w-[104vw]" src={item.url} style="-webkit-transform:scale(0.5);-moz-transform-scale(0.5);" />
						<img src="laptop-png-grey.png" class="h-[50vw] md:h-[30.8vw]" alt="" />
					</div>
					<div class="mobile_render">
						<iframe src={item.url} style="-webkit-transform:scale(0.59);-moz-transform-scale(0.59);" />
						<img src="phone.png" alt="" />
					</div>
				</section>
			{/each}
		</div>
	</Scroller>
</section>

<style>
	section {
		flex: 1;
	}

	.main .title {
		/* background-color: black; */
		padding-bottom: 0.5vw;
	}

	.textual .summary {
		/* font-size: 1vw; */
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

	/* .desktop_render iframe{
		width: 64vw;
		height:  36vw;
	} */
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

	.mobile_render iframe {
		height: 26.75vw;
		width: 14.85vw;
	}

	.textual {
		position: absolute;
		margin-left: 5%;
		left: 0;
		/* width: 40%; */
		margin-top: -5vw;
		/* text-shadow: #ff3e00 .1vw .1vw; */
	}

	.textual h1 {
		/* font-size: 2vw; */
		margin-block-start: 0;
		margin-block-end: 0;
	}

	.desktop_render img {
		/* position: absolute; */
		/* justify-self: center; */
	}

	.desktop_render iframe {
		/* margin-top: -10vw; */
		/* margin-right: -10.7vw; */
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
		margin-top: 2.2vw;
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
		padding-top: 2.25vw;
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
		/* width: 100%; */
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

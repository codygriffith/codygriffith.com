<script lang="ts">
	import { slide } from "svelte/transition";

	let count = 0;
	let index = 0;
	let offset = 0;
	let progress = 0.2;
	let top = 0.1;
	let threshold = 0.85;
	let bottom = 0.9;

	let items = [
		{ 
			name: "Contidly", 
			url: "https://contidly.com",
			repo: "",
			summary: "A lightweight CRM built with Web Developers in mind - Contidly is a SaaS webapp that automates the work of choosing qualified leads and tracking interactions. Using the <a href='https://developers.google.com/speed/docs/insights/v5/get-started'>PageSpeed Insights API</a>, users are able to perform bulk audits on client websites and filter the results using selected options to leveragee that data into better marketing decisions.", 
			tags: ["cloudflare", "stripe", "tailwindcss", "svelte"] },
		{
			name: "Pathlight",
			url: "https://pathlight.dev",
			repo: "",
			summary:
				"Pathlight is a public API for auditing web addresses with Google Lighthouse. Featuring a front end dashboard, you can initiate new audits and view past scans plus their full reports. Built using <a href='https://aws.amazon.com/lambda/'>AWS Lambda</a> and an <a href='https://aws.amazon.com/sqs/'>SQS based queue</a>, Pathlight is able to infinitely scale with user demand.",
			tags: ["cloudflare", "tailwindcss", "svelte"],
		},
	];

	import { scrollTo, scrollRef, scrollTop } from "svelte-scrolling";
</script>

<section class="main" id="myWork" use:scrollRef={"myWork"}>
	<h1 class="title text-lg  md:text-2xl mt-8 mb-4">My Projects</h1>
	<!-- <Scroller {top} {threshold} {bottom} bind:count bind:index bind:offset bind:progress> -->
		

		<div>
			{#each items as item, i}
				<!-- content here -->
				<section class="flex md:flex-col justify-center relative">
					<!-- {#if i <= index && count != 0} -->
					<div class="textual md:mt-8 w-full z-[100] lg:flex ">
						<div class="lg:w-[55%]">
							<a href="{item.url}">
								<h1 class="text-3xl md:text-5xl">{item.name}</h1>
							</a>

							<p class="summary text-lg md:text-base lg:text-lg my-2 pr-6">{@html item.summary}</p>

							<div class="w-auto flex-col md:flex-row flex mt-5">
								<div class="w-auto flex">
									<!-- Netlify -->
									<!-- {item.tags[0]} -->
									{#if item.tags.includes("cloudflare")}
										<a href="https://www.cloudflare.com/" class="hover:transform w-auto mr-2 mt-1" target="_blank">
											<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 42" height="3rem" width="4rem" fill="none">
												<g clip-path="url(#a)">
												  <path fill="#FBAD41" d="M52.688 13.028c-.22 0-.437.008-.654.015a.297.297 0 0 0-.102.024.365.365 0 0 0-.236.255l-.93 3.249c-.401 1.397-.252 2.687.422 3.634.618.876 1.646 1.39 2.894 1.45l5.045.306c.15.008.28.08.359.199a.492.492 0 0 1 .051.434.64.64 0 0 1-.547.426l-5.242.306c-2.848.132-5.912 2.456-6.987 5.29l-.378 1a.28.28 0 0 0 .248.382h18.054a.48.48 0 0 0 .464-.35 13.12 13.12 0 0 0 .48-3.54c0-7.22-5.789-13.072-12.933-13.072"/>
												  <path fill="#F6821F" d="m44.808 29.578.334-1.175c.402-1.397.253-2.687-.42-3.634-.62-.876-1.647-1.39-2.896-1.45l-23.665-.306a.467.467 0 0 1-.374-.199.492.492 0 0 1-.052-.434.64.64 0 0 1 .552-.426l23.886-.306c2.836-.131 5.9-2.456 6.975-5.29l1.362-3.6a.914.914 0 0 0 .04-.477C48.998 5.259 42.79 0 35.368 0c-6.842 0-12.647 4.462-14.73 10.665a6.92 6.92 0 0 0-4.911-1.374c-3.28.33-5.92 3.002-6.246 6.318a7.148 7.148 0 0 0 .18 2.472c-5.36.16-9.66 4.598-9.66 10.052 0 .493.035.979.106 1.453a.46.46 0 0 0 .457.402h43.704a.57.57 0 0 0 .54-.418"/>
												</g>
											  </svg>
										</a>
										<!-- content here -->
									{/if}
									<!-- {#if item.tags.includes("stripe")}
										<a href="https://stripe.com/" class="hover:transform scale-120 mr-4" target="_blank">
											<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 640 512" color="white" style="color:white" height="3rem" width="3rem" xmlns="http://www.w3.org/2000/svg">
												<path
													d="M165 144.7l-43.3 9.2-.2 142.4c0 26.3 19.8 43.3 46.1 43.3 14.6 0 25.3-2.7 31.2-5.9v-33.8c-5.7 2.3-33.7 10.5-33.7-15.7V221h33.7v-37.8h-33.7zm89.1 51.6l-2.7-13.1H213v153.2h44.3V233.3c10.5-13.8 28.2-11.1 33.9-9.3v-40.8c-6-2.1-26.7-6-37.1 13.1zm92.3-72.3l-44.6 9.5v36.2l44.6-9.5zM44.9 228.3c0-6.9 5.8-9.6 15.1-9.7 13.5 0 30.7 4.1 44.2 11.4v-41.8c-14.7-5.8-29.4-8.1-44.1-8.1-36 0-60 18.8-60 50.2 0 49.2 67.5 41.2 67.5 62.4 0 8.2-7.1 10.9-17 10.9-14.7 0-33.7-6.1-48.6-14.2v40c16.5 7.1 33.2 10.1 48.5 10.1 36.9 0 62.3-15.8 62.3-47.8 0-52.9-67.9-43.4-67.9-63.4zM640 261.6c0-45.5-22-81.4-64.2-81.4s-67.9 35.9-67.9 81.1c0 53.5 30.3 78.2 73.5 78.2 21.2 0 37.1-4.8 49.2-11.5v-33.4c-12.1 6.1-26 9.8-43.6 9.8-17.3 0-32.5-6.1-34.5-26.9h86.9c.2-2.3.6-11.6.6-15.9zm-87.9-16.8c0-20 12.3-28.4 23.4-28.4 10.9 0 22.5 8.4 22.5 28.4zm-112.9-64.6c-17.4 0-28.6 8.2-34.8 13.9l-2.3-11H363v204.8l44.4-9.4.1-50.2c6.4 4.7 15.9 11.2 31.4 11.2 31.8 0 60.8-23.2 60.8-79.6.1-51.6-29.3-79.7-60.5-79.7zm-10.6 122.5c-10.4 0-16.6-3.8-20.9-8.4l-.3-66c4.6-5.1 11-8.8 21.2-8.8 16.2 0 27.4 18.2 27.4 41.4.1 23.9-10.9 41.8-27.4 41.8zm-126.7 33.7h44.6V183.2h-44.6z"
												/>
											</svg>
										</a>
									{/if} -->

									{#if item.tags.includes("tailwindcss")}
										<a href="https://tailwindcss.com/" class="hover:transform scale-120 flex items-center mr-4" target="_blank">
											<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" height="2.25rem" width="2.25rem" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 154" class="iconify iconify--logos"><defs><linearGradient id="iconifySvelte10" x1="-2.778%" x2="100%" y1="32%" y2="67.556%"><stop offset="0%" stop-color="#2298BD"></stop><stop offset="100%" stop-color="#0ED7B5"></stop></linearGradient></defs><path fill="url(#iconifySvelte10)" d="M128 0C93.867 0 72.533 17.067 64 51.2C76.8 34.133 91.733 27.733 108.8 32c9.737 2.434 16.697 9.499 24.401 17.318C145.751 62.057 160.275 76.8 192 76.8c34.133 0 55.467-17.067 64-51.2c-12.8 17.067-27.733 23.467-44.8 19.2c-9.737-2.434-16.697-9.499-24.401-17.318C174.249 14.743 159.725 0 128 0ZM64 76.8C29.867 76.8 8.533 93.867 0 128c12.8-17.067 27.733-23.467 44.8-19.2c9.737 2.434 16.697 9.499 24.401 17.318C81.751 138.857 96.275 153.6 128 153.6c34.133 0 55.467-17.067 64-51.2c-12.8 17.067-27.733 23.467-44.8 19.2c-9.737-2.434-16.697-9.499-24.401-17.318C110.249 91.543 95.725 76.8 64 76.8Z"></path></svg>
										</a>
									{/if}

									{#if item.tags.includes("svelte")}
										<a href="https://svelte.dev/" class="hover:transform scale-120 flex items-center mr-4" target="_blank">
											<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" height="2rem" width="2rem" preserveAspectRatio="xMidYMid meet" viewBox="0 0 256 308" class="iconify iconify--logos"><path fill="#FF3E00" d="M239.682 40.707C211.113-.182 154.69-12.301 113.895 13.69L42.247 59.356a82.198 82.198 0 0 0-37.135 55.056a86.566 86.566 0 0 0 8.536 55.576a82.425 82.425 0 0 0-12.296 30.719a87.596 87.596 0 0 0 14.964 66.244c28.574 40.893 84.997 53.007 125.787 27.016l71.648-45.664a82.182 82.182 0 0 0 37.135-55.057a86.601 86.601 0 0 0-8.53-55.577a82.409 82.409 0 0 0 12.29-30.718a87.573 87.573 0 0 0-14.963-66.244"></path><path fill="#FFF" d="M106.889 270.841c-23.102 6.007-47.497-3.036-61.103-22.648a52.685 52.685 0 0 1-9.003-39.85a49.978 49.978 0 0 1 1.713-6.693l1.35-4.115l3.671 2.697a92.447 92.447 0 0 0 28.036 14.007l2.663.808l-.245 2.659a16.067 16.067 0 0 0 2.89 10.656a17.143 17.143 0 0 0 18.397 6.828a15.786 15.786 0 0 0 4.403-1.935l71.67-45.672a14.922 14.922 0 0 0 6.734-9.977a15.923 15.923 0 0 0-2.713-12.011a17.156 17.156 0 0 0-18.404-6.832a15.78 15.78 0 0 0-4.396 1.933l-27.35 17.434a52.298 52.298 0 0 1-14.553 6.391c-23.101 6.007-47.497-3.036-61.101-22.649a52.681 52.681 0 0 1-9.004-39.849a49.428 49.428 0 0 1 22.34-33.114l71.664-45.677a52.218 52.218 0 0 1 14.563-6.398c23.101-6.007 47.497 3.036 61.101 22.648a52.685 52.685 0 0 1 9.004 39.85a50.559 50.559 0 0 1-1.713 6.692l-1.35 4.116l-3.67-2.693a92.373 92.373 0 0 0-28.037-14.013l-2.664-.809l.246-2.658a16.099 16.099 0 0 0-2.89-10.656a17.143 17.143 0 0 0-18.398-6.828a15.786 15.786 0 0 0-4.402 1.935l-71.67 45.674a14.898 14.898 0 0 0-6.73 9.975a15.9 15.9 0 0 0 2.709 12.012a17.156 17.156 0 0 0 18.404 6.832a15.841 15.841 0 0 0 4.402-1.935l27.345-17.427a52.147 52.147 0 0 1 14.552-6.397c23.101-6.006 47.497 3.037 61.102 22.65a52.681 52.681 0 0 1 9.003 39.848a49.453 49.453 0 0 1-22.34 33.12l-71.664 45.673a52.218 52.218 0 0 1-14.563 6.398"></path></svg>
										</a>
									{/if}
									{#if item.tags.includes("AWS")}
										<a href="https://aws.amazon.com/" class="hover:transform scale-120 mr-4 mt-2" target="_blank">
											<svg height="2.25rem" width="2.25rem" viewBox="0 0 301 180" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
												<g transform="matrix(1,0,0,1,-1.66798,-1.1)">
													<g>
														<path
															d="M86.4,66.4C86.4,70.1 86.8,73.1 87.5,75.3C88.3,77.5 89.3,79.9 90.7,82.5C91.2,83.3 91.4,84.1 91.4,84.8C91.4,85.8 90.8,86.8 89.5,87.8L83.2,92C82.3,92.6 81.4,92.9 80.6,92.9C79.6,92.9 78.6,92.4 77.6,91.5C76.2,90 75,88.4 74,86.8C73,85.1 72,83.2 70.9,80.9C63.1,90.1 53.3,94.7 41.5,94.7C33.1,94.7 26.4,92.3 21.5,87.5C16.6,82.7 14.1,76.3 14.1,68.3C14.1,59.8 17.1,52.9 23.2,47.7C29.3,42.5 37.4,39.9 47.7,39.9C51.1,39.9 54.6,40.2 58.3,40.7C62,41.2 65.8,42 69.8,42.9L69.8,35.6C69.8,28 68.2,22.7 65.1,19.6C61.9,16.5 56.5,15 48.8,15C45.3,15 41.7,15.4 38,16.3C34.3,17.2 30.7,18.3 27.2,19.7C25.6,20.4 24.4,20.8 23.7,21C23,21.2 22.5,21.3 22.1,21.3C20.7,21.3 20,20.3 20,18.2L20,13.3C20,11.7 20.2,10.5 20.7,9.8C21.2,9.1 22.1,8.4 23.5,7.7C27,5.9 31.2,4.4 36.1,3.2C41,1.9 46.2,1.3 51.7,1.3C63.6,1.3 72.3,4 77.9,9.4C83.4,14.8 86.2,23 86.2,34L86.2,66.4L86.4,66.4ZM45.8,81.6C49.1,81.6 52.5,81 56.1,79.8C59.7,78.6 62.9,76.4 65.6,73.4C67.2,71.5 68.4,69.4 69,67C69.6,64.6 70,61.7 70,58.3L70,54.1C67.1,53.4 64,52.8 60.8,52.4C57.6,52 54.5,51.8 51.4,51.8C44.7,51.8 39.8,53.1 36.5,55.8C33.2,58.5 31.6,62.3 31.6,67.3C31.6,72 32.8,75.5 35.3,77.9C37.7,80.4 41.2,81.6 45.8,81.6ZM126.1,92.4C124.3,92.4 123.1,92.1 122.3,91.4C121.5,90.8 120.8,89.4 120.2,87.5L96.7,10.2C96.1,8.2 95.8,6.9 95.8,6.2C95.8,4.6 96.6,3.7 98.2,3.7L108,3.7C109.9,3.7 111.2,4 111.9,4.7C112.7,5.3 113.3,6.7 113.9,8.6L130.7,74.8L146.3,8.6C146.8,6.6 147.4,5.3 148.2,4.7C149,4.1 150.4,3.7 152.2,3.7L160.2,3.7C162.1,3.7 163.4,4 164.2,4.7C165,5.3 165.7,6.7 166.1,8.6L181.9,75.6L199.2,8.6C199.8,6.6 200.5,5.3 201.2,4.7C202,4.1 203.3,3.7 205.1,3.7L214.4,3.7C216,3.7 216.9,4.5 216.9,6.2C216.9,6.7 216.8,7.2 216.7,7.8C216.6,8.4 216.4,9.2 216,10.3L191.9,87.6C191.3,89.6 190.6,90.9 189.8,91.5C189,92.1 187.7,92.5 186,92.5L177.4,92.5C175.5,92.5 174.2,92.2 173.4,91.5C172.6,90.8 171.9,89.5 171.5,87.5L156,23L140.6,87.4C140.1,89.4 139.5,90.7 138.7,91.4C137.9,92.1 136.5,92.4 134.7,92.4L126.1,92.4ZM254.6,95.1C249.4,95.1 244.2,94.5 239.2,93.3C234.2,92.1 230.3,90.8 227.7,89.3C226.1,88.4 225,87.4 224.6,86.5C224.2,85.6 224,84.6 224,83.7L224,78.6C224,76.5 224.8,75.5 226.3,75.5C226.9,75.5 227.5,75.6 228.1,75.8C228.7,76 229.6,76.4 230.6,76.8C234,78.3 237.7,79.5 241.6,80.3C245.6,81.1 249.5,81.5 253.5,81.5C259.8,81.5 264.7,80.4 268.1,78.2C271.5,76 273.3,72.8 273.3,68.7C273.3,65.9 272.4,63.6 270.6,61.7C268.8,59.8 265.4,58.1 260.5,56.5L246,52C238.7,49.7 233.3,46.3 230,41.8C226.7,37.4 225,32.5 225,27.3C225,23.1 225.9,19.4 227.7,16.2C229.5,13 231.9,10.2 234.9,8C237.9,5.7 241.3,4 245.3,2.8C249.3,1.6 253.5,1.1 257.9,1.1C260.1,1.1 262.4,1.2 264.6,1.5C266.9,1.8 269,2.2 271.1,2.6C273.1,3.1 275,3.6 276.8,4.2C278.6,4.8 280,5.4 281,6C282.4,6.8 283.4,7.6 284,8.5C284.6,9.3 284.9,10.4 284.9,11.8L284.9,16.5C284.9,18.6 284.1,19.7 282.6,19.7C281.8,19.7 280.5,19.3 278.8,18.5C273.1,15.9 266.7,14.6 259.6,14.6C253.9,14.6 249.4,15.5 246.3,17.4C243.2,19.3 241.6,22.2 241.6,26.3C241.6,29.1 242.6,31.5 244.6,33.4C246.6,35.3 250.3,37.2 255.6,38.9L269.8,43.4C277,45.7 282.2,48.9 285.3,53C288.4,57.1 289.9,61.8 289.9,67C289.9,71.3 289,75.2 287.3,78.6C285.5,82 283.1,85 280,87.4C276.9,89.9 273.2,91.7 268.9,93C264.4,94.4 259.7,95.1 254.6,95.1Z"
															style="fill:rgb(214,214,214);fill-rule:nonzero;"
														/>
														<g>
															<path d="M273.5,143.7C240.6,168 192.8,180.9 151.7,180.9C94.1,180.9 42.2,159.6 3,124.2C-0.1,121.4 2.7,117.6 6.4,119.8C48.8,144.4 101.1,159.3 155.2,159.3C191.7,159.3 231.8,151.7 268.7,136.1C274.2,133.6 278.9,139.7 273.5,143.7Z" style="fill:rgb(255,153,0);" />
															<path d="M287.2,128.1C283,122.7 259.4,125.5 248.7,126.8C245.5,127.2 245,124.4 247.9,122.3C266.7,109.1 297.6,112.9 301.2,117.3C304.8,121.8 300.2,152.7 282.6,167.5C279.9,169.8 277.3,168.6 278.5,165.6C282.5,155.7 291.4,133.4 287.2,128.1Z" style="fill:rgb(255,153,0);" />
														</g>
													</g>
												</g>
											</svg>
										</a>
									{/if}
								</div>
								<div class="items-center text-xl hidden md:flex">
									•
								</div>
								<div class="flex items-center text-sm lg:text-base mt-2 md:mt-0 md:ml-5 font-bold text-white">
									{#if item.repo}
										 <a class="text-white underline underline-offset-4 decoration-1	underline-offset-4 hover:decoration-[#4166ab] hover:decoration-1 mr-4" href="{item.repo}">View Repository</a>
										 <div class="flex items-center lg:text-base mr-4">
											 •
										 </div>
									{/if}
									<a class="underline text-white decoration-1	underline-offset-4 hover:decoration-[#4166ab] hover:decoration-1 mr-6" href="{item.url}">Visit Website</a>
									<!-- ➟ -->
								</div>
								
							</div>
						</div>

						<!-- <p>{i}</p> -->

						<!-- content here -->
						<div class="relative">
							<div class="mobile_render md:mt-[3.5%] md:ml-[6vw]">
								<iframe title="Mobile version of {item.url}" class="md:h-[26.75vw] md:w-[14.75vw] mt-[9vw] h-[63.5vw] w-[34.9vw] mr-[-5.75vw] md:mt-[2.2vw] md:mr-[5.45vw]" src={item.url} style="-webkit-transform:scale(0.59);-moz-transform-scale(0.59);" />
								<img src="phone.png" class="w-[23vw] mt-[18vw] md:w-[9.65vw] md:mr-[8vw] md:mt-[6vw]" alt="" />
							</div>
							<div class="desktop_render md:mr-[15%] mt-0">
								<iframe title="Desktop version of {item.url}" class="md:mt-[-10vw] md:mr-[-11vw] md:w-[64.75vw] md:h-[36.5vw] mt-[-12vw] mr-[-21vw] h-[71.5vw] w-[125vw]" src={item.url} style="-webkit-transform:scale(0.5);-moz-transform-scale(0.5);" />
								<img src="laptop-png-grey.png" class="h-[60vw] mt-[7vw] lg:mt-[unset] md:mt-0 md:h-[30.8vw]" alt="" />
							</div>
						</div>
					</div>
					<!-- {:else if count == undefined}
						<p>count undefined</p>
					{/if} -->

					<!-- <iframe src="http://localhost:8888"></iframe> -->
				</section>
			{/each}
		</div>
	<!-- </Scroller> -->
</section>

<style>
	section {
		flex: 1;
	}

	.main .title {
		padding-bottom: 0.5vw;
	}

	.desktop_render {
		width: 100%;
		justify-content: flex-end;
		display: flex;
		height: 100%;
		align-items: center;
	}

	.mobile_render {
		justify-content: flex-end;
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
	}

	.textual {
		left: 0;
	}

	.textual h1 {
		margin-block-start: 0;
		margin-block-end: 0;
	}

	.desktop_render iframe {
		z-index: 200;
		position: absolute;
	}

	.mobile_render img {
		position: absolute;

		z-index: 220;
	}

	.mobile_render iframe {
		z-index: 230;
		border: none !important;
	}

	:global(svelte-scroller-outer) {
		width: 100%;
	}

	:global(svelte-scroller-background) {
		height: 80vh !important;
		display: flex !important;
		align-items: center;
	}

	.main {
		background-color: #101011d8;
		z-index: 100;
		padding-top: 2.25vw;
	}

	h1 {
		width: 100%;
	}

	section {
		color: white;
		padding: 1em;
		margin: 0 0 2em 0;
	}
</style>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<script lang="ts">
	import { onMount } from "svelte";

	let article: {
		title: string;
		body: string;
	};
	
	async function getArticle() {
		const res = await fetch(`https://jsonplaceholder.typicode.com/posts/1`);
		const data = await res.json();
		return data;
	}

	onMount(async () => {
		article = await getArticle();
	});
</script>

<div class="px-3">
	<h1 class="py-3">About this project</h1>

	<p>This is my school project made in the last year of High School in 2023/24.</p>
	
	
</div>